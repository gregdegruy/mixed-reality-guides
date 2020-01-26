import base64
import json

with open('C:\\Users\\grego\\Documents\\GitHub\\greg\\guides-entity-temp\\GuidesEncoder\\in.json', encoding="utf8") as jsonfile:
    data = json.load(jsonfile)
    datastr = json.dumps(data)
    encoded = base64.b64encode(datastr.encode('utf-8'))
    print("done")

j = {"Schema":"GuidesV3","Guide":{"Id":"14f1b784-87e6-4ec8-a966-9828ca0983f8","Type":"Microsoft.Guides.Schema.IGuide","Name":"Just Steps Text Guide","Tasks":[{"Id":"a0cc74cc-1713-4ae8-ba8b-508bba1f9c46","Type":"Microsoft.Guides.Schema.IGuideTask","Name":"Task name","Steps":[{"Id":"879b78f1-ebad-46ad-82f1-eb6363a3a817","Type":"Microsoft.Guides.Schema.IGuideStep","InstructionText":"This is step 1 of all my tasks","Tether":{"Id":"3fef234d-36b9-41d7-b6ce-3aeb5e09e1e6","Type":"Microsoft.Guides.Schema.ITether","Transform":{"Position":[0.0,0.0,0.0],"Rotation":[0.0,0.0,0.0,0.0],"Scale":[0.0,0.0,0.0]},"IsPlacedInWorld":false,"DisableAnimation":false,"RenderMode":0,"AssetId":"00000000-0000-0000-0000-000000000000","TetheredAsset":"00000000-0000-0000-0000-000000000000","AttachedTo":0},"Media":[],"PartTemplates":[],"StepMode":0}]}],"AlignmentStep":{"Id":"40a99c91-902c-49d9-82c9-a5fdc20390fa","Type":"Microsoft.Guides.Schema.IAlignment","InstructionText":"1. Align “digital anchor” hologram to a real world object:\n     o Tap and hold the hologram to move\n     o Tap and hold the blue spheres to rotate\n\n2. Select ‘Confirm’ when you are done.","Tether":{"Id":"321351c1-1e31-46a4-89ae-90f798e46465","Type":"Microsoft.Guides.Schema.ITether","Transform":{"Position":[0.0,0.0,0.0],"Rotation":[0.0,0.0,0.0,0.0],"Scale":[0.0,0.0,0.0]},"IsPlacedInWorld":false,"DisableAnimation":false,"RenderMode":0,"AssetId":"00000000-0000-0000-0000-000000000000","TetheredAsset":"00000000-0000-0000-0000-000000000000","AttachedTo":3},"Media":[null],"DigitalTwin":{"Id":"c31962b8-4a8f-4e3b-9ed6-8d0ea2538f8d","Type":"Microsoft.Guides.Schema.IModelRef","AssetId":"8d856ff1-abb3-e911-a812-000d3af46b49","RenderMode":0},"StepMode":1,"AlignmentModelType":0},"CompletionStep":{"Id":"42492eb2-3bb3-4f6d-956f-8b17a9c5816d","Type":"Microsoft.Guides.Schema.IGuideStep","InstructionText":"Congratulations! You successfully completed this guide.","Tether":{"Id":"436404ae-9e2e-4836-acf2-d26e2e3e5577","Type":"Microsoft.Guides.Schema.ITether","Transform":{"Position":[0.0,0.0,0.0],"Rotation":[0.0,0.0,0.0,0.0],"Scale":[0.0,0.0,0.0]},"IsPlacedInWorld":false,"DisableAnimation":false,"RenderMode":0,"AssetId":"00000000-0000-0000-0000-000000000000","TetheredAsset":"00000000-0000-0000-0000-000000000000","AttachedTo":0},"Media":[],"PartTemplates":[],"StepMode":0}}}
s = json.dumps(j)  # Turns your json dict into a str
print(s)
dd = base64.b64encode(s)
print(s)
