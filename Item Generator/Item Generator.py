import random
while True:
    print('What are you trying to generate? \n Weapon, Armor, Enhancement, Curse, RWG, RAG')
    choice = input()
    choice = choice.lower()
    if choice == 'weapon':
        print('Please specify which type of weapon you want. Example: simple or martial (ranged) weapon.')
        weapon_choice = input()
        weapon_choice = weapon_choice.lower()
        while True:
            if weapon_choice == 'simple':
                random_simple = random.choice(open('simple weapon.txt').readlines())
                print(random_simple)
                break
            elif weapon_choice == 'srange':
                random_srange = random.choice(open('simple ranged weapon.txt').readlines())
                print(random_srange)
                break
            elif weapon_choice == 'martial':
                random_martial = random.choice(open('martial weapon.txt').readlines())
                print(random_martial)
                break
            elif weapon_choice == 'mrange':
                random_mrange = random.choice(open('martial ranged weapon.txt').readlines())
                print(random_mrange)
                break
            elif weapon_choice == 'back':
                break
    elif choice =='armor':
        print('Please specify which type of armor you want. Example: light, medium, heavy, shield.')
        armor_choice = input()
        armor_choice = armor_choice.lower()
        while True:
            if armor_choice == 'light':
                random_light = random.choice(open('light armor.txt').readlines())
                print(random_light)
                break
            elif armor_choice == 'medium':
                random_medium = random.choice(open('medium armor.txt').readlines())
                print(random_medium)
                break
            elif armor_choice == 'heavy':
                random_heavy = random.choice(open('heavy armor.txt').readlines())
                print(random_heavy)
                break
            elif armor_choice == 'shield':
                random_shield = random.choice(open('shield.txt').readlines())
                print(random_shield)
                break
            elif armor_choice == 'back':
                break
    elif choice == 'enhancement':
        random_enhancement = random.choice(open('enhancement.txt').readlines())
        print(random_enhancement)
        continue
    elif choice == 'curse':
        print('What is the curse for? Weapon or Armor?')
        curse_choice = input()
        curse_choice = curse_choice.lower()
        while True:
            if curse_choice == 'weapon':
                random_curse = random.choice(open('wcurse.txt').readlines())
                print(random_curse)
                break
            elif curse_choice == 'armor':
                random_curse = random.choice(open('acurse.txt').readlines())
                print(random_curse)
                break
    elif choice == 'rwg': #Random Weapon Generated
        random_weapon = random.choice(open('all weapons.txt').readlines())
        random_enhancement = random.choice(open('enhancement.txt').readlines())
        random_curse = random.choice(open('wcurse.txt').readlines())
        print(random_weapon)
        print(random_enhancement)
        print(random_curse)
        continue
    elif choice == 'rag': #Random Armor Generated
        random_armor = random.choice(open('all armor.txt').readlines())
        random_enhancement = random.choice(open('enhancement.txt').readlines())
        random_curse = random.choice(open('acurse.txt').readlines())
        print(random_armor)
        print(random_enhancement)
        print(random_curse)
        continue
    elif choice == 'quit':
        break
print('Thanks for using the shop!')
