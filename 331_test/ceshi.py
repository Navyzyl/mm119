wek=['MON','TUE','WED','THU','FRI','SAT','SUN']
while True:
    choice=int(input('请输入数字1-7（输入0结束）：'))
    if choice==0:
        break
    elif 1<=choice<=7:
        print(f'{wek[choice-1]}')
    else:
        print('请输入正确的数字')