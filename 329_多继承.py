class a():
    def a_1(self):
        print('aaa')

class b():
    def b_1(self):
        print('bbb')

class c():
    def c_1(self):
        print('ccc')

class d(a,b,c):
    pass
h1=d()
h1.c_1()
h1.b_1()
h1.a_1()
