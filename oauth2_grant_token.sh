CLIENT_ID=<:)> \
CLIENT_SECRET=<:(> \
REDIRECT_URI=http%3A%2F%2Fcallbackurl \
RESOURCE=https%3A%2F%2Fmsott.api.crm.dynamics.com%2F \
TENANT=grdegr.onmicrosoft.com

curl -X POST https://login.microsoftonline.com/${TENANT}/oauth2/token \
-H "cache-control: no-cache" \
-H "content-type: multipart/form-data" \
-F "client_id=${CLIENT_ID}" \
-F "client_secret=${CLIENT_SECRET}" \
-F "grant_type=client_credentials" \
-F "resource=${RESOURCE}"

curl -X POST https://login.microsoftonline.com/${TENANT}/oauth2/authorize?client_id=${CLIENT_ID}&response_type=code&redirect_uri=${REDIRECT_URI}&response_mode=query&resource=${RESOURCE}&state=12345


https://login.microsoftonline.com/grdegr.onmicrosoft.com/oauth2/authorize?client_id=0960be47-c441-4a8b-96e1-16f97487ff35&response_type=code&redirect_uri=https%3A%2F%2Fcallbackurl&response_mode=query&resource=https%3A%2F%2Fmsott.api.crm.dynamics.com%2F&state=12345

# get's code that can be used to request a JWT for use as a Beaer token in OAuth 2.0 authorization for API calls 