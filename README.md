
```sh
cat in.json | tr -d '\r\n[:space:]' > out.json
```

```bash
eyJTY2hlbWEiOiJHdWlkZXNWMyIsIkd1aWRlIjp7IklkIjoiMTRmMWI3ODQtODdlNi00ZWM4LWE5NjYtOTgyOGNhMDk4M2Y4IiwiVHlwZSI6Ik1pY3Jvc29mdC5HdWlkZXMuU2NoZW1hLklHdWlkZSIsIk5hbWUiOiJKdXN0IFN0ZXBzIFRleHQgR3VpZGUiLCJUYXNrcyI6W3siSWQiOiJhMGNjNzRjYy0xNzEzLTRhZTgtYmE4Yi01MDhiYmExZjljNDYiLCJUeXBlIjoiTWljcm9zb2Z0Lkd1aWRlcy5TY2hlbWEuSUd1aWRlVGFzayIsIk5hbWUiOiJUYXNrIG5hbWUiLCJTdGVwcyI6W3siSWQiOiI4NzliNzhmMS1lYmFkLTQ2YWQtODJmMS1lYjYzNjNhM2E4MTciLCJUeXBlIjoiTWljcm9zb2Z0Lkd1aWRlcy5TY2hlbWEuSUd1aWRlU3RlcCIsIkluc3RydWN0aW9uVGV4dCI6IlRoaXMgaXMgc3RlcCAxIG9mIGFsbCBteSB0YXNrcyIsIlRldGhlciI6eyJJZCI6IjNmZWYyMzRkLTM2YjktNDFkNy1iNmNlLTNhZWI1ZTA5ZTFlNiIsIlR5cGUiOiJNaWNyb3NvZnQuR3VpZGVzLlNjaGVtYS5JVGV0aGVyIiwiVHJhbnNmb3JtIjp7IlBvc2l0aW9uIjpbMC4wLDAuMCwwLjBdLCJSb3RhdGlvbiI6WzAuMCwwLjAsMC4wLDAuMF0sIlNjYWxlIjpbMC4wLDAuMCwwLjBdfSwiSXNQbGFjZWRJbldvcmxkIjpmYWxzZSwiRGlzYWJsZUFuaW1hdGlvbiI6ZmFsc2UsIlJlbmRlck1vZGUiOjAsIkFzc2V0SWQiOiIwMDAwMDAwMC0wMDAwLTAwMDAtMDAwMC0wMDAwMDAwMDAwMDAiLCJUZXRoZXJlZEFzc2V0IjoiMDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAwIiwiQXR0YWNoZWRUbyI6MH0sIk1lZGlhIjpbXSwiUGFydFRlbXBsYXRlcyI6W10sIlN0ZXBNb2RlIjowfV19XSwiQWxpZ25tZW50U3RlcCI6eyJJZCI6IjQwYTk5YzkxLTkwMmMtNDlkOS04MmM5LWE1ZmRjMjAzOTBmYSIsIlR5cGUiOiJNaWNyb3NvZnQuR3VpZGVzLlNjaGVtYS5JQWxpZ25tZW50IiwiSW5zdHJ1Y3Rpb25UZXh0IjoiMS4gQWxpZ24g4oCcZGlnaXRhbCBhbmNob3LigJ0gaG9sb2dyYW0gdG8gYSByZWFsIHdvcmxkIG9iamVjdDpcbiAgICAgbyBUYXAgYW5kIGhvbGQgdGhlIGhvbG9ncmFtIHRvIG1vdmVcbiAgICAgbyBUYXAgYW5kIGhvbGQgdGhlIGJsdWUgc3BoZXJlcyB0byByb3RhdGVcblxuMi4gU2VsZWN0IOKAmENvbmZpcm3igJkgd2hlbiB5b3UgYXJlIGRvbmUuIiwiVGV0aGVyIjp7IklkIjoiMzIxMzUxYzEtMWUzMS00NmE0LTg5YWUtOTBmNzk4ZTQ2NDY1IiwiVHlwZSI6Ik1pY3Jvc29mdC5HdWlkZXMuU2NoZW1hLklUZXRoZXIiLCJUcmFuc2Zvcm0iOnsiUG9zaXRpb24iOlswLjAsMC4wLDAuMF0sIlJvdGF0aW9uIjpbMC4wLDAuMCwwLjAsMC4wXSwiU2NhbGUiOlswLjAsMC4wLDAuMF19LCJJc1BsYWNlZEluV29ybGQiOmZhbHNlLCJEaXNhYmxlQW5pbWF0aW9uIjpmYWxzZSwiUmVuZGVyTW9kZSI6MCwiQXNzZXRJZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDAwMDAwMDAwMCIsIlRldGhlcmVkQXNzZXQiOiIwMDAwMDAwMC0wMDAwLTAwMDAtMDAwMC0wMDAwMDAwMDAwMDAiLCJBdHRhY2hlZFRvIjozfSwiTWVkaWEiOltudWxsXSwiRGlnaXRhbFR3aW4iOnsiSWQiOiJjMzE5NjJiOC00YThmLTRlM2ItOWVkNi04ZDBlYTI1MzhmOGQiLCJUeXBlIjoiTWljcm9zb2Z0Lkd1aWRlcy5TY2hlbWEuSU1vZGVsUmVmIiwiQXNzZXRJZCI6IjhkODU2ZmYxLWFiYjMtZTkxMS1hODEyLTAwMGQzYWY0NmI0OSIsIlJlbmRlck1vZGUiOjB9LCJTdGVwTW9kZSI6MSwiQWxpZ25tZW50TW9kZWxUeXBlIjowfSwiQ29tcGxldGlvblN0ZXAiOnsiSWQiOiI0MjQ5MmViMi0zYmIzLTRmNmQtOTU2Zi04YjE3YTljNTgxNmQiLCJUeXBlIjoiTWljcm9zb2Z0Lkd1aWRlcy5TY2hlbWEuSUd1aWRlU3RlcCIsIkluc3RydWN0aW9uVGV4dCI6IkNvbmdyYXR1bGF0aW9ucyEgWW91IHN1Y2Nlc3NmdWxseSBjb21wbGV0ZWQgdGhpcyBndWlkZS4iLCJUZXRoZXIiOnsiSWQiOiI0MzY0MDRhZS05ZTJlLTQ4MzYtYWNmMi1kMjZlMmUzZTU1NzciLCJUeXBlIjoiTWljcm9zb2Z0Lkd1aWRlcy5TY2hlbWEuSVRldGhlciIsIlRyYW5zZm9ybSI6eyJQb3NpdGlvbiI6WzAuMCwwLjAsMC4wXSwiUm90YXRpb24iOlswLjAsMC4wLDAuMCwwLjBdLCJTY2FsZSI6WzAuMCwwLjAsMC4wXX0sIklzUGxhY2VkSW5Xb3JsZCI6ZmFsc2UsIkRpc2FibGVBbmltYXRpb24iOmZhbHNlLCJSZW5kZXJNb2RlIjowLCJBc3NldElkIjoiMDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAwIiwiVGV0aGVyZWRBc3NldCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDAwMDAwMDAwMCIsIkF0dGFjaGVkVG8iOjB9LCJNZWRpYSI6W10sIlBhcnRUZW1wbGF0ZXMiOltdLCJTdGVwTW9kZSI6MH19fQ==
```

Works
```json
{"Schema":"GuidesV3","Guide":{"Id":"14f1b784-87e6-4ec8-a966-9828ca0983f8","Type":"Microsoft.Guides.Schema.IGuide","Name":"Just Steps Text Guide","Tasks":[{"Id":"a0cc74cc-1713-4ae8-ba8b-508bba1f9c46","Type":"Microsoft.Guides.Schema.IGuideTask","Name":"Task name","Steps":[{"Id":"879b78f1-ebad-46ad-82f1-eb6363a3a817","Type":"Microsoft.Guides.Schema.IGuideStep","InstructionText":"This is step 1 of all my tasks","Tether":{"Id":"3fef234d-36b9-41d7-b6ce-3aeb5e09e1e6","Type":"Microsoft.Guides.Schema.ITether","Transform":{"Position":[0.0,0.0,0.0],"Rotation":[0.0,0.0,0.0,0.0],"Scale":[0.0,0.0,0.0]},"IsPlacedInWorld":false,"DisableAnimation":false,"RenderMode":0,"AssetId":"00000000-0000-0000-0000-000000000000","TetheredAsset":"00000000-0000-0000-0000-000000000000","AttachedTo":0},"Media":[],"PartTemplates":[],"StepMode":0}]}],"AlignmentStep":{"Id":"40a99c91-902c-49d9-82c9-a5fdc20390fa","Type":"Microsoft.Guides.Schema.IAlignment","InstructionText":"1. Align \"digital anchor\" hologram to a real world object:\n     o Tap and hold the hologram to move\n     o Tap and hold the blue spheres to rotate\n\n2. Select \"Confirm\" when you are done.","Tether":{"Id":"321351c1-1e31-46a4-89ae-90f798e46465","Type":"Microsoft.Guides.Schema.ITether","Transform":{"Position":[0.0,0.0,0.0],"Rotation":[0.0,0.0,0.0,0.0],"Scale":[0.0,0.0,0.0]},"IsPlacedInWorld":false,"DisableAnimation":false,"RenderMode":0,"AssetId":"00000000-0000-0000-0000-000000000000","TetheredAsset":"00000000-0000-0000-0000-000000000000","AttachedTo":3},"Media":[null],"DigitalTwin":{"Id":"c31962b8-4a8f-4e3b-9ed6-8d0ea2538f8d","Type":"Microsoft.Guides.Schema.IModelRef","AssetId":"8d856ff1-abb3-e911-a812-000d3af46b49","RenderMode":0},"StepMode":1,"AlignmentModelType":0},"CompletionStep":{"Id":"42492eb2-3bb3-4f6d-956f-8b17a9c5816d","Type":"Microsoft.Guides.Schema.IGuideStep","InstructionText":"Congratulations! You ARE REALLY CUSTOM successfully completed this guide.","Tether":{"Id":"436404ae-9e2e-4836-acf2-d26e2e3e5577","Type":"Microsoft.Guides.Schema.ITether","Transform":{"Position":[0.0,0.0,0.0],"Rotation":[0.0,0.0,0.0,0.0],"Scale":[0.0,0.0,0.0]},"IsPlacedInWorld":false,"DisableAnimation":false,"RenderMode":0,"AssetId":"00000000-0000-0000-0000-000000000000","TetheredAsset":"00000000-0000-0000-0000-000000000000","AttachedTo":0},"Media":[],"PartTemplates":[],"StepMode":0}}}
```

```json
{"Schema":"GuidesV3","Guide":{"Id":"14f1b784-87e6-4ec8-a966-9828ca0983f8","Type":"Microsoft.Guides.Schema.IGuide","Name":"JustStepsTextGuide","Tasks":[{"Id":"a0cc74cc-1713-4ae8-ba8b-508bba1f9c46","Type":"Microsoft.Guides.Schema.IGuideTask","Name":"Taskname","Steps":[{"Id":"879b78f1-ebad-46ad-82f1-eb6363a3a817","Type":"Microsoft.Guides.Schema.IGuideStep","InstructionText":"Thisisstep1ofallmytasks","Tether":{"Id":"3fef234d-36b9-41d7-b6ce-3aeb5e09e1e6","Type":"Microsoft.Guides.Schema.ITether","Transform":{"Position":[0,0,0],"Rotation":[0,0,0,0],"Scale":[0,0,0]},"IsPlacedInWorld":false,"DisableAnimation":false,"RenderMode":0,"AssetId":"00000000-0000-0000-0000-000000000000","TetheredAsset":"00000000-0000-0000-0000-000000000000","AttachedTo":0},"Media":[],"PartTemplates":[],"StepMode":0}]}],"AlignmentStep":{"Id":"40a99c91-902c-49d9-82c9-a5fdc20390fa","Type":"Microsoft.Guides.Schema.IAlignment","InstructionText":"1.Align\"digitalanchor\"hologramtoarealworldobject:\noTapandholdthehologramtomove\noTapandholdthebluespherestorotate\n\n2.Select\"Confirm\"whenyouaredone.","Tether":{"Id":"321351c1-1e31-46a4-89ae-90f798e46465","Type":"Microsoft.Guides.Schema.ITether","Transform":{"Position":[0,0,0],"Rotation":[0,0,0,0],"Scale":[0,0,0]},"IsPlacedInWorld":false,"DisableAnimation":false,"RenderMode":0,"AssetId":"00000000-0000-0000-0000-000000000000","TetheredAsset":"00000000-0000-0000-0000-000000000000","AttachedTo":3},"Media":[null],"DigitalTwin":{"Id":"c31962b8-4a8f-4e3b-9ed6-8d0ea2538f8d","Type":"Microsoft.Guides.Schema.IModelRef","AssetId":"8d856ff1-abb3-e911-a812-000d3af46b49","RenderMode":0},"StepMode":1,"AlignmentModelType":0},"CompletionStep":{"Id":"42492eb2-3bb3-4f6d-956f-8b17a9c5816d","Type":"Microsoft.Guides.Schema.IGuideStep","InstructionText":"Congratulations!YouAREREALLYCUSTOMsuccessfullycompletedthisguide.","Tether":{"Id":"436404ae-9e2e-4836-acf2-d26e2e3e5577","Type":"Microsoft.Guides.Schema.ITether","Transform":{"Position":[0,0,0],"Rotation":[0,0,0,0],"Scale":[0,0,0]},"IsPlacedInWorld":false,"DisableAnimation":false,"RenderMode":0,"AssetId":"00000000-0000-0000-0000-000000000000","TetheredAsset":"00000000-0000-0000-0000-000000000000","AttachedTo":0},"Media":[],"PartTemplates":[],"StepMode":0}}}
```

# Guides Generator 

A helper to generate Guides from a URL.

## Setup

Open a terminal as an admin.

Setup python3 virtual env or source an existing on your os.
```python
sudo apt-get update
pip install virtualenv
python3 -m venv linux 
source env/linux/bin/activate 
```

```python
pip install virtualenv
python -m venv .win
env\.win\Scripts\activate.bat
```

Pull dependencies.
```bash
pip install -r requirements.txt
python __main__.py
```

Give me a url.

## Status

Unit test needed...
