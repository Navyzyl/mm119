a_1 = str(input('请输入一个整数：'))
l=len(a_1)
print(f'长度为{l}')
for i in range(0,l):
    print(f'{a_1[l-1-i]}',end='')
    i =+1