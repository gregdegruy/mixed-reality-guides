import uuid

from .msmrwguidestep import MSMRWGuideStep

class MSMRWGuideTask:
    
    taskJson = {}
    
    def __init__(self, name):
        step1 = MSMRWGuideStep("Select the Menu from the upper right corner of the printer's touch screen.")
        step2 = MSMRWGuideStep("Select the Utilities tile from the available options.")
        step3 = MSMRWGuideStep("Select the Temperature Control tile from the available options.")
        step4 = MSMRWGuideStep("Select the Heat option on the screen when prompted.")
        step5 = MSMRWGuideStep("Remove the thumb screw that connects the fiber Bowden tube to the print head.")
        step6 = MSMRWGuideStep("Look down throught the print head channel to verify that the print head blockage is clear.")
        self.taskJson = {
            "Id": str(uuid.uuid4()),
            "Type": "Microsoft.Guides.Schema.IGuideTask",
            "Name": name,
            "Steps": [
                step1.stepJson,
                step2.stepJson,
                step3.stepJson,
                step4.stepJson,
                step5.stepJson,
                step6.stepJson
            ]
        }