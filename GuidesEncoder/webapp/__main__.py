from flask import Flask, render_template, session, request, redirect, url_for
from flask_session import Session
import msal
import requests
import uuid

# from ..config import Config

from .config import DevConfig

app = Flask(__name__)
config = DevConfig
app.config.from_object(config)
app.config["CLIENT_SECRET"] = "0JKAaSQKItx5YGr7gNNmspq7rYFuiYLZKLjoVdfvnAE="
app.config["SESSION_TYPE"] = "filesystem"

@app.route("/")
def index():
    if not session.get("user"):
        return redirect(url_for("login"))
    return render_template('index.html', user=session["user"], version=msal.__version__)

@app.route("/login")
def login():
    session["state"] = str(uuid.uuid4())
    # here we choose to also collect end user consent upfront 
    auth_url = _build_auth_url(scopes=config.SCOPE, state=session["state"])
    return render_template("login.html", auth_url=auth_url, version=msal.__version__)

@app.route(config.REDIRECT_PATH)  # Its absolute URL must match your app's redirect_uri set in AAD
def authorized():
    if request.args.get('state') != session.get("state"):
        return redirect(url_for("index"))
    if "error" in request.args:
        return render_template("auth_error.html", result=request.args)
    if request.args.get('code'):
        cache = _load_cache()
        result = _build_msal_app(cache=cache).acquire_token_by_authorization_code(
            request.args['code'],
            scopes=config.SCOPE,
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
        config.AUTHORITY_MULTI_TENANT + "/oauth2/v2.0/logout" +
        "?post_logout_redirect_uri=" + url_for("index", _external=True))

@app.route("/graphcall")
def graphcall():
    token = _get_token_from_cache(config.SCOPE)
    if not token:
        return redirect(url_for("login"))    
    print("token " + token['access_token'])
    graph_data = requests.get(
        str(config.CDS_API_URL + "/msmrw_guides?$select=msmrw_name&$expand=msmrw_guide_Annotations"),
        headers={'Authorization': 'Bearer ' + token['access_token']},
        ).json()
    print(str(graph_data))
    return render_template('display.html', result=graph_data)


def _load_cache():
    cache = msal.SerializableTokenCache()
    if session.get("token_cache"):
        cache.deserialize(session["token_cache"])
    return cache

def _save_cache(cache):
    if cache.has_state_changed:
        session["token_cache"] = cache.serialize()

def _build_msal_app(cache=None, authority=None):
    return msal.ConfidentialClientApplication(
        config.CLIENT_ID, authority=authority or config.AUTHORITY_MULTI_TENANT,
        client_credential=config.CLIENT_SECRET, token_cache=cache)

def _build_auth_url(authority=None, scopes=None, state=None):
    return _build_msal_app(authority=authority).get_authorization_request_url(
        scopes or [],
        state=state or str(uuid.uuid4()),
        redirect_uri=url_for("authorized", _external=True))

def _get_token_from_cache(scope=None):
    cache = _load_cache() 
    cca = _build_msal_app(cache=cache)
    accounts = cca.get_accounts()
    if accounts:  # So all account(s) belong to the current signed-in user
        result = cca.acquire_token_silent(scope, account=accounts[0])
        _save_cache(cache)
        return result

app.jinja_env.globals.update(_build_auth_url=_build_auth_url) 

if __name__ == "__main__":
    app.run()
