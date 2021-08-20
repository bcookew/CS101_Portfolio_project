from Player_classes import rand_mod, damage_roll

class Enemy:
    def __init__(self, name, atk_mod, spell_mod, dex_mod):
        self.name = name
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
    
    def use_spell(self, spell, player):
        if (self.spell_mod + rand_mod() >= player.spell_mod + rand_mod()):
            return (self.spell_mod + self.spells[spell])
        else:
            return 0

    def evade(self, player):
        if (self.dex_mod + rand_mod()) > (player.dex_mod + rand_mod()):
            return True
        else:
            return False


class Goblin(Enemy):
    def __init__(self):
        self.name = 'Goblin'
        self.hp = 10
        self.armor = 15
        self.atk_mod = 4
        self.spell_mod = 0
        self.dex_mod = 6
        self.weapons = ['Scimitar',4]
        self.spells = None
        super().__init__(self.name, self.atk_mod, self.spell_mod, self.dex_mod)

class Lizardfolk(Enemy):
    def __init__(self):
        self.name = 'Lizardfolk'
        self.hp = 15
        self.armor = 16
        self.atk_mod = 7
        self.spell_mod = 7
        self.dex_mod = 0
        self.weapons = {'Bite':4, 'Heavy Club':4}
        self.spells = None
        super().__init__(self.name, self.atk_mod, self.spell_mod, self.dex_mod)

class Bugbear(Enemy):
    def __init__(self):
        self.name = 'Bugbear'
        self.hp = 27
        self.armor = 16
        self.atk_mod = 10
        self.spell_mod = 5
        self.dex_mod = 5
        self.weapons = {'Knuckles':2, 'Sword':5, 'Two-Handed Axe':10}
        self.spells = {'Fireball': 5, 'Spirit Bomb': 10, 'Shriek': 3}
        super().__init__(self.name, self.atk_mod, self.spell_mod, self.dex_mod)