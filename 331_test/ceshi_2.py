a=input('请输入一个整数')
b=int(a)
l=len(a)
print(b,l)
for i in range(0, l):
    if a[l - i - 1] != '0':
        c= 1 - i - 1
        print(c)
    i=i+1
