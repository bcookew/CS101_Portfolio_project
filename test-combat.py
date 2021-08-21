from Actions import attack_roll, evade, damage_roll
from dice import *
from Player_classes import Monk
from Bad_Guy_Classes import Goblin


player = Monk('Ben Jammin', 'Monk')
baddy = Goblin()

#player_stats = {'hp': player.hp, 'armor':player.armor, 'atk': player.atk_mod, 'spell': player.spell_mod, 'dex': player.dex_mod}
#baddy_stats = {'hp': baddy.hp, 'armor':baddy.armor, 'atk': baddy.atk_mod, 'spell': baddy.spell_mod, 'dex': baddy.dex_mod}
#weapons = {'scimitar':4, 'Brass Knuckles':3}

print('\n')
print(f"{player.name} is fighting as a {player.chosen_class} starting with {str(player.hp)} hp")
print(f"{baddy.name} is starting with {str(baddy.hp)}hp\n")


def combat():
    while player.hp > 0:
        
        player_act = input('Attack, Cast Spell, Evade? ').lower
        baddy_act = baddy_action() #randomizes baddy action
        print(player_act)
        print(baddy_act)
        
        if player_act == 'evade' and baddy_act == 'evade':
            print('\nYou both dodged!\n')
            continue
        
        elif player_act == 'attack' and baddy_act == 'evade':
            baddy.dodged = evade(baddy.dex_mod, player.dex_mod) 
            if baddy.dodged == True: #Checks if baddy evades successfully and skips player attack if true
                print(f'The {baddy.name} dodged {player.name}\'s attack!')
                continue
            else:
                player_hit = attack_roll(player.atk_mod, baddy.armor)
                if player_hit == True: #Checks if player hit successfully and deals damage if true
                    damage =  damage_roll(player.weapons)
                    baddy.hp -= damage
                    print(f'{player.name} did {damage} points of damage to the {baddy.name}')
                else:
                    print(f'{player.name} swang and missed!')
                    continue

        elif player_act == 'evade' and baddy_act == 'attack':
            player.dodged = evade(player.dex_mod, baddy.dex_mod) 
            if player.dodged == True: #Checks if player evades successfully and skips baddy attack if true
                print(f'The {player.name} dodged the {player.name}\'s attack!')
                continue
            else:
                baddy_hit = attack_roll(baddy.atk_mod, player.armor)
                if baddy_hit == True: #Checks if baddy hit successfully and deals damage if true
                    damage = damage_roll(baddy.weapons)
                    player.hp -= damage
                    print(f'{baddy.name} did {damage} points of damage to {player.name}')
                else:
                    print(f'The {baddy.name} swang and missed!')
                    continue
        else:
            print('no condition met')
            continue




combat()













                # if player_action.lower() == 'attack':
                #     print('\n=========================================================\n')
                #     hit_check = baddy.hp
                #     baddy.hp = player.attack(player.weapons,baddy.atk_mod, baddy.hp)
                #     if hit_check > baddy.hp:
                #         print(f"{player.name} hit for {str(hit_check - baddy.hp)} points of damage")
                #         print(baddy.name + " now has " + str(baddy.hp) + "hp\n")
                #     else:
                #         print(f'{player.name} swung their {player.weapons[0]} and missed!\n')
                # elif player_action.lower() == 'cast spell':
                #     continue
                # elif player_action.lower() == 'evade':
                #     player.dodged = player.evade(baddy.dex_mod)

                # player.dodged, player.hp = baddy.attack(baddy.weapons, player.armor, player.hp, player.dodged)

                # print(player.chosen_class + " " + str(player.hp) + "hp")
                # print(baddy.name + " " + str(baddy.hp) + "hp")
