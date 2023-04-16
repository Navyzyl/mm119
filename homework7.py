l=int(input('请输入杨辉三角阶数：'))
sanjiao=[[1],[1,1]]
for i in range(2,l):
    sanjiao_1=sanjiao[i-1]
    sanjiao_2=[1]
    for j in range(0,i-1):
        sanjiao_2.append(sanjiao_1[j]+sanjiao_1[j+1])
    sanjiao_2.append(1)
    sanjiao.append(sanjiao_2)
print(sanjiao)
for i in range(0,l):
    print(sanjiao[i])
print(sanjiao[8][6])

