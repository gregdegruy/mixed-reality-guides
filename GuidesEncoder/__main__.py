from dynamicsmsmrw import AzureAuth
from dynamicsmsmrw import MSMRWGuide

if __name__ == "__main__":
    # azureAuth = AzureAuth()

    guide = MSMRWGuide("Guide")
    guide.createGuideFile()    
    guide.encodeGuideFile() 
