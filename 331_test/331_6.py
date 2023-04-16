name_1=[]
tel_1=[]
while True:
    choice=input('请选择你的操作：1新建联系人 2查看联系人 3修改联系人 4删除联系人 0推出：')
    name_2=len(name_1)
    tel_2=len(tel_1)
    if choice =='1':
        name_3=input('新建联系人姓名：')
        tel_3=input('新建联系人电话：')
        name_1.append(name_3)
        tel_1.append(tel_3)
    elif choice=='2':
        print('--------通讯录--------')
        print(' 姓名\t\t\t电话')
        for i,j in zip(name_1,tel_1):
            print(i,'\t',j)
            print('---------------------')
    elif choice=='3':
        name_4=input('请输入修改联系人姓名：')
        name_index=None
        for i in range(0,name_2):
            if name_1[i]==name_4:
                name_index=i
                break
        if name_index is not None:
            tel_1[name_index]=input('请输入新的电话号码：')
            print(f'成功修改{name_4}的电话号码')
        else:
            print(f'没有找到{name_4}的员工记录')
    elif choice=='4':
        name_5 = input('请输入删除联系人姓名：')
        name_index1 = None
        for i in range(0, name_2):
            if name_1[i] == name_5:
                name_index1 = i
                break
        if name_index1 is not None:
            del name_1[name_index1]
            del tel_1[name_index1]
            print(f'成功删除联系人{name_5}')
        else:
                print(f'没有找到{name_5}的员工记录')
    elif choice=='0':
        print('程序结束')
        break
    else:
        print('请输入正确的操作选项')