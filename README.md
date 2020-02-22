# Guides Generator 

An API to create Dynamics 365 Guides using Python.

## Required 

1. [HoloLens Emulator](https://docs.microsoft.com/en-us/windows/mixed-reality/using-the-hololens-emulator)
2. [Microsoft Guides App](https://www.microsoft.com/en-us/p/microsoft-dynamics-365-guides/9n038fb42kkb)
3. [Dynamics 365 Trial](https://trials.dynamics.com/) this blog has the [steps](https://community.dynamics.com/crm/b/magnetismsolutionscrmblog/posts/how-to-get-30-day-trial-of-microsoft-dynamics-365-for-free).
4. [Microsoft Guides License](https://docs.microsoft.com/en-us/office365/admin/manage/assign-licenses-to-users?view=o365-worldwide)
5. [Register an application in Azure AD](https://docs.microsoft.com/en-us/skype-sdk/ucwa/registeringyourapplicationinazuread)

## Environment

Setup python3 virtual env or source an existing on your os.

Linux
```python
sudo apt-get update
pip install virtualenv
python3 -m venv linux 
source env/linux/bin/activate 
```

Windows
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

Security and Compliance. Authenticate to get token and authorization to verify your permissions using [MSAL](https://github.com/Azure-Samples/ms-identity-python-webapp).

For MSAL the main auth endpoint is. `https://login.microsoftonline.com/grdegr.onmicrosoft.com/oauth2/authorize?client_id=0960be47-c441-4a8b-96e1-16f97487ff35&response_type=code&redirect_uri=https%3A%2F%2Fcallbackurl&response_mode=query&resource=https%3A%2F%2Fmsott.api.crm.dynamics.com%2F&state=12345`.

```sh
https://login.microsoftonline.com/TENANT/oauth2/authorize?
client_id=CLIENT_ID
&response_type=code
&redirect_uri=http%3A%2F%2Flocalhost%3A12345
&response_mode=query
&resource=https%3A%2F%DYNAMICS_CDS_ORD.api.crm.dynamics.com%2F
&state=12345
```

You can verify scope and authority using [jwt](https://jwt.ms/).