#game_objects.py
import simplejson as json
import random as rnd
import game_weapon as wpn

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
            "hero_name": self.objects["hero_name"],
            "hero_class": self.objects["hero_class"],
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
        # a → b
        # b → a
        # o viceversa
        atk_init = rnd(0, 10)
        if(atk_init > 6):
            print('*** You attack first!')
            self.__attack_hero(self, target)
            self.__attack_monster(self, target)
        else:
            print('*** Your enemy attacks first!')
            self.__attack_monster(self, target)
            self.__attack_hero(self, target)

    def __attack_monster(self, target):
        if target in self.objects:
            hero = self.objects["hero"]
            monster = self.objects[target]
            print('*** {0} attacks {1}'.format(hero.hero_name, monster.monster_name))
            attr_agi = hero.hero_attr_agi
            chance = rnd.randint(0, 99) + attr_agi
            if (chance > 49):
                attr_str = hero.hero_attr_str
                wpn_damage = hero.equip["weapon1"].get_damage()
                chance = rnd.randint(0, 99) + attr_agi
                if(chance < 20):
                    crit_mod = 0.5
                elif (chance > 100):
                    crit_mod = 2
                else:
                    crit_mod = 1
                damage = int((attr_str + wpn_damage) * crit_mod)
                print('    {0} damage'.format(damage))
                monster.suffer_attack(damage)
                if(monster.get_life() < 0):
                    print('    {0}\'s been defeated!'.format(monster.monster_name))
                    if target in self.objects: del self.objects[target]
                else:
                    print('    {0} has {1} life points left'.format(monster.monster_name, monster.get_life()))
            else:
                print('    attack missed')
        else:
            print('*** nothing to attack')

    def __attack_hero(self, target):
        hero = self.objects["hero"]
        monster = self.objects[target]
        print('*** {0} attacks {1}'.format(monster.monster_name, hero.hero_name))
        attr_agi = hero.hero_attr_agi
        chance = rnd.randint(0, 99) + attr_agi
        if (chance > 49):
            attr_str = hero.hero_attr_str
            wpn_damage = hero.equip["weapon1"].get_damage()
            chance = rnd.randint(0, 99) + attr_agi
            if(chance < 20):
                crit_mod = 0.5
            elif (chance > 100):
                crit_mod = 2
            else:
                crit_mod = 1
            damage = int((attr_str + wpn_damage) * crit_mod)
            print('    {0} damage'.format(damage))
            monster.suffer_attack(damage)
            if(monster.get_life() < 0):
                print('    You\'ve been defeated!')
                if target in self.objects: del self.objects[target]
            else:
                print('    {0} has {1} life points left'.format(monster.monster_name, monster.get_life()))
        else:
            print('    attack missed')
# end class GameObject

class HeroObject:
    hero_name = ""
    hero_class = ""
    hero_race = "Human"
    hero_level = 1
    hero_exp = 0
    hero_life = 100
    hero_attr_man = 10 #mana
    hero_attr_str = 10 #strenght
    hero_attr_agi = 10 #agility
    hero_attr_def = 10 #defense
    hero_attr_mag = 10 #magic power
    hero_movement = 100
    hero_desc = ""
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

    def __init__(self):
        return

    def create(self, hero_name):
        self.hero_name = hero_name
        self.equip["weapon1"] = wpn.Fist()

    def get_dump(self):
        return

    def get_name(self):
        return self.hero_name

    def descr(self):
        return {'Class': self.hero_class, 'Description': self.hero_desc}

    def get_life(self):
        return self.hero_life

    def suffer_attack(self, attack):
        self.hero_life -= int(attack)
        return
# end class CharacterObject

class WarriorObject(HeroObject):
    hero_class = "Warrior"
    hero_desc = "A fierce fighter proficient in armed close combat"
    hero_life = 100
    hero_attr_man = 6 #mana
    hero_attr_str = 16 #strenght
    hero_attr_agi = 10 #agility
    hero_attr_def = 14 #defense
    hero_attr_mag = 4 #magic power
# end class WarriorObject

class MageObject(HeroObject):
    hero_class = "Mage"
    hero_desc = "A wise scholar proficient in handling natural elements"
    hero_life = 100
    hero_attr_man = 17 #mana
    hero_attr_str = 5 #strenght
    hero_attr_agi = 8 #agility
    hero_attr_def = 4 #defense
    hero_attr_mag = 16 #magic power
# end class MageObject

class ThiefObject(HeroObject):
    hero_class = "Thief"
    hero_desc = "A cunning scoundrel proficient in stealth movement"
    hero_life = 100
    hero_attr_man = 8 #mana
    hero_attr_str = 7 #strenght
    hero_attr_agi = 17 #agility
    hero_attr_def = 12 #defense
    hero_attr_mag = 6 #magic power
# end class ThiefObject

class MonsterObject:
    monster_name = ""
    monster_class = ""
    monster_race = ""
    monster_life = 100
    monster_attr = {
        "man" : 10, #mana
        "str" : 10, #strenght
        "agi" : 10, #agility
        "def" : 10, #defense
        "mag" : 10, #magic power
    }
    monster_movement = 100
    monster_desc = ""
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

    def __init__(self, monster_name):
        self.monster_name = monster_name
        self.equip["weapon1"] = wpn.UglyStick()
        return

    def get_name(self):
        return self.monster_name

    def descr(self):
        return {'Class': self.monster_class, 'Description': self.monster_desc}

    def get_life(self):
        return self.monster_life

    def suffer_attack(self, attack):
        self.monster_life -= int(attack)
        return
# end class MonsterObject

class GoblinObject(MonsterObject):
    monster_name = ""
    monster_race = "Goblin"
    monster_class = ""
    monster_desc = "A foul creature"
# end class Goblin
