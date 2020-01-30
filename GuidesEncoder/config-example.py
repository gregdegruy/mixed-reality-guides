class Config(object):
    DEBUG = False

class DevConfig(Config):
    AUTHORITY_MULTI_TENANT="https://login.microsoftonline.com/common"
    AUTHORITY_SINGLE_TENANT="https://login.microsoftonline.com/put_your_tenant"
    CDS_API_URL=""
    CLIENT_ID=""
    CLIENT_SECRET=""
    DEBUG = True
    REDIRECT_URI=""
    REDIRECT_PATH=""
    RESOURCE="" # like "https://your_cds_environment.api.crm.dynamics.com/"
    SCOPE = [] # like https://your_cds_environment.api.crm.dynamics.com/user_impersonation
    SESSION_TYPE = "filesystem"
