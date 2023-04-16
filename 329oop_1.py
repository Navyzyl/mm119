class Person():
    person_num=0
    def __init__(self,n,a,w):
        self.names=n
        self.ages=a
        self.walk=w
        Person.person_num += 1
    def say(self):
        print(f'我叫{self.names}今年{self.ages}岁，能走{self.walk}米')



#a=Person()
#a.names='zyl'
#a.ages='18'
#a.walk=100000
#a.say()
#b=Person()
#b.names='mjy'
#b.ages='18'
#b.walk=500
#b.say()
#print(f'names')
a=Person('zyl',18,50000)
a.say()
b=Person('aaa',55,5555555)
c=Person('kahd',19,444444)
print(Person.person_num)

