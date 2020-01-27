import adal

from .config import *

class AzureAuth:
    bearerToken = ""

    def __init__(self):
        authCtx = adal.AuthenticationContext(AUTHORITY_URL)
        tokenResponse = authCtx.acquire_token_with_client_credentials(RESOURCE, CLIENT_ID, CLIENT_SECRET)
        self.bearerToken = tokenResponse["accessToken"]
        print("got token")          
    
    def refreshToken():
        pass
