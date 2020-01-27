import base64
import json
import os
import platform
import uuid

from .azureauth import AzureAuth
from .config import *
from .msmrwguidealignmentstep import MSMRWGuideAlignmentStep
from .msmrwguidecompletionstep import MSMRWGuideCompletionStep
from .msmrwguidetask import MSMRWGuideTask

class MSMRWGuide:
    annotationId = ""
    guideId = ""
    guidesFolder =""
    url = ""

    def __init__(self):
        self.url = CDS_API_URL + "/msmrw_guides?$expand=msmrw_guide_Annotations"
        if platform.system() == "Windows":
            self.guidesFolder = os.getcwd() + "\\GuidesEncoder\\dynamicsmsmrw\\guides\\"
        elif platform.system() == "Linux":
            self.guidesFolder = os.getcwd() + "/GuidesEncoder/dynamicsmsmrw/guides/"

    def get(self):        
        payload  = {}
        headers = {
            "Authorization": "Bearer " + token_response["accessToken"]
        }
        response = requests.request("GET", self.url, headers=headers, data=payload)
        print(response.text.encode("utf8"))

    def getStepsFromHtml(self):
        sampleDiagnosis = "https://beta.revtwo.com/session/L9X26twMg3cRTBnvmPkq4KVJbWNCHj?navcode=5cGZd3fFhz"
        domStepClass = "stepbox-frame"

    def createGuide(self):
        j = {"msmrw_schemaversion": 3, "msmrw_name": "REST Guide 1", "msmrw_guide_Annotations": [{"mimetype": "application/octet-stream", "isdocument": true, "filename": "Name it whatever.json"}]}
        jStr = json.dumps(j1)
        # TODO: Save Guide Id and annotationId

    def addGuideFile(self):
        # TODO: Grab these from createGuide
        guideId = "bfa368fc-a440-ea11-a812-000d3a569653"
        annotationId = "c0a368fc-a440-ea11-a812-000d3a569653"
        pass

    def createGuideFile(self):
        # TODO: don't forget the guide id
        guideId = "bfa368fc-a440-ea11-a812-000d3a569653"
        
        # TODO: generate GUID for each Task, AlignmentStep, and CompletionStep
        g = str(uuid.uuid4())        
       
        with open(self.guidesFolder + "in.json", "r+") as guideFile:
            data = json.load(guideFile)
            data["Guide"]["Id"] = guideId
            data["Guide"]["Tasks"][0]["Steps"][0]["InstructionText"] = "And Knucks"
            guideFile.seek(0)  
            json.dump(data, guideFile, indent=2)
            guideFile.truncate()
            guideFile.close()
        
    def encodeGuideFile(self):
        with open(self.guidesFolder + "in.json", encoding="utf8") as guideFile:
            data = json.load(guideFile)
            datastr = json.dumps(data)
            encoded = base64.b64encode(datastr.encode("utf-8"))
            guideFile.close()
            encodedGuideFile = open(self.guidesFolder + "out.json", "w")
            encodedGuideFile.write(encoded.decode("utf-8"))
            encodedGuideFile.close()