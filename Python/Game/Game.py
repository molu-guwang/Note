#!/usr/bin/python3



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
Hero_Characteristic = {'HP': 10, 'MP': 5, 'Attack': 4, 'Defense': 1, 'EXP': 0, 'Level': 1,
                       'Crit_Probability': 0, 'Miss_Probability': 0, 'Move_Speed': 1}
Monster_Characteristic = {'HP': 200, 'MP': 6, 'Attack': 20, 'Defense': 1, 'EXP': 3, 'Level': 2,
                          'Crit_Probability': 0, 'Miss_Probability': 1}

Hero_HP_Own = Hero_Characteristic['HP']+Helmet['HP']+Clothes['HP']+Pants['HP']
print(Hero_HP_Own)

'''
def Player_Choice(run):
    if Player_Choice():
        print("You are running.")
    else :
        print('Fight')
        Monster_HP_Remind = Monster_Characteristic('HP') - Hero_Characteristic('Attack')
        Hero_HP_Remind = Hero_Characteristic('HP') - Monster_Characteristic('Attack')
        print(Hero_HP_Remind)
        print(Monster_HP_Remind)
        while Monster_HP_Remind >0 and Hero_HP_Remind >0:
            continue
        while Monster_HP_Remind <0 or Hero_HP_Remind <0 :
            break
        if Monster_HP_Remind <0:
            print()
        elif Hero_HP_Remind <0:
            print()

Choice=input("please choose you choise:"
             "fight"
             "run")
if Choice == "run":
    Player_Choice()
'''





