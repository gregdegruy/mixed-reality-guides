import adal
import msal

from .config import *

class AzureAuth:
    bearerToken = ""

    def __init__(self):
        authCtx = adal.AuthenticationContext(AUTHORITY_URL)
        tokenResponse = authCtx.acquire_token_with_client_credentials(RESOURCE, CLIENT_ID, CLIENT_SECRET)
        self.bearerToken = tokenResponse["accessToken"]
        print("got token")          

        app = msal.ConfidentialClientApplication(CLIENT_ID, authority=AUTHORITY_URL, client_credential=CLIENT_SECRET)

        result = None
        result = app.acquire_token_silent(["https://grdegr.onmicrosoft.com/73a06a75-ca39-4442-be8a-2e6c79b622f7/.default"], account=None)

        if not result:
            result = app.acquire_token_for_client(scopes=["https://grdegr.onmicrosoft.com/73a06a75-ca39-4442-be8a-2e6c79b622f7/.default"])
        print("")
    
    def refreshToken():
        pass
