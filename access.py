import requests
import json

def getAcessToken():
    import requests
    

    api_key = 'SGimukQbbBoek5FalhrFahJg'
    secret_key = 'TBdywXIzEA2LFYgSdluVG8uKqlgBa6CL'
    token_url = 'https://aip.baidubce.com/oauth/2.0/token'
    url = f"{token_url}?grant_type=client_credentials&client_id={api_key}&client_secret={secret_key}"

    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return json.loads(response.text)['access_token']

accessToken = getAcessToken()