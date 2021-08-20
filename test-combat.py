from Player_classes import Monk
from Bad_Guy_Classes import Goblin

player = Monk('Ben Jammin', 'Monk')
baddy = Goblin()

print('\n')
print(player.chosen_class + " is starting with " + str(player.hp) + "hp")
print(baddy.name + " is starting with " + str(baddy.hp) + "hp\n")
continuing = True
while continuing == True:
    if player.hp > 0:
        userinput = input('Do you want to attack again? ')
        if userinput.lower() == 'yes':
            print('\n=========================================================\n')
            hit_check = baddy.hp
            baddy.hp = player.attack(player.weapons,baddy.atk_mod, baddy.hp)
            if hit_check > baddy.hp:
                print(player.name + " hit for " + str(hit_check - baddy.hp) + " points of damage")
                print(baddy.name + " now has " + str(baddy.hp) + "hp\n")
            else:
                print(f'{player.name} swung their {player.weapons[0]} and missed!\n')
        elif userinput.lower() == 'no':
            continuing = False
        if baddy.hp > 0:
            hit_check = player.hp
            player.hp = baddy.attack(baddy.weapons,player.atk_mod, player.hp)
            if hit_check > player.hp:
                print(baddy.name + " hit for " + str(hit_check - player.hp) + " points of damage!")
                print(player.name + " now has " + str(player.hp) + "hp\n")
            else:
                print(f'{baddy.name} swung their {baddy.weapons[0]} and missed!\n')
        elif baddy.hp <= 0:
            print(f"You killed the {baddy.name}!\n")
            continuing = False
    else:
        continuing = False

#print(player.chosen_class + " " + str(player.hp) + "hp")
#print(baddy.name + " " + str(baddy.hp) + "hp")
