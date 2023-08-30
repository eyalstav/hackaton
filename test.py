import geocoder
import requests
import json
g = geocoder.ip('me')
lat, lon = g.latlng

data = {"eyal44hdfasdfd321": {"description": "fasdfasd", "location": {"lat": lat, "lon": lon}}}
print(data)
res = requests.patch("https://communityconnect1234-default-rtdb.europe-west1.firebasedatabase.app/Help.json", json.dumps(data))
print(res.content)