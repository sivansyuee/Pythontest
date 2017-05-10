#author: sivan
#coding:utf8

data = {
   '上海分公司': {
       '运作部': {
           '客服部':['小戴','小王'],
           '储运部':['小罗','小马']
       },
       '财务部': {},
       '业务部': {},
       '行政部': {}
   },
    '哈尔滨分公司': {
        '财务部': {},
        '运作部': {},
        '业务部': {},
        '行政部': {}
    },
    '长春分公司': {
        '财务部': {},
        '运作部': {},
        '业务部': {},
        '行政部': {}
    },
    '沈阳分公司': {
        '财务部': {},
        '运作部': {},
        '业务部': {},
        '行政部': {}
    }
}

_quit = False


while not _quit:
    for branch in data:
        print(branch)
    select_next = input('--->')
    if select_next in data:
        while not _quit:
            for breach2 in data[select_next]:
                print(breach2)
            select_next2 = input('--->')
            if select_next2 in data[select_next]:
                while not _quit:
                    for breach3 in data[select_next][select_next2]:
                        print(breach3)
                    select_next3 = input('--->')
                    if select_next3 in data[select_next][select_next2]:
                        while not _quit:
                            for breach4 in data[select_next][select_next2][select_next3]:
                                print(breach4)
                            select_next4 = input('-->')
                            if select_next4 == 'b':
                                break
                            elif select_next4 == 'q':
                                _quit = True
                    elif select_next3 == 'b':
                        break
                    elif select_next3 == 'q':
                        _quit = True
            elif select_next2 == 'b':
                break
            elif select_next2 == 'q':
                _quit = True
    elif select_next == 'b':
        break
    elif select_next == 'q':
        _quit = True