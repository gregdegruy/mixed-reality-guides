# Guides Generator 

An API to create Dynamics 365 Guides using Python.

## Setup

Open a terminal as an admin.

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

Application permissions for Graph do NOT require interactve auth from user
https://github.com/Azure-Samples/ms-identity-python-daemon/tree/master/1-Call-MsGraph-WithSecret

Delegated permissions for CRM required interactve auth from user, requires get code from the BIG endpoint
https://github.com/AzureAD/azure-activedirectory-library-for-python/blob/dev/sample/website_sample.py#L104

the BIG endpoint

https://login.microsoftonline.com/grdegr.onmicrosoft.com/oauth2/authorize?client_id=0960be47-c441-4a8b-96e1-16f97487ff35&response_type=code&redirect_uri=https%3A%2F%2Fcallbackurl&response_mode=query&resource=https%3A%2F%2Fmsott.api.crm.dynamics.com%2F&state=12345

From [Request an authorization code](Request an authorization code)

```sh
https://login.microsoftonline.com/{tenant}/oauth2/authorize?
client_id=6731de76-14a6-49ae-97bc-6eba6914391e
&response_type=code
&redirect_uri=http%3A%2F%2Flocalhost%3A12345
&response_mode=query
&resource=https%3A%2F%2Fservice.contoso.com%2F
&state=12345
```