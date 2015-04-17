import urllib.request
import json

url = "http://graph.facebook.com/me/friends"
resp = urllib.request.urlopen(url).read()
data = json.loads(resp.decode('utf-8'))
for amigo in data['data']:
	print (amigo['name'])
