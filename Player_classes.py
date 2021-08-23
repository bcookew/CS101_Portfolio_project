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
        

    def __repr__(self):
        return f'{self.name} the {self.chosen_class}'


class Monk(Player):
    def __init__(self, name, chosen_class):
        self.hp = 10
        self.armor = 16
        self.atk_mod = 7
        self.spell_mod = 4
        self.dex_mod = 6
        self.weapons = ['brass knuckles', d4, 4, '1d4']
        self.spells = ['Vulcan Nerve Pinch']
        super().__init__(name, chosen_class, self.atk_mod, self.spell_mod, self.dex_mod)

class Paladin(Player):
    def __init__(self, name, chosen_class):
        self.hp = 7
        self.armor = 18
        self.atk_mod = 7
        self.spell_mod = 7
        self.dex_mod = 3
        self.weapons = ['claymore', d12, 6, '1d12']
        self.spells = ['Divine Prison']
        super().__init__(name, chosen_class, self.atk_mod, self.spell_mod, self.dex_mod)

class Barbarian(Player):
    def __init__(self, name, chosen_class):
        self.hp = 15
        self.armor = 14
        self.atk_mod = 8
        self.spell_mod = 4
        self.dex_mod = 5
        self.weapons = ['bare hands', d6, 4, '1d6']
        self.spells = ['Headbutt']
        super().__init__(name, chosen_class, self.atk_mod, self.spell_mod, self.dex_mod)
