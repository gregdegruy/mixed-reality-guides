import adal
import json
import logging
import os
import sys

class AzureAuth():
    hdd = ''

    def __init__(self, hdd):
        self.hdd = hdd
        print("Creating class")
        
