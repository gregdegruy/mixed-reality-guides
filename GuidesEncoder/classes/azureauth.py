import json
import logging
import os
import platform
import sys


class AzureAuth:
    hdd = ""
    path = ""

    def __init__(self, hdd, path):
        self.hdd = hdd
        print("Creating class")
        if platform.system() == "Windows":
            self.path = os.getcwd() + "\\" + "filename"
        elif platform.system() == "Linux":
            self.path = os.getcwd() + "/" + "filename"
        print(self.path)

    def readConfig():
        # with open(os.getcwd() + "\\GuidesEncoder\\steps\\in.json", encoding="utf8") as jsonfile:
        #     data = json.load(jsonfile)
        #     datastr = json.dumps(data)
        #     encoded = base64.b64encode(datastr.encode("utf-8"))
        print("done")
        