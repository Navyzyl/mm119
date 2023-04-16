mon_1 = int(input('请输入您出行的月份：1~12:'))
level_1 = int(input('请问你选择头等舱还是经济舱？头等舱输入1，经济舱输入2:'))
price_1 = 5000
if 1<=mon_1<=12:
    if 4 <= mon_1 <= 10:
        if level_1==1:
            price_1=price_1*0.9
        elif level_1==2:
            price_1=price_1*0.6
        else:
            print('请输入正确数字')
    else:
        if level_1==1:
            price_1=price_1*0.5
        elif level_1==2:
            price_1=price_1*0.4
        else:
            print('请输入正确数字')
    print(f'您的机票价格为：{price_1}')
else:
    print('请输入正确月份')



