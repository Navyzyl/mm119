name_1=[]#新建姓名列表
tel_1=[]#新建电话列表
while True:
    choice=input('请选择你的操作：1新建联系人 2查看联系人 3修改联系人 4删除联系人 0推出：')#打印操作菜单
    name_2=len(name_1)#测量姓名列表长度
    tel_2=len(tel_1)#测量电话列表长度
    if choice =='1':#如果输入操作数为1
        name_3=input('新建联系人姓名：')#输入新建联系人名字
        tel_3=input('新建联系人电话：')#输入新建联系人号码
        name_1.append(name_3)#加入姓名列表最后一位
        tel_1.append(tel_3)#加入电话列表最后一位
    elif choice=='2':#如果操作数为2
        print('--------通讯录--------')#打印通讯录
        print(' 姓名\t\t\t电话')
        for i,j in zip(name_1,tel_1):#通过i，j对两个列表进行遍历
            print(i,'\t',j)#打印姓名和电话
            print('---------------------')
    elif choice=='3':#如果操作数为3
        name_4=input('请输入修改联系人姓名：')#输入你想修改的联系人姓名
        name_index=None#设置一个不在列表索引数的数
        for i in range(0,name_2):
            if name_1[i]==name_4:
                name_index=i
                break#对姓名列表进行遍历，如果找到目标，退出循环，并将设置的name_index变为目标值的索引数
        if name_index is not None:
            tel_1[name_index]=input('请输入新的电话号码：')#若name_index不是None意味着输入姓名在列表内，可通过修改他的手机号
            print(f'成功修改{name_4}的电话号码')#通过显示表明修改成功
        else:
            print(f'没有找到{name_4}的员工记录')#若name_index等于None，则输入姓名不在列表内，不可修改
    elif choice=='4':#如果操作数为4
        name_5 = input('请输入删除联系人姓名：')#输入想删除的联系人名字
        name_index1 = None#设置一个不在列表索引数的数
        for i in range(0, name_2):
            if name_1[i] == name_5:
                name_index1 = i
                break#对姓名列表进行遍历，如果找到目标，退出循环，并将设置的name_index变为目标值的索引数
        if name_index1 is not None:
            del name_1[name_index1]
            del tel_1[name_index1]#若name_index不是None意味着输入姓名在列表内，可删除他的姓名和电话
            print(f'成功删除联系人{name_5}')#通过显示表明删除成功
        else:
                print(f'没有找到{name_5}的员工记录')#若name_index等于None，则输入姓名不在列表内，不可删除
    elif choice=='0':#若操作数是0，则退出循环，程序结束
        print('程序结束')
        break
    else:#若输入的操作数不是0.1.2.3.4，则通过显示提示重新输入操作数
        print('请输入正确的操作选项')






