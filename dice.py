import random

#functions for dice rolling

def d20():
    random.seed(random.randint(1,1000000))
    return random.randint(1, 20)

def d12():
    random.seed(random.randint(1,1000000))
    return random.randint(1, 12)

def d10():
    random.seed(random.randint(1,1000000))
    return random.randint(1, 10)

def d8():
    random.seed(random.randint(1,1000000))
    return random.randint(1, 8)

def d6():
    random.seed(random.randint(1,1000000))
    return random.randint(1, 6)

def d4():
    random.seed(random.randint(1,1000000))
    return random.randint(1, 4)


#function determines enemy action every round
def baddy_action():
    random.seed(random.randint(1,1000000))
    action = random.randint(1,10)
    if action in range(1,5):
        return "attack"
    elif action in range(5,8):
        return "cast spell"
    elif action in range(8,11):
        return "evade"

#checks attacker d20 + atk_mod vs enemy armor
def attack_roll(attacker, defender):
        if (attacker + d20() >= defender):
            return True
        else:
            return False

#checks attacker d20 + spell_mod vs enemy armor
def cast_roll(caster, defender):
        if (caster + d20() >= defender):
            return True
        else:
            return False

#checks attacker d20 + dex_mod vs enemy armor
def evade(evader, attacker):
        if (evader + d20()) > (attacker + d20()):
            return True
        else:
            return False

#calls die roll listed in weapons for class and adds weapon bonus
def damage_roll(weapon):
    return weapon[1]() + weapon[2]
