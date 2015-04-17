import urllib.request
import json
 
def search(texto):
  url = 'http://graph.facebook.com/search?q='
  tail = '&type=post&access_token=CAACEdEose0cBAAX2J5NqCSJZCd5nct0YZCEFVmlJLKZB1u1C6mggiEHrRjuBcHQw0aBMutxtMtHm5J2fHX2POhog5GZCJTOLxpkfgOp5UBVDe4bga4mpE0NbegqFMhZBcSzO3czgVUTcewUoZCaUAZBwU1ZAhn3VHdnjpDHKAR0ioGGXy61BtGcrg0AW5KT9NJwZD'
  resp = urllib.request.urlopen(url+texto+tail).read()
  data = json.loads(resp.decode('utf-8'))
  return data['data']
 
for resp in search('CPRecife2'):
  if 'message' in resp:
    print (resp['from']['name'] + ': ' + resp['message'] + '\n')
