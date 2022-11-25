import json 
f=open("result.json").read()
data=json.loads(f)
print(data['name'])