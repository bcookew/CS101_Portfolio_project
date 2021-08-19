from hst import Score_Card
from Player_classes import Monk, Paladin, Barbarian

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




#score = int(input('What was your whole number score? '))

#Score_Card.update_high_scores([name, score])
print('\n')

