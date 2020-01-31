from flask import Flask, render_template, session, request, redirect, url_for
from flask_session import Session
import msal
import requests
import uuid

from guidesencoder.config import DevConfig

try:
    from guidesencoder.app.msmrw.azureauth import AzureAuth
except ImportError:
    import sys
    sys.path.append('.')
    from guidesencoder.app.msmrw.azureauth import AzureAuth

app = Flask(__name__)
app.config.from_object(DevConfig)
Session(app)
azureAuth = AzureAuth()

@app.route("/")
def index():    
    if not session.get("user"):
        return redirect(url_for("login"))
    return render_template('index.html', user=session["user"], version=msal.__version__)

@app.route("/login")
def login():
    session["state"] = str(uuid.uuid4())
    auth_url = _build_auth_url(scopes=DevConfig.SCOPE, state=session["state"])
    return render_template("login.html", auth_url=auth_url, version=msal.__version__)

@app.route(DevConfig.REDIRECT_PATH)  # Its absolute URL must match your app's redirect_uri set in AAD
def authorized():
    if request.args.get('state') != session.get("state"):
        return redirect(url_for("index"))
    if "error" in request.args:
        return render_template("auth_error.html", result=request.args)
    if request.args.get('code'):
        cache = _load_cache()
        result = azureAuth.confidentialClient.acquire_token_by_authorization_code(
            request.args['code'],
            scopes=DevConfig.SCOPE,
            redirect_uri=url_for("authorized", _external=True))
        if "error" in result:
            return render_template("auth_error.html", result=result)
        session["user"] = result.get("id_token_claims")
        _save_cache(cache)
    return redirect(url_for("index"))

@app.route("/logout")
def logout():
    session.clear() 
    return redirect( 
        DevConfig.AUTHORITY_MULTI_TENANT + "/oauth2/v2.0/logout" +
        "?post_logout_redirect_uri=" + url_for("index", _external=True))

@app.route("/getguide")
def getGuides():
    token = _get_token_from_cache(DevConfig.SCOPE)
    if not token:
        return redirect(url_for("login"))    
    graph_data = requests.get(
        str(DevConfig.CDS_API_URL + "/msmrw_guides?$select=msmrw_name&$expand=msmrw_guide_Annotations"),
        headers={'Authorization': 'Bearer ' + token['access_token']},
        ).json()
    return render_template('display.html', result=graph_data)

@app.route("/postguide")
def postGuides():
    token = _get_token_from_cache(DevConfig.SCOPE)
    if not token:
        return redirect(url_for("login"))    
    guideNmae = "REST Guide 22"
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

def _load_cache():
    if session.get("token_cache"):
        azureAuth.cache.deserialize(session["token_cache"])
    return azureAuth.cache
    
def _save_cache(cache):
    if azureAuth.cache.has_state_changed:
        azureAuth.cache = cache
        session["token_cache"] = azureAuth.cache.serialize()

def _build_auth_url(authority=None, scopes=None, state=None):
    return azureAuth.get_auth_url(state, url_for("authorized", _external=True))

def _get_token_from_cache(scope=None):
    cache = _load_cache()
    if azureAuth.confidentialClient.get_accounts():
        result = azureAuth.confidentialClient.acquire_token_silent(scope, account=azureAuth.confidentialClient.get_accounts()[0])
        _save_cache(cache)
        return result 

app.jinja_env.globals.update(_build_auth_url=_build_auth_url) 

if __name__ == "__main__":
    app.run()
