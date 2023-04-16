class Car():
    def __init__(self,carname='运输'):
        self.carname_1=carname
    def jieshao(self):
        print(f'这辆车的用途为：{self.carname_1}')

class Home_Car(Car):
    pass
car_1=Home_Car()
car_2=Home_Car('玩')
car_1.jieshao()
car_2.jieshao()