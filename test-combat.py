from Player_classes import Monk
from Bad_Guy_Classes import Goblin

player = Monk('Ben Jammin', 'Monk')
baddy = Goblin()

print('\n')
print(f"{player.name} is fighting as a {player.chosen_class} starting with {str(player.hp)} hp")
print(f"{baddy.name} is starting with {str(baddy.hp)}hp\n")

while player.hp > 0:
    userinput = input('Attack, Cast Spell, Evade? ')
    if userinput.lower() == 'attack':
        print('\n=========================================================\n')
        hit_check = baddy.hp
        baddy.hp = player.attack(player.weapons,baddy.atk_mod, baddy.hp)
        if hit_check > baddy.hp:
            print(f"{player.name} hit for {str(hit_check - baddy.hp)} points of damage")
            print(baddy.name + " now has " + str(baddy.hp) + "hp\n")
        else:
            print(f'{player.name} swung their {player.weapons[0]} and missed!\n')
    elif userinput.lower() == 'cast spell':
        continue
    elif userinput.lower() == 'evade':
        player.dodged = player.evade(baddy.dex_mod)

    player.dodged, player.hp = baddy.attack(baddy.weapons, player.armor, player.hp, player.dodged)

    print(player.chosen_class + " " + str(player.hp) + "hp")
    print(baddy.name + " " + str(baddy.hp) + "hp")
