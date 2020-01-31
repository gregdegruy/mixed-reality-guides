﻿import msal # works for api with application permissions

try:
    from guidesencoder.config import DevConfig
except ImportError:
    import sys
    sys.path.append('.')
    from guidesencoder.config import DevConfig

class AzureAuth:
   
    def __init__(self):
       self.cache = msal.SerializableTokenCache()
       self.confidentialClient = msal.ConfidentialClientApplication(
            DevConfig.CLIENT_ID, 
            authority=DevConfig.AUTHORITY_MULTI_TENANT,
            client_credential=DevConfig.CLIENT_SECRET, 
            token_cache=self.cache)
    
    def get_auth_url(self, state=None, redirect_uri=None):
        return self.confidentialClient.get_authorization_request_url(
            DevConfig.SCOPE or [],
            state=state or str(uuid.uuid4()),
            redirect_uri=redirect_uri)

    def acquire_token_by_authorization_code(self, authCodeFromServer, redirectUri):
        return self.confidentialClient.acquire_token_by_authorization_code(
            authCodeFromServer,
            scopes=DevConfig.SCOPE,
            redirect_uri=redirectUri)
    
    def load_cache(self, flaskSession):
        if flaskSession.get("token_cache"):
            self.cache.deserialize(flaskSession["token_cache"])
        return self.cache

    def save_cache(self, cache):
        if self.cache.has_state_changed:
            self.cache = cache
        return self.cache.serialize()
    
    def refreshToken():
        pass
