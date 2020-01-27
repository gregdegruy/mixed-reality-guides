import uuid

class MSMRWGuideAlignmentStep:
    
    alignmentStepJson = {}

    def __init__():
        self.alignmentStepJson = {
            "Id": str(uuid.uuid4()),
            "Type": "Microsoft.Guides.Schema.IAlignment",
            "InstructionText": "1. Align \"digital anchor\" hologram to a real world object:\n     o Tap and hold the hologram to move\n     o Tap and hold the blue spheres to rotate\n\n2. Select \"Confirm\" when you are done.",
            "Tether": {
                "Id": "4181a318-fb23-42db-99c6-86b41ceea700",
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
                "AttachedTo": 3
            },
            "Media": [
                null
            ],
            "DigitalTwin": {
                "Id": "c31962b8-4a8f-4e3b-9ed6-8d0ea2538f8d",
                "Type": "Microsoft.Guides.Schema.IModelRef",
                "AssetId": "8d856ff1-abb3-e911-a812-000d3af46b49",
                "RenderMode": 0
            },
            "StepMode": 1,
            "AlignmentModelType": 0
        }