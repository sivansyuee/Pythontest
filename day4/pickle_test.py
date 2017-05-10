import pickle
def sayhi(name):
    print('hello,',name)

info = {
    'name':'sivan',
    'age':25,
    'func':sayhi
}



f = open('text1.txt','wb')
f.write(pickle.dumps(info))
