import requests
import json

a = {"type":"book", "id":3}
b = '{"type":"book", "id":3}'

#dumps => dict -> str
c = json.dumps(a)

#loads => str -> dict
d = json.loads(b)

print d['type']
