#!/usr/bin/python3
# -*- coding:utf-8 -*-

from random import randrange

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
    'Crit_Probability': 2
}

Pants = {
    'HP': 7,
    'Defense': 2
}

Rings = {
    'Crit_Probability': 5
}

Shoes = {
    'Miss_probability': 3,
    'Move_Speed': 1
}

Treasures = ('Helmet',
             'Clothes',
             'Weapon',
             'Pants',
             'Rings',
             'Shoes')

Treasures_Own = []

Hero_Initial_Characteristic = {'HP': 10,
                               'MP': 5,
                               'Attack': 4,
                               'Defense': 1,
                               'EXP': 19,
                               'Level': 1,
                               'Crit_Probability': 4,
                               'Miss_Probability': 0,
                               'Move_Speed': 1
                               }

Monster_List = {}

Monster_Characteristic = {'HP': 40,
                          'MP': 6,
                          'Attack': 20,
                          'Defense': 1,
                          'EXP': 3,
                          'Level': 2,
                          'Crit_Probability': 0,
                          'Miss_Probability': 1}

# 英雄属性为初始属性加上装备属性
Hero_Characteristic = {
    'HP_Max': Hero_Initial_Characteristic.get('HP') + Helmet['HP'] + Clothes['HP'] + Pants['HP'],
    'HP_Remind': Hero_Initial_Characteristic['HP'] + Helmet['HP'] + Clothes['HP'] + Pants['HP'],
    'Defense': Hero_Initial_Characteristic['Defense'] + Helmet['Defense'] + Clothes['Defense'] + Pants['Defense'],
    'Attack': Hero_Initial_Characteristic['Attack'] + Weapon['Attack'],
    'Crit_Probability': Hero_Initial_Characteristic['Crit_Probability'] + Rings['Crit_Probability'],
    'Miss_probability': Hero_Initial_Characteristic['Miss_Probability'] + Shoes['Miss_probability'],
    'Move_Speed': Hero_Initial_Characteristic['Move_Speed'] + Shoes['Move_Speed'],
    'EXP_Have': Hero_Initial_Characteristic['EXP'],
    'EXP_Ceiling': 20

}

print(Hero_Initial_Characteristic)
print(Hero_Characteristic)

# 几率
print(randrange(1, 100))


def Fight():
    Monster_HP_Remind = Monster_Characteristic['HP'] - Hero_Characteristic['Attack']
    Hero_HP_Remind = Hero_Characteristic['HP_Remind'] - Monster_Characteristic['Attack']
    while Monster_HP_Remind > 0 and Hero_HP_Remind > 0:
        if randrange(1, 100) > Hero_Characteristic['Crit_Probability'] and randrange(1, 100) > Hero_Characteristic[
                                                                                                'Miss_probability']:
            Monster_HP_Remind = Monster_Characteristic['HP'] + Monster_Characteristic['Defense'] - Hero_Characteristic[
                'Attack']
            Hero_HP_Remind = Hero_Characteristic['HP_Remind'] + Hero_Characteristic['Defense'] - Monster_Characteristic[
                'Attack']
        elif Hero_Characteristic['Crit_Probability'] > randrange(1, 100) > Hero_Characteristic['Miss_probability']:
            print('You crited')
            Monster_HP_Remind = Monster_Characteristic['HP'] + Monster_Characteristic['Defense'] - Hero_Characteristic[
                'Attack'] * 2
            Hero_HP_Remind = Hero_Characteristic['HP_Remind'] + Hero_Characteristic['Defense'] - Monster_Characteristic[
                'Attack']
        elif randrange(1, 100) < Hero_Characteristic['Miss_probability']:
            print('Monster missed')
            Monster_HP_Remind = Monster_Characteristic['HP'] + Monster_Characteristic['Defense'] - Hero_Characteristic[
                'Attack']
            Hero_HP_Remind = Hero_Characteristic['HP_Remind']
        Monster_Characteristic['HP'] = Monster_HP_Remind
        Hero_Characteristic['HP_Remind'] = Hero_HP_Remind
        randrange(1, 100)
        print(randrange(1, 100))
        print('---------------')
        print(Hero_HP_Remind)
        print(Monster_HP_Remind)
    else:
        if Monster_HP_Remind < 0:
            print('You are winning')
            Hero_Characteristic['EXP_Have'] = Hero_Initial_Characteristic['EXP'] + Monster_Characteristic['EXP']
            print(Hero_Characteristic['EXP_Have'])
            Level_Up()
        elif Hero_HP_Remind < 0:
            print('You are death')


def Player_Choice():
    if Choice == 'run':
        print("You are running.")
    elif Choice == 'fight':
        print('Fight')
        # 交战，英雄先出手
        Fight()
    else:
        print("Make a choose")


# 升级
def Level_Up():
    if Hero_Characteristic['EXP_Have'] > Hero_Characteristic['EXP_Ceiling']:
        print('Level up!')
        Hero_Initial_Characteristic['EXP'] = Hero_Characteristic['EXP_Have'] - Hero_Characteristic['EXP_Ceiling']
        Hero_Initial_Characteristic['Level'] += 1
        Hero_Characteristic['EXP_Ceiling'] += 30
        Hero_Initial_Characteristic['Attack'] += 2
        Hero_Initial_Characteristic['Defense'] += 1
        Hero_Initial_Characteristic['HP'] += 3
        Hero_Initial_Characteristic['MP'] += 1
        Hero_Initial_Characteristic['Move_Speed'] += 0.25
        Hero_Characteristic['HP_Remind'] = Hero_Characteristic['HP_Max']
        print(Hero_Initial_Characteristic)
        print(Hero_Characteristic)


Choice = input("please choose you choice:"
               "fight"
               "run")
Player_Choice()
