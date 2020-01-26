import base64
import json

with open('C:\\Users\\grego\\Documents\\GitHub\\greg\\guides-entity-temp\\GuidesEncoder\\works.json', encoding="utf8") as jsonfile:
    data = json.load(jsonfile)
    datastr = json.dumps(data)
    encoded = base64.b64encode(datastr.encode('utf-8'))
    print("done")
