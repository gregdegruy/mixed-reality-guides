from flask import Flask, render_template, session, request, redirect, url_for
from flask_session import Session
import msal
import requests
import uuid

try:
    from guidesencoder.app.msmrw.azureauth import AzureAuth
    from guidesencoder.app.msmrw.guide import Guide
    from guidesencoder.config import DevConfig
except ImportError:
    import sys
    sys.path.append('.')
    from guidesencoder.app.msmrw.azureauth import AzureAuth
    from guidesencoder.app.msmrw.guide import Guide
    from guidesencoder.config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)
Session(app)
azureAuth = AzureAuth()
guide = Guide("PY Guide")

@app.route("/")
def index():    
    if not session.get("user"):
        return redirect(url_for("login"))
    return render_template('index.html', user=session["user"], version=msal.__version__)

@app.route("/login")
def login():
    session["state"] = str(uuid.uuid4())
    auth_url = _build_auth_url()
    return render_template("login.html", auth_url=auth_url, version=msal.__version__)

@app.route(DevConfig.REDIRECT_PATH)
def authorized():
    if request.args.get('state') != session.get("state"):
        return redirect(url_for("index"))
    if "error" in request.args:
        return render_template("auth_error.html", result=request.args)
    if request.args.get('code'):
        azureAuth.load_cache(session)
        azureAuth.build_msal_app()
        result = azureAuth.acquire_token_by_authorization_code(
            request.args['code'],
            url_for("authorized", _external=True))
        if "error" in result:
            return render_template("auth_error.html", result=result)
        session["user"] = result.get("id_token_claims")
        session["token_cache"] = azureAuth.save_cache()
    return redirect(url_for("index"))

@app.route("/logout")
def logout():
    session.clear() 
    return redirect( 
        DevConfig.AUTHORITY_MULTI_TENANT + "/oauth2/v2.0/logout" +
        "?post_logout_redirect_uri=" + url_for("index", _external=True))

@app.route("/getguide")
def getGuides():
    token = azureAuth.get_token_from_cache(session)
    session["token_cache"] = azureAuth.save_cache()
    if not token:
        return redirect(url_for("login"))    
    graph_data = requests.get(
        str(DevConfig.CDS_API_URL + "/msmrw_guides?$select=msmrw_name&$expand=msmrw_guide_Annotations"),
        headers={'Authorization': 'Bearer ' + token['access_token']},
        ).json()
    return render_template('display.html', result=graph_data)

@app.route("/postguide")
def postGuides():
    token = azureAuth.get_token_from_cache(session)
    session["token_cache"] = azureAuth.save_cache()
    if not token:
        return redirect(url_for("login"))    
    guideNmae = "PY Guide"
    payload = "{\r\n    \"msmrw_schemaversion\": 3,\r\n    \"msmrw_name\": \"" + guideNmae + "\",\r\n    \"msmrw_guide_Annotations\": [\r\n    \t{\r\n\t        \"mimetype\": \"application/octet-stream\",\r\n\t\t\t\"isdocument\": true,\r\n\t        \"filename\": \"Name it whatever.json\"\r\n    \t}\r\n\t]\r\n}"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token['access_token']
    }
    graph_data = requests.request("POST", 
        str(DevConfig.CDS_API_URL + "/msmrw_guides?$select=msmrw_name&$expand=msmrw_guide_Annotations"), 
        headers=headers, 
        data=payload)
    return render_template('display.html', result=str("Post complete" + graph_data.text))

def _build_auth_url():
    return azureAuth.get_auth_url(session["state"], url_for("authorized", _external=True))

app.jinja_env.globals.update(_build_auth_url=_build_auth_url) 

if __name__ == "__main__":
    app.run()
