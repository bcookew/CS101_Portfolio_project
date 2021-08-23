from dice import *

def attack_roll(attacker, defender):
        if (attacker + d20() >= defender):
            return True
        else:
            return False

def cast_roll(caster, defender):
        if (caster + d20() >= defender):
            return True
        else:
            return False

def evade(evader, attacker):
        if (evader + d20()) > (attacker + d20()):
            return True
        else:
            return False


def damage_roll(weapon):
    return weapon[1]() + weapon[2]
