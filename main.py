import json 
f=open("result.json").read()
data=json.loads(f)
# print(data['name'])
messag=data['messages']
count_users=0
user=[]
for i in messag:
    if i['type']=='message':
        if user.count(i['from'])==0:
            count_users+=1
        user.append(i['from'])
print(count_users)

 