#!/usr/bin/python3
# -*- coding:utf-8 -*-

from random import randrange

Helmet = {
    'HP': '10',
    'MP': '5',
    'Defense': '3'
}

Clothes = {
    'HP': '8',
    'Defense': '4'
}

Weapon = {
    'Attack': '12',
    'Crit_Probability': '2'
}

Pants = {
    'HP': '7',
    'Defense': '2'
}

Rings = {
    'Crit_Probability': '5'
}

Shoes = {
    'Miss_probability': '3',
    'Move_Speed': '1'
}

Treasures = ('Helmet', 'Clothes', 'Weapon', 'Pants', 'Rings', 'Shoes')
Treasures_Own = []
Hero_Initial_Characteristic = {'HP': 10, 'MP': 5, 'Attack': 4, 'Defense': 1, 'EXP': 0, 'Level': 1,
                               'Crit_Probability': 50, 'Miss_Probability': 0, 'Move_Speed': 1}

Monster_List = {}
Monster_Characteristic = {'HP': 200, 'MP': 6, 'Attack': 20, 'Defense': 1, 'EXP': 3, 'Level': 2,
                          'Crit_Probability': 0, 'Miss_Probability': 1}

# 英雄属性为初始属性加上装备属性
Hero_Characteristic = {
    'HP_Max': int(Hero_Initial_Characteristic['HP']) + int(Helmet['HP']) + int(Clothes['HP']) + int(Pants['HP']),
    'HP_Remind': int(Hero_Initial_Characteristic['HP']) + int(Helmet['HP']) + int(Clothes['HP']) + int(Pants['HP']),
    'Defense': int(Hero_Initial_Characteristic['Defense']) + int(Helmet['Defense']) + int(Clothes['Defense']) + int(
        Pants['Defense']),
    'Attack': int(Hero_Initial_Characteristic['Attack']) + int(Weapon['Attack']),
    'Crit_Probability': int(Rings['Crit_Probability']),
    'Miss_probability': int(Shoes['Miss_probability']),
    'Move_Speed': int(Hero_Initial_Characteristic['Move_Speed']) + int(Shoes['Move_Speed'])
}

print(Hero_Characteristic)

# 几率
print(randrange(1, 100))


def Fight():
    Monster_HP_Remind = int(Monster_Characteristic['HP']) - int(Hero_Characteristic['Attack'])
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


Choice = input("please choose you choise:"
               "fight"
               "run")
Player_Choice()
