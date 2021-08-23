from hst import Score_Card
from Actions import attack_roll, evade, damage_roll, cast_roll
from dice import *
from Player_classes import Monk, Paladin, Barbarian
from Bad_Guy_Classes import Goblin, Lizardfolk, Bugbear


big_bads = [Goblin, Lizardfolk, Bugbear]
monk = Monk('Monk', 'monk')
paladin = Paladin('Paladin', 'paladin')
barbarian = Barbarian('Barbarian', 'barbarian')
knows_classes = ''
chosen_class = ''

#print('\n')



def combat():
    round_counter = 1
    points = 0
    player_starting_hp = player.hp
    for big_bad in big_bads:
        baddy = big_bad()
        print(f'\nA new challenger approaches!')
        print(f"\n{player.name} starting with {str(player.hp)} hp")
        print(f"{baddy.name} is starting with {str(baddy.hp)}hp\n")
        baddy_starting_hp = baddy.hp
        while baddy.hp > 0:
            print(f'\n##########--Round {str(round_counter)}--##########')
            print(f'{player.name}: {player.hp}hp        {baddy.name}: {baddy.hp}\n')
            if player.stunned == False and baddy.stunned == False:
                player_act = input('Attack, Cast Spell, Evade? ').lower()
                baddy_act = baddy_action() #randomizes baddy action
            elif player.stunned == True:
                print(f'{player.name} is stunned this round\n')
                player_act = 'stunned'
                player.stunned = False
                baddy_act = baddy_action() #randomizes baddy action    
            elif baddy.stunned == True:
                print(f'The {baddy.name} is stunned this round\n')
                baddy_act = 'stunned'
                baddy.stunned = False
                player_act = input('Attack, Cast Spell, Evade? ').lower()
            
            if player_act not in ['attack', 'cast spell', 'evade', 'stunned']:
                print('''Please enter 'Attack', 'Cast Spell', 'Evade', or 'Quit'.''')
                continue
            else:
                round_counter += 1
                points += 2
            
            if player_act == 'attack' and baddy_act == 'attack':
                print(player_act)
                print(baddy_act + "\n")
                player_hit = attack_roll(player.atk_mod, baddy.armor)
                baddy_hit = attack_roll(baddy.atk_mod, player.armor)
                if player_hit == True: #Checks if player hit successfully and deals damage if true
                    damage = damage_roll(player.weapons)
                    points += damage
                    baddy.hp -= damage
                    print(f'{player.name} did {damage} points of damage to the {baddy.name} with their {player.weapons[0]}')
                    if baddy.hp <= 0:
                        print(f'{player.name} killed the {baddy.name}!')    
                    else:
                        if baddy_hit == True:
                            damage =  damage_roll(baddy.weapons)
                            player.hp -= damage
                            print(f'The {baddy.name} did {damage} points of damage to {player.name}')
                            if player.hp <= 0:
                                print(f'{player.name} died. They were killed by a {baddy.name} with only {baddy.hp}hp left.')
                                break
                        else:
                            print(f'The {baddy.name} swang and missed!')
                else:
                    print(f'{player.name} swang and missed!')
                    if baddy_hit == True:
                        damage = damage_roll(baddy.weapons)
                        player.hp -= damage
                        print(f'The {baddy.name} did {damage} points of damage to {player.name} with their {baddy.weapons[0]}\n')
                        if player.hp <= 0:
                            print(f'{player.name} died. They were killed by a {baddy.name} with only {baddy.hp}hp left.')
                            break
                    else:
                        print(f'The {baddy.name} swang and missed!')
                                
            elif player_act == 'attack' and baddy_act == 'cast spell':
                print(player_act)
                print(baddy_act + "\n")
                player_hit = attack_roll(player.atk_mod, baddy.armor)
                baddy_hit = cast_roll(baddy.spell_mod, player.armor)
                if player_hit == True: #Checks if player hit successfully and deals damage if true
                    damage = damage_roll(player.weapons)
                    points += damage
                    baddy.hp -= damage
                    print(f'{player.name} did {damage} points of damage to the {baddy.name} with their {player.weapons[0]}')
                    if baddy.hp <= 0:
                        print(f'{player.name} killed the {baddy.name}!')    
                    else:
                        if baddy_hit == True:
                            player.stunned = True
                            print(f'The {baddy.name} cast {baddy.spells[0]} and stunned {player.name}')
                        else:
                            print(f'The {baddy.name} cast {baddy.spells[0]} but {player.name} resisted!')
                else:
                    print(f'{player.name} swang and missed!')
                    if baddy_hit == True:
                        player.stunned = True
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
                        points += damage
                        baddy.hp -= damage
                        print(f'{player.name} did {damage} points of damage to the {baddy.name} with their {player.weapons[0]}')
                        print(f'{baddy.name} tried to evade and failed!')
                        if baddy.hp <= 0:
                            print(f'{player.name} killed the {baddy.name}!')
                    else:
                        print(f'{baddy.name} stumbled trying to evade but {player.name} was startled by a shiny coin and missed anyway!')       

            elif player_act == 'cast spell' and baddy_act == 'attack':
                print(player_act)
                print(baddy_act + "\n")
                player_hit = cast_roll(player.spell_mod, baddy.armor)
                if player_hit == True: #Checks if player hit successfully and deals damage if true
                    points += 2
                    baddy.stunned = True
                    print(f'{player.name} cast {player.spells[0]} and stunned the{baddy.name}')
                else:
                    print(f'{player.name} cast {player.spells[0]} but the {baddy.name} resisted!')
                    baddy_hit = attack_roll(baddy.atk_mod, player.armor)
                    if baddy_hit == True:
                        damage = damage_roll(baddy.weapons)
                        player.hp -= damage
                        print(f'The {baddy.name} did {damage} points of damage to {player.name} with their {baddy.weapons[0]}\n')
                        if player.hp <= 0:
                            print(f'{player.name} died. They were killed by a {baddy.name} with only {baddy.hp}hp left.')
                            break
                    else:
                        print(f'The {baddy.name} swang and missed!')

            elif player_act == 'cast spell' and baddy_act == 'cast spell':
                print(player_act)
                print(baddy_act + "\n")
                player_hit = cast_roll(player.spell_mod, baddy.armor)
                baddy_hit = cast_roll(baddy.spell_mod, player.armor)
                if player_hit == True: #Checks if player hit successfully and deals damage if true
                    points += 2
                    baddy.stunned = True
                    print(f'{player.name} cast {player.spells[0]} and stunned {baddy.name}')
                else:
                    print(f'{player.name} cast {player.spells[0]} but the {baddy.name} resisted!')
                    if baddy_hit == True:
                        player.stunned = True
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
                        points += 2
                        baddy.stunned = True
                        print(f'{player.name} cast {player.spells[0]} and stunned the {baddy.name}\n')
                    else:
                        print(f'{player.name} cast {player.spells[0]} but the {baddy.name} attempted to evade and resisted!\n')      

            elif player_act == 'evade' and baddy_act == 'attack':
                print(player_act)
                print(baddy_act + "\n")
                player.dodged = evade(player.dex_mod, baddy.dex_mod) 
                if player.dodged == True: #Checks if player evades successfully and skips baddy attack if true
                    points += 1
                    print(f'{player.name} dodged the {baddy.name}\'s attack!\n')
                else:
                    baddy_hit = attack_roll(baddy.atk_mod, player.armor)
                    if baddy_hit == True: #Checks if baddy hit successfully and deals damage if true
                        damage = damage_roll(baddy.weapons)
                        player.hp -= damage
                        print(f'{baddy.name} did {damage} points of damage to {player.name} with their {baddy.weapons[0]}\n')
                        if player.hp <= 0:
                            print(f'{player.name} died. They were killed by a {baddy.name} with only {baddy.hp}hp left.')
                            break
                    else:
                        print(f'The {baddy.name} swang and missed!\n')
            
            elif player_act == 'evade' and baddy_act == 'cast spell':
                print(player_act)
                print(baddy_act + "\n")
                player.dodged = evade(player.dex_mod, baddy.dex_mod) 
                if player.dodged == True: #Checks if player evades successfully and skips baddy attack if true
                    points += 1
                    print(f'The {player.name} dodged the {baddy.name}\'s attack!\n')
                else:
                    baddy_hit = cast_roll(baddy.spell_mod, player.armor)
                    if baddy_hit == True:
                        player.stunned = True
                        print(f'The {baddy.name} cast {baddy.spells[0]} and stunned {player.name}\n')
                    else:
                        print(f'The {baddy.name} cast {baddy.spells[0]} but {player.name} resisted!\n')

            elif player_act == 'evade' and baddy_act == 'evade':
                print(player_act)
                print(baddy_act + "\n")
                print('\nYou both dodged!\n')
            
            elif player_act == 'stunned':
                if baddy_act == 'attack':
                    baddy_hit = attack_roll(baddy.atk_mod, player.armor-5)
                    if baddy_hit == True: #Checks if baddy hit successfully and deals damage if true
                        damage = damage_roll(baddy.weapons)
                        player.hp -= damage
                        print(f'{baddy.name} did {damage} points of damage to {player.name}\n')
                        if player.hp <= 0:
                            print(f'{player.name} died. They were killed by a {baddy.name} with only {baddy.hp}hp left.')
                            break
                    else:
                        print(f'The {baddy.name} swang and missed!\n')
                
                elif baddy_act == 'cast spell':
                    baddy_hit = cast_roll(baddy.spell_mod, player.armor-5)
                    if baddy_hit == True:
                        player.stunned = True
                        print(f'The {baddy.name} cast {baddy.spells[0]} and stunned {player.name} again!\n')
                    else:
                        print(f'The {baddy.name} tried to stun {player.name} again but failed miserably!\n')
                
                elif baddy_act == 'evade':
                    print(f'The stupid {baddy.name} just tried to evade it\'s stunned opponent... What a dumb dumb!')

            elif baddy_act == 'stunned':
                print(f'{baddy.name} is still stunned!')
                if player_act == 'attack':
                    player_hit = attack_roll(player.atk_mod, baddy.armor-5)
                    if player_hit == True: #Checks if player hit successfully and deals damage if true
                        damage =  damage_roll(player.weapons)
                        baddy.hp -= damage
                        print(f'{player.name} did {damage} points of damage to the {baddy.name}')
                        if baddy.hp <= 0:
                            print(f'{player.name} killed the {baddy.name}!')
                    else:
                        print(f'{player.name} swang and missed!')
                
                elif player_act == 'cast_spell':
                    player_hit = cast_roll(player.spell_mod, baddy.armor-5)
                    if player_hit == True: #Checks if player hit successfully and deals damage if true
                        baddy.stunned = True
                        print(f'{player.name} stunned the {baddy.name} again')
                    else:
                        print(f'{player.name} tried to stun {baddy.name} but failed!')

                elif player_act == 'evade':
                    print(f'For some reason {player.name} tried to evade the {baddy.name} even though it was stunned...\n That\'s a bit of a head scratcher...')

            elif player_act == 'quit' or 'Quit':
                exit()

        if player.hp > 0 and baddy.name != 'Bugbear':
            points += 5

            print(f'\nCongratulations! You made it past that {baddy.name}. Now you get a special bonus...\nYou can have a health pack to increase your hp by 10 or you can have a stat boost to increase one of your stats by 3')
            while True:
                bonus = input('''So what\'ll it be 'Stat' or 'Health'? ''').lower()
                if bonus == 'stat':
                    stat = input('''\nOK, which one? 'Attack', 'Spell', or 'Dex'? ''').lower()
                    if stat == 'attack':
                        player.atk_mod +=3
                        print(f'Your Attack is now {player.atk_mod}')
                        break
                    elif stat == 'spell':
                        player.spell_mod +=3
                        print(f'Your Spell attack is now {player.spell_mod}')
                        break
                    elif stat == 'dex':
                        player.dex_mod +=3
                        print(f'Your Dex is now {player.dex_mod}')
                        break
                    else:
                        print('''Let's try that again...''')
                elif bonus == 'health':
                    player.hp += 10
                    print(f'Your hp is now {player.hp}')
                    break
                
                else:
                    print('''Let's try that again...''')
        elif player.hp > 0 and baddy.name == 'Bugbear':
            points += points
            print(f'Congratulations {player.name}! You beat all the dastardly bad guys this arena had to offer!\n\nYOU WON!\n\n')
            break
        else:
            print(f'You died but congrats on getting this far.\nScore: {points}')
            break
    return points



        
high_scores = Score_Card.load_high_scores()
Score_Card.print_scores()       

name = input('Greetings friend! What is your name? ')

print(f'''\nIt\'s good to have you here {name}.
I hope you put on your fighting pants today...\n''')

while True:
    knows_classes = input(f'''Do you know what fighting class you want to pick?(yes/no):''').lower()
    if knows_classes in ['yes', 'no']:
        break
    else:
        print('Well... Do you know or not?')

if knows_classes.lower() == 'yes':
        chosen_class = input('\nGreat! Good and ready for the grinder I see. The spectators in the arena will love that! \nSo which one: ').lower()
elif knows_classes.lower() == 'no':
        chosen_class = input(f'''\nOk then, let's see... 
The three fighting styles we allow are:
    Monk:
        {monk.hp} hp
        {monk.armor} armor
        + {monk.atk_mod} Attack
        + {monk.spell_mod} Spell Casting
        + {monk.dex_mod} Dexterity
        Uses {monk.weapons[0]} to do {monk.weapons[3]} + {monk.weapons[2]}
        Uses {monk.spells[0]} to stun
        
    Paladin:
        {paladin.hp} hp
        {paladin.armor} armor
        + {paladin.atk_mod} Attack
        + {paladin.spell_mod} Spell Casting
        + {paladin.dex_mod} Dexterity
        Uses {paladin.weapons[0]} to do {paladin.weapons[3]} + {paladin.weapons[2]}
        Uses {paladin.spells[0]} to stun
        
    Barbarian:
        {barbarian.hp} hp
        {barbarian.armor} armor
        + {barbarian.atk_mod} Attack
        + {barbarian.spell_mod} Spell Casting
        + {barbarian.dex_mod} Dexterity
        Uses {barbarian.weapons[0]} to do {barbarian.weapons[3]} + {barbarian.weapons[2]}
        Uses {barbarian.spells[0]} to stun
        \nWhat's your style: ''').lower()
else:
        print('Well... Do you know or not?')

while True:
    if chosen_class == "monk":
        player = Monk(name, chosen_class.capitalize())
        break
    elif chosen_class == "paladin":
        player = Paladin(name, chosen_class.capitalize())
        break
    elif chosen_class == "barbarian":
        player = Barbarian(name, chosen_class.capitalize())
        break
    else:
        chosen_class = input('So... What style? ').lower()

print(f'\nOk, {player.name} it\'s time to send you into the arena. \n{player}... That sounds pretty good I reckon.\nI\'m sure you\'ll do fine')

print(f'''\n{player.name} is a {player.chosen_class}
Their stats are:
    {player.atk_mod} Attack Mod
    {player.spell_mod} Spell Mod
    {player.dex_mod} Dexterity Mod
    \n''')

score = combat()

Score_Card.update_high_scores([player.name,score])