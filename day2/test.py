#author: sivan
#coding:utf8

def consumer(name):
    print('%s 准备吃包子啦！'%name)
    items = yield
    print('%s 包子来了， 被%s吃了'%(items,name))
c =consumer('sivan')
c.__next__()
c.send('牛肉馅')