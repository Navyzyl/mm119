def xinjian():
    new = input('新建联系人姓名：')
    member.append(new)
    newtel = input('新建联系人电话：')
    tel.append(newtel)
    print('输入完成。')
    return
def chakan():
    print(f'-------通讯录-------')
    print(f'姓名         电话')
    for i in range(0, len(member)):
        print(f'{member[i]}    {tel[i]}')
    print('-------------------')
    return
def xiugai():
    replacer = input('请输入要修改联系人的姓名：')
    modifier = None
    for re in range(0, len(member)):
        if member[re] == replacer:
            tel[re] = input('请输入新修改电话：')
            modifier = re
            break
    if modifier is not None:
        print('修改完成。')
    else:
        print('通讯录内不存在此人')
        return
def shanchu():
    dele = input('请输入要删除联系人的姓名：')
    modifier = None
    for de in range(0, len(member)):
        if member[de] == dele:
            member.pop(de)
            tel.pop(de)
            modifier = de
            break
    if modifier is not None:
        print('删除成功。')
    else:
        print('通讯录内不存在此人')
member = ['aaa', 'bbb']
tel = ['111', '222']
while True:
    caozuo = input('请选择你的操作：1新建联系人 2查看联系人 3修改联系人 4删除联系人 0退出：')
    if caozuo == '1':
        xinjian()
    elif caozuo == '2':
        chakan()
    elif caozuo == '3':
        xiugai()
    elif caozuo == '4':
        shanchu()
    elif caozuo == '0':
        print('您已退出通讯录。')
        break
    else:
        print('输入错误，请重新输入。')
