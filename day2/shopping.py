# #author: sivan
# #coding:utf8
#
commodity =[('IPhone',3000),
            ('Mac Pro', 12000),
            ('Starbuck Latte',31),
            ('book',50)]


user = {"username":'sivan','balance': 5000}

shopp_user = {}
salary = input('please input salary:')
if salary.isdigit():
    salary = int(salary)
    while True:
        for index, value in enumerate(commodity):
            print(index+1,value)
        select_number = input('-->')
        if select_number.isdigit():
            select_number = int(select_number)
            if select_number < len(commodity):
                if salary > commodity[select_number-1][1]:
                    salary -= commodity[select_number-1][1]
                    print('%s ----%s'%(salary,commodity[select_number-1]))
                else:
                    print('余额不足')
                    print('%s ----余额%s' % (commodity[select_number - 1],salary))
                    break

#
# elif salary=='q':
#     print('exit()')
#
# # salaryold = salary
# # while True:
# #     shopping = []
# #
# #    # shopping.append()
# #     for i in commodity:
# #         print(i)
# #     serial_number= input('enter the serial number you want to buy goods ')
# #
# #     if 'q' == serial_number:
# #        print('You have to buy business {shopp} spend {money} money ,balance {balance}'.format(shopp=shopping, money=salaryold-salary,balance=salary))
# #        break
# #     else:
# #         if commodity[int(serial_number) - 1]:
# #             if salary > commodity[int(serial_number) - 1][1]:
# #                 salary -= commodity[int(serial_number) - 1][1]
# #                 shopping.append(commodity[int(serial_number) - 1])
# #
# #             continue
# #         else:
# #             print('This at not there')
# #             continue
# #
