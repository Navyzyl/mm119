class Jiaoche():
    def prices(self):
        self.price=500

class Keche():
    def prices(self):
        self.price=1000

class benchi():
    def beishu(self):
        self.b=1.5

class baoma():
    def beishu(self):
        self.b=1

class bieke():
    def beishu(self):
        self.b=0.5
prices=0
beishu=0
while True:
    print('---------小课汽车租赁系统--------')
    choice_1=input('请选择车型：1轿车，2客车，0退出')
    if choice_1=='1':
        prices=Jiaoche()
        prices.prices()

        choice_2=input('请选择皮牌：1奔驰，2宝马，3别克')
        if choice_2=='1':
            beishu=benchi()
            beishu.beishu()
        elif choice_2=='2':
            beishu=baoma()
            beishu.beishu()
        elif choice_2=='3':
            beishu=bieke()
            beishu.beishu()
        else:
            print('请输入正确的品牌数')
    elif choice_1=='2':
        prices = Keche()
        prices.prices()
        choice_2 = input('请选择皮牌：1奔驰，2宝马，3别克')
        if choice_2 == '1':
            beishu = benchi()
            beishu.beishu()
        elif choice_2 == '2':
            beishu = baoma()
            beishu.beishu()
        elif choice_2 == '3':
            beishu = bieke()
            beishu.beishu()
        else:
            print('请输入正确的品牌数')
    elif choice_1=='0':
        print('感谢使用，下次再见')
        break
    else:
        print('请输入正确的操作数')
    days=int(input('输入租赁天数：'))
    prices=prices*beishu*days
    print(f'您租赁的汽车{days}天，共计{prices}')



