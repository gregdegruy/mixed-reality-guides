import uuid

from .msmrwguidestep import MSMRWGuideStep

class MSMRWGuideTask:
    
    taskJson = {}
    
    def __init__(self, Name):
        self.taskJson = {
            "Id": str(uuid.uuid4()),
            "Type": "Microsoft.Guides.Schema.IGuideTask",
            "Name": "Task name",
            "Steps": []
        }