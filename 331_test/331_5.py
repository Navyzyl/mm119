import random
while True:
    red=[]
    choice=input('是否生成随机双色球号码（Y/N）')
    if choice=='Y':
        while len(red)<=5:
            a=random.randint(1,33)
            if a not in red:
                red.append(a)
        for i in range(0,len(red)-1):
            for j in range(0,len(red)-1):
                if red[j]>red[j+1]:
                    red[j],red[j+1]=red[j+1],red[j]
        b_1=random.randint(1,16)
        print('红球',red)
        print('蓝球',b_1)
    elif choice=='N':
        break
    else:
        print('请输入正确的操作数')


