import random

def rand_mod():
    return random.randint(1, 20)

weapons = {'Knuckles':2, 'Sword':5, 'Two-Handed Axe':10}
spells = {'Fireball': 5, 'Spirit Bomb': 10, 'Shriek': 3}

def damage_roll():
    return random.randint(1,6)

class Player:
    def __init__(self, name, chosen_class, atk_mod, spell_mod, dex_mod):
        self.name = name
        self.chosen_class = chosen_class
        self.atk_mod = atk_mod
        self.spell_mod = spell_mod
        self.dex_mod = dex_mod

    def __repr__(self):
        return f'{self.name} the {self.chosen_class}'

    def attack(self, weapon, enemy_armor, enemy_health):
        if (self.atk_mod + rand_mod() >= enemy_armor + rand_mod()):
            return (enemy_health - (damage_roll() + weapon[1]))
        else:
            return enemy_health
    
    def use_spell(self, spell, enemy_type):
        if (self.spell_mod + rand_mod() >= enemy_type.spell_mod + rand_mod()):
            return (self.spell_mod + spells[spell])
        else:
            return 0

    def evade(self, enemy_type):
        if (self.dex_mod + rand_mod()) > (enemy_type.dex_mod + rand_mod()):
            return True
        else:
            return False


class Monk(Player):
    def __init__(self, name, chosen_class):
        self.hp = 10
        self.armor = 15
        self.atk_mod = 6
        self.spell_mod = 0
        self.dex_mod = 10
        self.weapons = ['Brass Knuckles', 3]
        super().__init__(name, chosen_class, self.atk_mod, self.spell_mod, self.dex_mod)

class Paladin(Player):
    def __init__(self, name, chosen_class):
        self.hp = 7
        self.armor = 15
        self.atk_mod = 7
        self.spell_mod = 7
        self.dex_mod = 0
        super().__init__(name, chosen_class, self.atk_mod, self.spell_mod, self.dex_mod)

class Barbarian(Player):
    def __init__(self, name, chosen_class):
        self.hp = 7
        self.armor = 15
        self.atk_mod = 10
        self.spell_mod = 5
        self.dex_mod = 5
        super().__init__(name, chosen_class, self.atk_mod, self.spell_mod, self.dex_mod)
