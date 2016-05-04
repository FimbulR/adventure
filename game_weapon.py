#game_weapon.py
import random as rnd

class WeaponObject():
    wpn_name = ""
    wpn_type = ""
    wpn_desc = ""
    wpn_hand = 1
    wpn_damage = [0,1]

    def __init__(self):
        return

# end class WeaponObject

class Fist(WeaponObject):
    wpn_name = "Fist"
    wpn_type = ""
    wpn_desc = "Only the brave or the fool fights with bare hands"
    wpn_hand = 1
    wpn_damage = [1,1]
# end class Fist

class UglyStick(WeaponObject):
    wpn_name = "UglyStick"
    wpn_type = ""
    wpn_desc = "Goblins weapon of choice"
    wpn_hand = 2
    wpn_damage = [0,2]
# end class Fist
