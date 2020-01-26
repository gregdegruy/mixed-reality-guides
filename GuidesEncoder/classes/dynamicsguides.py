import base64
import json
import os
import platform

from .azureauth import AzureAuth

class DynamicsGuides:
    hdd = ""

    def __init__(self):
        pass

    def get(self):
        url = CDS_API_URL + "/msmrw_guides?$expand=msmrw_guide_Annotations"
        payload  = {}
        headers = {
            "Authorization": "Bearer " + token_response["accessToken"]
        }

        response = requests.request("GET", url, headers=headers, data = payload)

        print(response.text.encode("utf8"))

    def createGuideFile(self):
        sampleDiagnosis = "https://beta.revtwo.com/session/L9X26twMg3cRTBnvmPkq4KVJbWNCHj?navcode=5cGZd3fFhz"
        domStepClass = "stepbox-frame"
        guideFilePath = ""
        if platform.system() == "Windows":
            guideFilePath = os.getcwd() + "\\GuidesEncoder\\steps\\in.json"
        elif platform.system() == "Linux":
            guideFilePath = os.getcwd() + "/GuidesEncoder/steps/in.json"
        with open(guideFilePath, encoding="utf8") as jsonfile:
            data = json.load(jsonfile)
            datastr = json.dumps(data)
            encoded = base64.b64encode(datastr.encode("utf-8"))
            print("done")
