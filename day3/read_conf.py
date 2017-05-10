#获取数据
def output(dirname):
    data = {}
    with open(dirname, 'r') as f:
        for i in f:
            if not i[0].isspace(): #如果首字母不为空则作为字典的键
                j = i
                # j = i.rstrip('\n')
                data[j] = []
            else:
                # i = i.rstrip('\n')
                data[j].append(i) #向列表里面添加值
    return data



#查询函数
def search(search_str):
    data = output('new.txt')
    for i in data.keys():
        if i.find(search_str) != -1:
            print(data[i])
            break


#修改函数

def revamp(search_str,info):
    data = output('new.txt')
    data[search_str].append(info)
    sttr1 = ''
    with open('new1.txt', 'w+') as f:

        for i in data.keys():
            sttr1 += i
            for j in data[i]:
                sttr1 += j
        f.write(sttr1)

search_str = 'backend  www.syuee.com\n'
info = '        server 100.1.7.8 100.1.7.8 weight 20 maxconn 3000\n'
#search(search_str)
revamp(search_str,info)