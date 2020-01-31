import base64
import json
import os
import platform
import uuid

try:
    from guidesencoder.config import DevConfig
except ImportError:
    import sys
    sys.path.append('.')
    from guidesencoder.config import DevConfig

from .guidealignmentstep import GuideAlignmentStep
from .guidecompletionstep import GuideCompletionStep
from .guidetask import GuideTask

class Guide:

    def __init__(self, name):
        self.url = DevConfig.CDS_API_URL + "/msmrw_guides?$expand=msmrw_guide_Annotations"
        if platform.system() == "Windows":
            self.guidesFolder = os.getcwd() + "\\GuidesEncoder\\app\\msmrw\\guides\\"
        elif platform.system() == "Linux":
            self.guidesFolder = os.getcwd() + "/GuidesEncoder/app/msmrw/guides/"
        self.guideJson = {
            "Schema": "GuidesV3",
            "Guide": {
                "Id": "00000000-0000-0000-0000-000000000000",
                "Type": "Microsoft.Guides.Schema.IGuide",
                "Name": name,
                "Tasks": [{}],
                "AlignmentStep": {},
                "CompletionStep": {}
            }
        }
        self.task = GuideTask("Manually heat the nozzle to remove the jam ")
        self.alignmentStep = GuideAlignmentStep()
        self.completionStep = GuideCompletionStep("You're done! To finish up please do...")

    def get(self):        
        pass

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
            self.guideJson["Guide"]["Id"] = guideId
            self.guideJson["Guide"]["Tasks"][0] = self.task.taskJson
            self.guideJson["Guide"]["AlignmentStep"] = self.alignmentStep.alignmentStepJson
            self.guideJson["Guide"]["CompletionStep"] = self.completionStep.completionStepJson
            json.dump(self.guideJson, guideFile, indent=2)
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
