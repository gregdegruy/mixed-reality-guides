import adal
import logging
import os
import platform
import sys

from .config import *

class AzureAuth:
    hdd = ""

    def __init__(self, hdd):
        self.hdd = hdd
        print("Creating class")
        auth_context = adal.AuthenticationContext(AUTHORITY_URL)
        token_response = auth_context.acquire_token_with_client_credentials(RESOURCE, CLIENT_ID, CLIENT_SECRET)
        print("Done")
