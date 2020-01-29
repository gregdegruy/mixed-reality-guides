import uuid

class GuideStep:
  
    stepJson = {}

    def __init__(self, instructionText):
        self.stepJson = {
            "Id": str(uuid.uuid4()),
            "Type": "Microsoft.Guides.Schema.IGuideStep",
            "InstructionText": instructionText,
            "Tether": {
                "Id": str(uuid.uuid4()),
                "Type": "Microsoft.Guides.Schema.ITether",
                "Transform": {
                    "Position": [0.0, 0.0, 0.0],
                    "Rotation": [0.0, 0.0, 0.0, 0.0],
                    "Scale": [0.0, 0.0, 0.0]
                },
                "IsPlacedInWorld": False,
                "DisableAnimation": False,
                "RenderMode": 0,
                "AssetId": "00000000-0000-0000-0000-000000000000",
                "TetheredAsset": "00000000-0000-0000-0000-000000000000",
                "AttachedTo": 0
            },
            "Media": [],
            "PartTemplates": [],
            "StepMode": 0
        }
