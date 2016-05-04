#game.py
import onoff
import os
import re
import simplejson as json
import time
import game_funcs as func
import game_objects as obj
import game_weapon as wpn

game_objects = obj.GameObject()
master_name = "Mysterious Guy"
hero = ""
hero_name = "Nameless Hero"

verb_dict = {
    "help": (func.help, "help descr"),
    "save": (game_objects.save_game, "save descr"),
    "load": (game_objects.load_game, "load descr"),
    "attack": (game_objects.attack, "attack descr"),
    "say": (func.say, "say descr"),
    "examine": (func.examine, "examine descr"),
}

def get_input(user_input):
  command = user_input.split()
  verb_word = command[0]
  if verb_word in verb_dict:
    verb = verb_dict[verb_word][0]
  else:
    print("Unknown verb {}". format(verb_word))
    return
  if len(command) >= 2:
    noun_word = command[1]
    verb(noun_word)
  else:
    verb()


class Foo(onoff.OnOffMixin):
    def __init__(self):
        self.on("hello", self.hello)

    def hello(self, *args):
        print("Hello: %s" % args)

    def test(self, *args):
        self.trigger("hello", *args)

f = Foo()
f.hello("hello events rock!")
f.test("test events rock!")

print(".....-----'''''-----.....-----'''''-----.....-----'''''-----.....")
if os.path.isfile(obj.save_file_path):
    print("Type [new] to start a new game \nType [load] to resume your last game!")
    print("When you start a new game every other save will be overwritten! Be careful!")
    input_game_type = input("> ")
else:
    print("Hi! You will be redirected soon to the game!")
    time.sleep(2)
    input_game_type = "new"
print(".....-----'''''-----.....-----'''''-----.....-----'''''-----.....")
if(input_game_type == "new"):
    func.talk(master_name, "Welcome to a new Adventure!")
    func.talk(master_name, "Are you ready to begin your journey?")
    input_ready = input("{0}> ".format(hero_name))
    if(func.catch_verb(r"yes", input_ready)):
        func.talk(master_name,'I am happy to hear that!')
        func.talk(master_name,'Now tell me. Are you a boy? Or are you a girl?')
        print("{0}> ...".format(hero_name))
        time.sleep(2)
        func.talk(master_name,'Hahaha! I am just joking!')
        func.talk(master_name,'Are you a warrior? Or are you a mage? Or are you a thief?')
        while True:
            input_class = input("{0}> ".format(hero_name))
            if(func.catch_verb(r"warrior", input_class)):
                hero = obj.WarriorObject()
                break
            elif(func.catch_verb(r"mage", input_class)):
                hero = obj.MageObject()
                break
            elif(func.catch_verb(r"thief", input_class)):
                hero = obj.ThiefObject()
                break
            else:
                func.talk(master_name, 'What?! Are you a warrior, a mage or a thief?')
        func.talk(master_name,'A {0} right?'.format(hero.descr()['Class'].lower()))
        func.talk(master_name,'{0}!'.format(hero.descr()['Description']))
        func.talk(master_name,'I have one last question. What is your name?')
        input_name = input("{0}> ".format(hero_name))
        hero_name = input_name.title()
        hero.set_name(hero_name)
        hero.set_equip("weapon1", wpn.Fist())
        game_objects.add_obj("hero", hero)
        game_objects.add_obj("hero_name", hero_name)
        game_objects.add_obj("hero_class", hero.descr()['Class'].lower())
        game_objects.save_game()
        time.sleep(1)
        func.talk(master_name,'Nice to meet you {0}! Let\'s begin our journey!'.format(hero.get_name()))
        #START TUTORIAL
        func.talk(master_name,'Whooooooaaah! What is that disgusting creature??!')
        tutorial_monster = obj.GoblinObject("Gnakt")
        tutorial_monster.set_equip("weapon1", wpn.UglyStick)
        func.talk(tutorial_monster.get_name(), 'Gnakt! Gnakt!!')
        time.sleep(1)
        func.talk(master_name,'Alas! Defeat that Goblin...')
        game_objects.add_obj("Gnakt", tutorial_monster)
        #END TUTORIAL
        while True:
            user_input = input("{0}> ".format(hero_name))
            if(user_input.lower() == "exit"):
                func.talk(master_name,'Well then. Goodbye Adventurer!')
                break
            else:
                get_input(user_input)




    elif(ready.lower() == "no"):
        func.talk(master_name,'Well then. Goodbye coward!')
    else:
        func.talk(master_name,'What?!... Goodbye you fool!')
elif(input_game_type == "load"):
    game_objects = game_objects.load_game()
    if(game_objects["hero_class"] == "warrior"):
        hero = obj.WarriorObject()
    elif(game_objects["hero_class"] == "mage"):
        hero = obj.MageObject()
    elif(game_objects["hero_class"] == "thief"):
        hero = obj.ThiefObject()
    hero_name = game_objects["hero_name"]
    hero.create(hero_name)
    func.talk(master_name,'Hello {0}! Welcome back!'.format(hero_name))
    while True:
        user_input = input("{0}> ".format(hero_name))
        if(user_input.lower() == "exit"):
            func.talk(master_name,'Well then. Goodbye Adventurer!')
            break
        else:
            get_input(user_input)
