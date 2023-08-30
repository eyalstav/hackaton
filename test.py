import geocoder
import requests
import json
g = geocoder.ip('me')
lat, lon = g.latlng

data = {'eyal4432iuyiu': {"description": "des_input.text", "location": {"lat": lat, "lon": lon}}}
# data = {"eyal44hdfasdfd321": {"description": "fasdfasd", "location": {"lat": lat, "lon": lon}}}
print(data)
res = requests.patch("https://communityconnect1234-default-rtdb.europe-west1.firebasedatabase.app/Help.json",
                     json.dumps(data))
print(res.content)



# import geocoder
#
# g = geocoder.ip('me')
# lat, lon = g.latlng
#
# data = {"eyal44hdfasdfd321": {"description": "fasdfasd", "location": {"lat": lat, "lon": lon}}}
# print(data)
# res = requests.patch("https://communityconnect1234-default-rtdb.europe-west1.firebasedatabase.app/Help.json", json.dumps(data))
# print(res.content)