#!/usr/bin/python3
#迭代器
import sys  # 引入 sys 模块
import self as self

'''
List = [1, 2, 3, 4]
it = iter(List)    # 创建迭代器对象
for x in it:
    print(x, end=" ")

print('')
print('----------')
List = [1, 2, 3, 4]
it = iter(List)  # 创建迭代器对象


'''
class Animal():
    self.age = 0  # 类属性

    def Eat(self):  # 类方法
        print("觅食")


dog = Animal()  # 类的实例化，即对象
cat = Animal()  # 类的实例化，即对象
dog.Eat()  # 相当于Animal.Eat(dog)

a_dic = {'A1': 1, 'B1': 2}


class Person:
    def __init__(self, attack, defense):
        self.attack = attack
        self.defense = defense + a_dic['A1']

    def myfunc(self):
        print(self.defense)

class Hero(Person):
    pass

Hero = Person(10, 63)
Hero.myfunc()
print(Hero.__dict__['defense'])
Hero = Person(10, a_dic['B1'] + 2)
Hero.myfunc()
print(type(Hero.__dict__['defense']))

