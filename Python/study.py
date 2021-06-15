#!/usr/bin/python3

import self as self
import sys
import re

'''
函数	描述
int(x [,base])
将x转换为一个整数

long(x [,base] )
将x转换为一个长整数

float(x)
将x转换到一个浮点数

complex(real [,imag])
创建一个复数

str(x)
将对象 x 转换为字符串

repr(x)
将对象 x 转换为表达式字符串

eval(str)
用来计算在字符串中的有效Python表达式,并返回一个对象

tuple(s)
将序列 s 转换为一个元组

list(s)
将序列 s 转换为一个列表

set(s)
转换为可变集合

dict(d)
创建一个字典。d 必须是一个序列 (key,value)元组。

frozenset(s)
转换为不可变集合

chr(x)
将一个整数转换为一个字符

unichr(x)
将一个整数转换为Unicode字符

ord(x)
将一个字符转换为它的整数值

hex(x)
将一个整数转换为一个十六进制字符串

oct(x)
将一个整数转换为一个八进制字符串
'''

'''
a_dic = {'A1': 1, 'B1': 2}
value = a_dic['A1'] + 1
b_dic = {'A2': value, 'B2': 3}
b_dic['A2'] = int(a_dic['A1']) + 1
print(a_dic)
print(b_dic)
print('---------')
a_dic['A1'] = 3
print(a_dic)
print(b_dic)
'''

'''
class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Person2(self):
        name2 = self.name
        age2 = self.age + 1


p1 = Person1("Bill", 63)
Person1.Person2()
print(p1.name)
print(p1.age)
p2 = Person1("Bill", 65)
Person1.Person2()
print(p2.name)
print(p2.age)
'''

'''
a_dic = {'A1': 1, 'B1': 2}
b_dic = {'A2': int(a_dic['A1'])+1, 'B2': 3}
b_dic['A2'] = int(a_dic['A1'])+1
print(a_dic)
print(b_dic)
print('---------')
a_dic['A1'] = 3
print(a_dic)
print(b_dic)
'''

'''
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
'''



Helmet = {
    'HP': 10,
    'MP': 5,
    'Defense': 3
}

Clothes = {
    'HP': 8,
    'Defense': 4
}

Weapon = {
    'Attack': 12,
    'Crit_Odds': 2
}

Pants = {
    'HP': 7,
    'Defense': 2
}

Rings = {
    'Crit_Odds': 5
}

Shoes = {
    'Miss_Odds': 3,
    'Move_Speed': 1
}


Hero_Initial_Characteristic = {'HP': 10,
                               'MP': 5,
                               'Attack': 4,
                               'Defense': 1,
                               'EXP': 19,
                               'Level': 1,
                               'Crit_Odds': 4,
                               'Miss_Odds': 0,
                               'Move_Speed': 1
                               }


class Hero_Characteristic:
    def __init__(self, HP_Max, HP_Remind, Defense, Attack, Crit_Odds, Miss_Odds, Move_Speed, EXP_Have,
                 EXP_Ceiling):
        self.HP_Max = HP_Max
        self.HP_Remind = HP_Remind
        self.Defense = Defense
        self.Attack = Attack
        self.Crit_Odds = Crit_Odds
        self.Miss_Odds = Miss_Odds
        self.Move_Speed = Move_Speed
        self.EXP_Have = EXP_Have
        self.EXP_Ceiling = EXP_Ceiling

    def myfunc(self):
        print(self.Defense)



Hero = Hero_Characteristic((Hero_Initial_Characteristic.get('HP') + Helmet['HP'] + Clothes['HP'] + Pants['HP']),
                           (Hero_Initial_Characteristic['HP'] + Helmet['HP'] + Clothes['HP'] + Pants['HP']),
                           (Hero_Initial_Characteristic['Defense'] + Helmet['Defense'] + Clothes['Defense'] + Pants[
            'Defense']),
                           (Hero_Initial_Characteristic['Attack'] + Weapon['Attack']),
                           (Hero_Initial_Characteristic['Crit_Odds'] + Rings['Crit_Odds']),
                           (Hero_Initial_Characteristic['Miss_Odds'] + Shoes['Miss_Odds']),
                           (Hero_Initial_Characteristic['Move_Speed'] + Shoes['Move_Speed']),
                           (Hero_Initial_Characteristic['EXP']),
                           20)

print(Hero_Initial_Characteristic['HP'])
Hero.myfunc()
print(Hero.__dict__['HP_Max'])
#print(type(Hero.__dict__['Defense']))
Hero_Initial_Characteristic['HP'] = Hero_Initial_Characteristic['HP'] + 6
Hero = Hero_Characteristic((Hero_Initial_Characteristic.get('HP') + Helmet['HP'] + Clothes['HP'] + Pants['HP']),
                           (Hero_Initial_Characteristic['HP'] + Helmet['HP'] + Clothes['HP'] + Pants['HP']),
                           (Hero_Initial_Characteristic['Defense'] + Helmet['Defense'] + Clothes['Defense'] + Pants[
            'Defense']),
                           (Hero_Initial_Characteristic['Attack'] + Weapon['Attack']),
                           (Hero_Initial_Characteristic['Crit_Odds'] + Rings['Crit_Odds']),
                           (Hero_Initial_Characteristic['Miss_Odds'] + Shoes['Miss_Odds']),
                           (Hero_Initial_Characteristic['Move_Speed'] + Shoes['Move_Speed']),
                           (Hero_Initial_Characteristic['EXP']),
                           20)

print(Hero_Initial_Characteristic['HP'])
Hero.myfunc()
print(Hero.__dict__['HP_Max'])