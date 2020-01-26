import base64
import json
import os

from classes import AzureAuth

if __name__ == "__main__":
    with open(os.getcwd() + "\\GuidesEncoder\\steps\\in.json", encoding="utf8") as jsonfile:
        data = json.load(jsonfile)
        datastr = json.dumps(data)
        encoded = base64.b64encode(datastr.encode("utf-8"))
        print("done")

    azureAuth = AzureAuth("", "")

    sampleDiagnosis = "https://beta.revtwo.com/session/L9X26twMg3cRTBnvmPkq4KVJbWNCHj?navcode=5cGZd3fFhz"
    domStepClass = "stepbox-frame"
