while True:
    shuchu=[]
    num=input('请输入一个整数:')
    if num.isdigit()==True:
        l=len(num)
        for i in range(0,l):
            if num[l-i-1]!='0':
                a=l-i-1
                break
            i=i+1
        for j in range(0,a+1):
            shuchu.append(num[a-j])
            j=j+1
        shuchu_1=''.join(shuchu)
        print(f'{shuchu_1}')
    else:
        print('请输入数字')
            