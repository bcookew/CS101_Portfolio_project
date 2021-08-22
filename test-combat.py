from hst import Score_Card
from Actions import attack_roll, evade, damage_roll, cast_roll
from dice import *
from Player_classes import Monk, Paladin, Barbarian
from Bad_Guy_Classes import Goblin


baddy = Goblin()


#print('\n')



def combat():
    print(f"\n{player.name} starting with {str(player.hp)} hp")
    print(f"{baddy.name} is starting with {str(baddy.hp)}hp\n")

    while player.hp > 0:
        print('#####################################################')
        player_act = input('Attack, Cast Spell, Evade? ').lower()
        baddy_act = baddy_action() #randomizes baddy action
        
        
        if player_act == 'attack' and baddy_act == 'attack':
            print(player_act)
            print(baddy_act + "\n")
            player_hit = attack_roll(player.atk_mod, baddy.armor)
            baddy_hit = attack_roll(baddy.atk_mod, player.armor)
            if player_hit == True: #Checks if player hit successfully and deals damage if true
                damage = damage_roll(player.weapons)
                baddy.hp -= damage
                print(f'{player.name} did {damage} points of damage to the {baddy.name}')
                if baddy.hp <= 0:
                    print(f'{player.name} killed the {baddy.name}!')    
                else:
                    if baddy_hit == True:
                        damage =  damage_roll(baddy.weapons)
                        player.hp -= damage
                        print(f'The {baddy.name} did {damage} points of damage to {player.name}')
                    else:
                        print(f'The {baddy.name} swang and missed!')
            else:
                print(f'{player.name} swang and missed!')
                if baddy_hit == True:
                    damage = damage_roll(baddy.weapons)
                    player.hp -= damage
                    print(f'The {baddy.name} did {damage} points of damage to {player.name}')
                else:
                    print(f'The {baddy.name} swang and missed!')
                            
        elif player_act == 'attack' and baddy_act == 'cast spell':
            print(player_act)
            print(baddy_act + "\n")
            player_hit = attack_roll(player.atk_mod, baddy.armor)
            baddy_hit = cast_roll(baddy.spell_mod, player.armor)
            if player_hit == True: #Checks if player hit successfully and deals damage if true
                damage = damage_roll(player.weapons)
                baddy.hp -= damage
                print(f'{player.name} did {damage} points of damage to the {baddy.name}')
                if baddy.hp <= 0:
                    print(f'{player.name} killed the {baddy.name}!')    
                else:
                    if baddy_hit == True:
                        #add stunned status code here
                        print(f'The {baddy.name} cast {baddy.spells[0]} and stunned {player.name}')
                    else:
                        print(f'The {baddy.name} cast {baddy.spells[0]} but {player.name} resisted!')
            else:
                print(f'{player.name} swang and missed!')
                if baddy_hit == True:
                    #add stunned status code here
                    print(f'The {baddy.name} cast {baddy.spells[0]} and stunned {player.name}')
                else:
                    print(f'The {baddy.name} cast {baddy.spells[0]} but {player.name} resisted!')

        elif player_act == 'attack' and baddy_act == 'evade':
            print(player_act)
            print(baddy_act + "\n")
            baddy.dodged = evade(baddy.dex_mod, player.dex_mod) 
            if baddy.dodged == True: #Checks if baddy evades successfully and skips player attack if true
                print(f'The {baddy.name} dodged {player.name}\'s attack!')
            else:
                player_hit = attack_roll(player.atk_mod, baddy.armor)
                if player_hit == True: #Checks if player hit successfully and deals damage if true
                    damage =  damage_roll(player.weapons)
                    baddy.hp -= damage
                    print(f'{player.name} did {damage} points of damage to the {baddy.name}')
                    print(f'{baddy.name} tried to evade and failed!')
                    if baddy.hp <= 0:
                        print(f'{player.name} killed the {baddy.name}!')
                else:
                    print(f'{player.name} swang and missed!')
                    continue

        elif player_act == 'cast spell' and baddy_act == 'attack':
            print(player_act)
            print(baddy_act + "\n")
            player_hit = cast_roll(player.spell_mod, baddy.armor)
            if player_hit == True: #Checks if player hit successfully and deals damage if true
                # Add statusing code here
                print(f'{player.name} cast {player.spells[0]} and stunned {baddy.name}')
            else:
                print(f'{player.name} cast {player.spells[0]} but the {baddy.name} resisted!')
                baddy_hit = attack_roll(baddy.atk_mod, player.armor)
                if baddy_hit == True:
                    damage = damage_roll(baddy.weapons)
                    player.hp -= damage
                    print(f'The {baddy.name} did {damage} points of damage to {player.name}')
                else:
                    print(f'The {baddy.name} swang and missed!')

        elif player_act == 'cast spell' and baddy_act == 'cast spell':
            print(player_act)
            print(baddy_act + "\n")
            player_hit = cast_roll(player.spell_mod, baddy.armor)
            baddy_hit = cast_roll(baddy.spell_mod, player.armor)
            if player_hit == True: #Checks if player hit successfully and deals damage if true
                # Add statusing code here
                print(f'The {player.name} cast {player.spells[0]} and stunned {baddy.name}')
            else:
                print(f'{player.name} cast {player.spells[0]} but the {baddy.name} resisted!')
                if baddy_hit == True:
                    #add stunned status code here
                    print(f'The {baddy.name} cast {baddy.spells[0]} and stunned {player.name}\n')
                else:
                    print(f'The {baddy.name} cast {baddy.spells[0]} but {player.name} resisted!\n')

        elif player_act == 'cast spell' and baddy_act == 'evade':
            print(player_act)
            print(baddy_act + "\n")
            baddy.dodged = evade(baddy.dex_mod, player.dex_mod) 
            if baddy.dodged == True: # Checks if baddy evades successfully and skips player attack if true
                print(f'The {baddy.name} dodged {player.name}\'s attack!\n')
            else:
                player_hit = cast_roll(player.spell_mod, baddy.armor)
                if player_hit == True: #Checks if player hit successfully and deals damage if true
                    # Add statusing code here
                    print(f'The {baddy.name} cast {baddy.spells[0]} and stunned {player.name}\n')
                else:
                    print(f'{player.name} cast {player.spells[0]} but the {baddy.name} attempted to evade and resisted!\n')

        elif player_act == 'evade' and baddy_act == 'attack':
            print(player_act)
            print(baddy_act + "\n")
            player.dodged = evade(player.dex_mod, baddy.dex_mod) 
            if player.dodged == True: #Checks if player evades successfully and skips baddy attack if true
                print(f'{player.name} dodged the {baddy.name}\'s attack!\n')
            else:
                baddy_hit = attack_roll(baddy.atk_mod, player.armor)
                if baddy_hit == True: #Checks if baddy hit successfully and deals damage if true
                    damage = damage_roll(baddy.weapons)
                    player.hp -= damage
                    print(f'{baddy.name} did {damage} points of damage to {player.name}\n')
                else:
                    print(f'The {baddy.name} swang and missed!\n')
        
        elif player_act == 'evade' and baddy_act == 'cast spell':
            print(player_act)
            print(baddy_act + "\n")
            player.dodged = evade(player.dex_mod, baddy.dex_mod) 
            baddy_hit = cast_roll(baddy.spell_mod, player.armor)
            if player.dodged == True: #Checks if player evades successfully and skips baddy attack if true
                print(f'The {player.name} dodged the {baddy.name}\'s attack!\n')
            else:
                if baddy_hit == True:
                    #add stunned status code here
                    print(f'The {baddy.name} cast {baddy.spells[0]} and stunned {player.name}\n')
                else:
                    print(f'The {baddy.name} cast {baddy.spells[0]} but {player.name} resisted!\n')

        elif player_act == 'evade' and baddy_act == 'evade':
            print(player_act)
            print(baddy_act + "\n")
            print('\nYou both dodged!\n')
        
        elif player_act == 'quit' or 'Quit':
            break
        
        else:
            print('''Please enter 'Attack', 'Cast Spell', 'Evade', or 'Quit'.''')

high_scores = Score_Card.load_high_scores()
Score_Card.print_scores()       

name = input('Greetings friend! What is your name? ')

knows_classes = input(f'''\nIt\'s good to have you here {name}.\n
I hope you put on your fighting pants today...\n
Do you know what fighting class you want to pick?(yes/no): ''')

if knows_classes.lower() == 'yes':
    chosen_class = input('\nGreat! Good and ready for the grinder I see. \nThe spectators in the arena will love that! So which one: ')
else:
    chosen_class = input('''Ok then, let's see...\n 
    The three fighting styles we allow are Monk, Paladin, and Barbarian.\n What's your style: ''')

if chosen_class.lower() == "monk":
    player = Monk(name, chosen_class.capitalize())
elif chosen_class.lower() == "paladin":
    player = Paladin(name, chosen_class.capitalize())
elif chosen_class.lower() == "barbarian":
    player = Barbarian(name, chosen_class.capitalize())

print(f'\nOk, {player.name} it\'s time to send you into the arena. \n{player}... That sounds pretty good I reckon.\nI\'m sure you\'ll do fine')

print(f'''\n{player.name} is a {player.chosen_class}\n
Their stats are:
    {player.atk_mod} Attack Mod
    {player.spell_mod} Spell Mod
    {player.dex_mod} Dexterity Mod
    \n''')



combat()