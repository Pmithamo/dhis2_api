import json
import base64

import requests


url = "http://192.168.1.100:8080/training/api/"
# cred = 

# Encode credentials to Base64 encoding format

credentials = base64.b64encode("mnjatha:Mnjatha123#".encode("utf-8"))

# make the request

req = requests.get(
    url + 'organisationUnits',
    headers = {
        'Authorization' : 'Basic ' + str(credentials),
        'Accept' : 'application/json',
        'Content-Type' : 'application/json'
    },
    params = {
        'paging' : 'false',
        'fields' : '[*]'
    }

)


# print ([x for x in dir(req) if not x.startswith('_')])
print (req)



