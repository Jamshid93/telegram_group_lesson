import json 
f=open("result.json").read()
data=json.loads(f)
# print(data['name'])
messag=data['messages']
for i in messag:
    print(i['id'])
