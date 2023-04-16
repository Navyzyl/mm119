names=['aaa','bbb','ccc']
mima=['111','2221','333']
while True:
    l=len(names)
    for i in range(0,l):
        name=input('请输入用户名：')
        m_1=input('请输入密码：')
        if name==names[i]and m_1==mima[i]:
            print('欢迎登录MyShopping系统！')
            break
        else:
            print(f'输入错误，您还有{3-i-1}次机会')
    break