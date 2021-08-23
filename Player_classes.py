from dice import *


weapons = {'Knuckles':2, 'Sword':5, 'Two-Handed Axe':10}
spells = {'Fireball': 5, 'Spirit Bomb': 10, 'Shriek': 3}


class Player:
    def __init__(self, name, chosen_class, atk_mod, spell_mod, dex_mod):
        self.name = name
        self.chosen_class = chosen_class
        self.atk_mod = atk_mod
        self.spell_mod = spell_mod
        self.dex_mod = dex_mod
        self.dodged = False
        self.stunned = False
        self.slowed = False

    def __repr__(self):
        return f'{self.name} the {self.chosen_class}'

    def attack(self, weapon, enemy_armor, enemy_health):
        if (self.atk_mod + d20() >= enemy_armor):
            return (enemy_health - (d6() + weapon[1]))
        else:
            return enemy_health
    
    def use_spell(self, spell, enemy_type):
        if (self.spell_mod + d20() >= enemy_type.spell_mod + d20()):
            return (self.spell_mod + spells[spell])
        else:
            return 0

    def evade(self, enemy_dex):
        if (self.dex_mod + d20()) > (enemy_dex + d20()):
            return True
        else:
            return False


class Monk(Player):
    def __init__(self, name, chosen_class):
        self.hp = 10
        self.armor = 16
        self.atk_mod = 6
        self.spell_mod = 0
        self.dex_mod = 10
        self.weapons = ['Brass Knuckles', d4, 3, '1d4']
        self.spells = ['Vulcan Nerve Pinch']
        super().__init__(name, chosen_class, self.atk_mod, self.spell_mod, self.dex_mod)

class Paladin(Player):
    def __init__(self, name, chosen_class):
        self.hp = 7
        self.armor = 18
        self.atk_mod = 7
        self.spell_mod = 7
        self.dex_mod = 0
        self.weapons = ['Claymore', d12, 6, '1d12']
        self.spells = ['Divine Prison']
        super().__init__(name, chosen_class, self.atk_mod, self.spell_mod, self.dex_mod)

class Barbarian(Player):
    def __init__(self, name, chosen_class):
        self.hp = 15
        self.armor = 12
        self.atk_mod = 10
        self.spell_mod = 5
        self.dex_mod = 5
        self.weapons = ['Bare Hands', d6, 4, '1d6']
        self.spells = ['Headbutt']
        super().__init__(name, chosen_class, self.atk_mod, self.spell_mod, self.dex_mod)
