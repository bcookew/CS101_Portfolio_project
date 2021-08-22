from dice import *



class Enemy:
    def __init__(self, name, atk_mod, spell_mod, dex_mod):
        self.name = name
        self.atk_mod = atk_mod
        self.spell_mod = spell_mod
        self.dex_mod = dex_mod
        self.dodged = False
        self.stunned = False
        self.slowed = False

    def __repr__(self):
        return f'{self.name} the {self.chosen_class}'

    def attack(self, weapon, enemy_armor, enemy_health, enemy_dodged):
        if enemy_dodged == True:
            print('You dodged the attack!')
            return False, enemy_health
        else:
            if (self.atk_mod + d20() >= enemy_armor):
                damage = d6() + weapon[1]
                print(f"{self.name} hit you for {damage} points of damage!")
                return False, enemy_health - damage
            else:
                print(f"The {self.name} missed you!")
                return False, enemy_health
    
    def use_spell(self, spell, player):
        if (self.spell_mod + d20() >= player.spell_mod + d20()):
            return (self.spell_mod + self.spells[spell])
        else:
            return 0

    def evade(self, player):
        if (self.dex_mod + d20()) > (player.dex_mod + d20()):
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
        self.weapons = ['Scimitar', d6, 4]
        self.spells = ['Frost']
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