class Prise():
    def __init__(self,n,a):
        self.name=n
        self.age=a


    def prices(self):
        self.age=int(self.age)
        if 18 <= self.age <60:
            print(f'{self.name}年龄为{self.age}为全价票')
        elif 6 <= self.age < 18:
            print(f'{self.name}年龄为{self.age}为半价票')
        else:
            print(f'{self.name}年龄为{self.age}免费')
while True:

    name=input('你的姓名为：')
    age=input('你的年龄为：')
    if age.isdigit()==True:
        a=Prise(name,age)
        a.prices()
    else:
        print('输入有误')
        break