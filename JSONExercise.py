import requests
import json

#Make API call from ISS
r = requests.get('http://api.open-notify.org/astros.json')

#Convert output from API call to string
resp = str(r.text)

#Convert previous string to JSON obj (dict) and focusing on key 'people'
ppl = json.loads(resp)['people']

#Topic header
print 'No  Craft  Name'

#Run each sequence in list of value referred to key 'people'
for x in range (len(ppl)):
    print (int(x)+1),' ',ppl[x]['craft'],'  ',ppl[x]['name']
