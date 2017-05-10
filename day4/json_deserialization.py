import json
f = open('test.txt','r')
data = json.loads(f.read())
f.close()
print(type(data))
