import json
info = {
    'name':'sivan',
    'age':25

}


f = open('test.txt','w+')
f.write(json.dumps(info))

f.close()

print()