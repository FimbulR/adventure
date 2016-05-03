#game_funcs.py
import re

def talk(who, speech):
    print('{0}> {1}'.format(who, speech))
    return

def catch_verb(verb, speech):
    match = re.search(verb, speech.lower())
    if match:
        return True
    else:
        return False

def examine(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_desc()
    else:
        return "There is no {} here.".format(noun)

def say(noun):
    return 'You said "{}"'.format(noun)

def help():
    #sarà un resoconto della situazionea del gioco
    help_str = ""
    li = list(verb_dict.keys())
    print(max(li))
    for verb_word in verb_dict:
        help_str += " {}\t\t\t{}\n".format(verb_word, verb_dict[verb_word][1])
    return help_str
