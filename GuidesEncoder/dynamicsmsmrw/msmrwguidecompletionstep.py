import uuid

class MSMRWGuideCompletionStep:
    
    completionStepJson = {}
    
    def __init__(self, instructionText):
        self.completionStepJson = {
            "Id": str(uuid.uuid4()),
            "Type": "Microsoft.Guides.Schema.IGuideStep",
            "InstructionText": instructionText,
            "Tether": {
                "Id": "3fc4f1c4-9520-4ac3-bc3d-b61852edc13b",
                "Type": "Microsoft.Guides.Schema.ITether",
                "Transform": {
                "Position": [
                    0.0,
                    0.0,
                    0.0
                ],
                "Rotation": [
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "Scale": [
                    0.0,
                    0.0,
                    0.0
                ]
                },
                "IsPlacedInWorld": false,
                "DisableAnimation": false,
                "RenderMode": 0,
                "AssetId": "00000000-0000-0000-0000-000000000000",
                "TetheredAsset": "00000000-0000-0000-0000-000000000000",
                "AttachedTo": 0
            },
            "Media": [
                null
            ],
            "PartTemplates": [
                null
            ],
            "StepMode": 0
        }