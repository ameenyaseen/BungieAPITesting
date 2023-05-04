import json
import urllib3 as url
with open("tokens.json", 'r') as f:
    tokens = json.load(f)

print(tokens)

resp = url.request('GET', 'http://www.bungie.net/Platform/Destiny2//Destiny2/Manifest/', headers={'X-API-Key': tokens['APIKey']})

data = resp.data.decode('utf-8')

data_dict = json.loads(data)

print(f'')
