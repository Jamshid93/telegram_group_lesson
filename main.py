import json 
f=open("result.json").read()
data=json.loads(f)
# print(data['name'])
messag=data['messages']
count=0
for i in messag:
    if i['type']=='message':
        count+=1
print(count)
 