import uuid

from .msmrwguidestep import MSMRWGuideStep

class MSMRWGuideTask:
    
    taskJson = {}
    
    def __init__(self, Name):
        step1 = MSMRWGuideStep("Step one text")
        step2 = MSMRWGuideStep("Step two text")
        self.taskJson = {
            "Id": str(uuid.uuid4()),
            "Type": "Microsoft.Guides.Schema.IGuideTask",
            "Name": "Task name",
            "Steps": [
                step1.stepJson,
                step2.stepJson
            ]
        }