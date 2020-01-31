import msal # works for api with application permissions

try:
    from guidesencoder.config import DevConfig
except ImportError:
    import sys
    sys.path.append('.')
    from guidesencoder.config import DevConfig

class AzureAuth:
    bearerToken = ""
    cache = None
    confidentialClient = None

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
    
    def get_token_from_cache(self, cache):
        if self.confidentialClient.get_accounts():
            result = self.confidentialClient.acquire_token_silent(scope, account=self.confidentialClient.get_accounts()[0])
            _save_cache(cache)
            return result
    
    def refreshToken():
        pass
