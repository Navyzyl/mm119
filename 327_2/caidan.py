import random
names = []
passwords = []
cards = []
denglu_name = None
denglu_card = None
while True:
    print('*************************************')
    a_1 = input('请输入你想你的操作数：1注册 2登录 3抽奖 0退出')
    if a_1 == '1':
        print('***************注册会员***************')
        while True:
            name = input('注册会员名：')
            if name.strip() == '':
                print('用户名不能为空')
            else:
                if name in names:
                    print('用户名已存在')
                else:
                    break
        while True:
            password = input('设置密码：')
            if password.strip() == '':
                print('密码不能为空')
            else:
                break
        names.append(name)
        passwords.append(password)
        if len(cards) == 8999:
            print('用户卡号已满，程序退出')
            exit()
        while True:
            card = random.randint(1000, 9999)
            if card not in cards:
                break
        cards.append(card)
        print(f'会员名{name}密码{password}会员卡号{card}')
    elif a_1 == '2':

            print('*************登录*************')
            name = input('请输入会员名：')
            password = input('请输入密码：')
            for i in range(0, len(names)):
                if names[i] == name and passwords[i] == password:
                    denglu_name = name
                    denglu_card = str(cards[i])
                    print(f'登陆成功，欢迎{denglu_name}')
                    break
            if denglu_name is None:
                print('登陆失败')
    elif a_1 == '3':
        rum_num = random.randint(0, 9)
        print('****************抽奖**************')
        if denglu_name is not None and denglu_card is not None:
            print(f'{denglu_name}你的卡号为{denglu_card}')
            if str(rum_num) == denglu_card[-1]:
                print(f'恭喜您获奖，本次中奖数字为{rum_num}')
            else:
                print(f'很遗憾，你没中奖，本次中奖数字为{rum_num}')
        else:
            print('需登陆账号进行抽奖')
    elif a_1 == '0':
        break
    else:
        print('请输入正确的操作数')

