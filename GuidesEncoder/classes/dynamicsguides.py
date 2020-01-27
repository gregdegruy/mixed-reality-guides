import base64
import json
import os
import platform
import uuid

from .azureauth import AzureAuth
from .config import *

class DynamicsGuides:
    url = ""
    def __init__(self):
        self.url = CDS_API_URL + "/msmrw_guides?$expand=msmrw_guide_Annotations"

    def get(self):        
        payload  = {}
        headers = {
            "Authorization": "Bearer " + token_response["accessToken"]
        }

        response = requests.request("GET", self.url, headers=headers, data=payload)

        print(response.text.encode("utf8"))

    def createGuide(self):
        j = {"msmrw_schemaversion": 3, "msmrw_name": "REST Guide 1", "msmrw_guide_Annotations": [{"mimetype": "application/octet-stream", "isdocument": true, "filename": "Name it whatever.json"}]}
        jStr = json.dumps(j1)

    def addGuideFile(self):
        # TODO: Grab these from createGuide
        guideId = "bfa368fc-a440-ea11-a812-000d3a569653"
        annotationId = "c0a368fc-a440-ea11-a812-000d3a569653"
        pass

    def createGuideFile(self):
        # TODO: don't forget the guide id
        guideId = "bfa368fc-a440-ea11-a812-000d3a569653"
        
        # TODO: generate GUID for each Tasks, AlignmentStep, and CompletionStep
        g = str(uuid.uuid4())
        print(g)

        sampleDiagnosis = "https://beta.revtwo.com/session/L9X26twMg3cRTBnvmPkq4KVJbWNCHj?navcode=5cGZd3fFhz"
        domStepClass = "stepbox-frame"
        guideFilePath = ""
        encoded = ""
        
        if platform.system() == "Windows":
            guideFilePath = os.getcwd() + "\\GuidesEncoder\\steps\\in.json"
        elif platform.system() == "Linux":
            guideFilePath = os.getcwd() + "/GuidesEncoder/steps/in.json"
        with open(guideFilePath, encoding="utf8") as jsonfile:
            data = json.load(jsonfile)
            datastr = json.dumps(data)
            encoded = base64.b64encode(datastr.encode("utf-8"))
            print("done")
        f = open(os.getcwd() + "\\GuidesEncoder\\steps\\out.txt", "w")
        f.write(encoded.decode("utf-8"))
        f.close()
