import pickle

def sayhi(name):
    print('hello, ', name)

f = open('text1.txt','rb')
data = pickle.loads(f.read())

print(data['func']('fsdf'))