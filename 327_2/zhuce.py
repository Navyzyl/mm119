import random
names=[]
passwords=[]
cards=[]

print('***************注册会员***************')
while True:
    name=input('注册会员名：')
    if name.strip()=='':
        print('用户名不能为空')
    else:
        if name in names:
            print('用户名已存在')
        else:
            break
while True:
    password=input('设置密码：')
    if password.strip()=='':
        print('密码不能为空')
    else:
        break
names.append(name)
passwords.append(password)
if len(cards)==8999:
    print('用户卡号已满，程序退出')
    exit()
while True:
    card=random.randint(1000,9999)
    if card not in cards:
        break
cards.append(card)
print(f'会员名{name}密码{password}会员卡号{card}')