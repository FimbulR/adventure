#game_objects.py
import simplejson as json
import random as rnd
import game_weapon as wpn
import os

save_file_path = "__save__\game.json"
hit_threshold = 65

class GameObject():
    objects = {}

    def __init__(self):
        return

    def add_obj(self, name, obj):
        self.objects[name] = obj
        return

    def del_obj(self, name):
        if name in self.objects: del self.objects[name]
        return

    def save_game(self):
        if not os.path.exists("__save__"):
            os.makedirs("__save__")

        save_file = open(save_file_path, "w")
        data = {
            "name": self.objects["hero_name"],
            "class": self.objects["hero_class"],
        }
        game_content = json.dumps(data, sort_keys=True, indent=4 * ' ')
        save_file.write(game_content)
        save_file.close()
        return

    def load_game(self):
        save_file = open(save_file_path, "r")
        file_read = save_file.read()
        game_content = json.loads(file_read)
        save_file.close()
        return game_content

    def attack(self, target):
        if target in self.objects:
            atk_init = rnd.randint(0, 10)
            if(atk_init > 6):
                print('*** You attack first!')
                self.__attack_monster(target)
                self.__attack_hero(target)
            else:
                print('*** Your enemy attacks first!')
                self.__attack_hero(target)
                self.__attack_monster(target)
        else:
            print('*** nothing to attack')

    def __attack_monster(self, target):
        hero = self.objects["hero"]
        monster = self.objects[target]
        print('*** {0} attacks {1}'.format(hero.name, monster.name))
        attr_agility = hero.attr_agility
        chance = rnd.randint(0, 99) + attr_agility
        if (chance > 49):
            attr_strength = hero.attr_strength
            weapon = hero.get_equip("weapon1")
            wpn_damage = rnd.randint(weapon.wpn_damage[0], weapon.wpn_damage[1])
            chance = rnd.randint(0, 99) + attr_agility
            if(chance < 20):
                crit_mod = 0.5
            elif (chance > 100):
                crit_mod = 2
            else:
                crit_mod = 1
            damage = int((attr_strength + wpn_damage) * crit_mod)
            print('    {0} damage'.format(damage))
            monster.suffer_attack(damage)
            if(monster.get_life() < 0):
                print('    {0}\'s been defeated!'.format(monster.name))
                if target in self.objects: del self.objects[target]
            else:
                print('    {0} has {1} life points left'.format(monster.name, monster.get_life()))
        else:
            print('    attack missed')

    def __attack_hero(self, target):
        hero = self.objects["hero"]
        monster = self.objects[target]
        print('*** {0} attacks {1}'.format(monster.name, hero.name))
        attr_agility = monster.attr_agility
        chance = rnd.randint(0, 99) + attr_agility
        if (chance > 49):
            attr_strength = monster.attr_strength
            weapon = monster.get_equip("weapon1")
            wpn_damage = rnd.randint(weapon.wpn_damage[0], weapon.wpn_damage[1])
            chance = rnd.randint(0, 99) + attr_agility
            if(chance < 20):
                crit_mod = 0.5
            elif (chance > 100):
                crit_mod = 2
            else:
                crit_mod = 1
            damage = int((attr_strength + wpn_damage) * crit_mod)
            print('    {0} damage'.format(damage))
            hero.suffer_attack(damage)
            if(hero.get_life() < 0):
                print('    You\'ve been defeated!')
                #if target in self.objects: del self.objects[target]
            else:
                print('    You have {0} life points left'.format(hero.get_life()))
        else:
            print('    attack missed')
# end class GameObject

class CharacterObject:
    name = ""
    race = ""
    profession = ""
    level = 1
    exp = 0
    life = 100
    attr_constitution = 10
    attr_strength = 10
    attr_agility = 10
    attr_defense = 10
    attr_mana = 10
    attr_intellect = 10
    aattr_will = 0
    sattr_luck = 0
    sattr_speed = 0
    movement = 100
    desc = ""
    equip = {
        "head" : None,
        "shoulder" : None,
        "chest" : None,
        "hands" : None,
        "legs" : None,
        "feet" : None,
        "weapon1" : None,
        "weapon2" : None,
        "amulet" : None,
        "back" : None,
    }
    inventory = {}

    def __init__(self, name = ""):
        self.name = name
        return

    def get_dump(self):
        return

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def descr(self):
        return {'Class': self.profession, 'Description': self.desc}

    def get_life(self):
        return self.life

    def set_equip(self, slot, piece):
        self.equip[slot] = piece

    def get_equip(self, slot):
        return self.equip[slot]

    def suffer_attack(self, attack):
        self.life -= int(attack)
        return
# end class CharacterObject

class WarriorObject(CharacterObject):
    race = "Human"
    profession = "Warrior"
    desc = "A fierce fighter proficient in armed close combat"
    life = 100
    attr_constitution = 10
    attr_strength = 16
    attr_agility = 10
    attr_defense = 14
    attr_mana = 6
    attr_intellect = 4
# end class WarriorObject

class MageObject(CharacterObject):
    race = "Human"
    profession = "Mage"
    desc = "A wise scholar proficient in handling natural elements"
    life = 100
    attr_constitution = 10
    attr_strength = 5
    attr_agility = 8
    attr_defense = 4
    attr_mana = 17
    attr_intellect = 16
# end class MageObject

class ThiefObject(CharacterObject):
    race = "Human"
    profession = "Thief"
    desc = "A cunning scoundrel proficient in stealth movement"
    life = 100
    attr_constitution = 10
    attr_strength = 7
    attr_agility = 12
    attr_defense = 12
    attr_mana = 8
    attr_intellect = 6
# end class ThiefObject

class GoblinObject(CharacterObject):
    race = "Goblin"
    profession = "Thug"
    desc = "A foul creature"
    life = 50
    attr_constitution = 10
    attr_strength = 10
    attr_agility = 10
    attr_defense = 10
    attr_mana = 5
    attr_intellect = 5
# end class Goblin
