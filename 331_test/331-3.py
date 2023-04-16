num=[]
for i in range(0,5):
    while True:
        a=input('请输入一个数字：')
        if a.isdigit()==True:
            break
    a=int(a)
    num.append(a)
print(f'五个数中最小值为{min(num)}')
