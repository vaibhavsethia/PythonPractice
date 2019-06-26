import simplejson as json
import requests

url="https://googleapis.com/urlshortner/v1/url"
payload = {"longurl":"http://example.com"}
headers={"Content-Type":"application/json"}
r=requests.post(url,json=payload,header=headers)

print(json.loads(r.text)["error"]["code"])