import itemlist
import random

class Item:
    def __init__(self, name, weight, goldValue):
        self.name       = name
        self.weight     = weight
        self.goldValue  = goldValue

    def getName():
        return self.name

    def getWeight():
        return self.weight

    def getValue():
        return self.goldValue

class Equippable(Item):
    def __init__(self, name, weight, type, goldValue):
        Item.__init__(self, name, weight, goldValue)
        self.type   = type

    def getType():
        return self.type

class Weapon(Equippable):
    def __init__(self, name, weight, type, goldValue, wepMin, wepMax, wepCrit, wepCritDmg, wepRange):
        Equippable.__init__(self, name, weight, type, goldValue)
        self.wepMin     = wepMin
        self.wepMax     = wepMax
        self.wepCrit    = wepCrit
        self.wepCritDmg = wepCritDmg
        self.wepRange   = wepRange

class Shield(Equippable):
    def __init__(self, name, weight, type, goldValue, blockValue):
        Equippable.__init__(self, name, weight, type, goldValue)
        self.blockValue  = blockValue
        self.blockChance = 4             #base 40% block chance

class Armor(Equippable):
     def __init__(self, name, weight, type, goldValue, armorClass):
         Equippable.__init__(self, name, weight, type, goldValue)
         self.armorClass = armorClass
        
def chooseWeapon(weapon_list, weaponChoice): #getting weapon properties out of the itemlist
    name         = {}
    name         = itemlist.weapon_list[weaponChoice][0]
    goldValue    = itemlist.weapon_list[weaponChoice][1]
    wepMin       = itemlist.weapon_list[weaponChoice][2]
    wepMax       = itemlist.weapon_list[weaponChoice][3]
    wepCrit      = itemlist.weapon_list[weaponChoice][4]
    wepCritDmg   = itemlist.weapon_list[weaponChoice][5]
    wepRange     = itemlist.weapon_list[weaponChoice][6]
    weight       = itemlist.weapon_list[weaponChoice][7]
    type         = itemlist.weapon_list[weaponChoice][8]
    return name, weight, type, goldValue, wepMin, wepMax, wepCrit, wepCritDmg, wepRange 

def chooseArmor(armor_list, armorChoice): #getting armor properties out of the itemlist
    name        = {}
    name        = itemlist.armor_list[armorChoice][0]
    goldValue   = itemlist.armor_list[armorChoice][1]
    armorClass  = itemlist.armor_list[armorChoice][2]
    weight      = itemlist.armor_list[armorChoice][3]
    type        = itemlist.armor_list[armorChoice][4]
    return name, weight, type, goldValue, armorClass #armor type currently not implimented

def chooseShield(shield_list, shieldChoice): #getting shield properties out of the itemlist
    name = {}
    name        = itemlist.shield_list[shieldChoice][0]
    goldValue   = itemlist.shield_list[shieldChoice][1]
    blockValue  = itemlist.shield_list[shieldChoice][2]
    weight      = itemlist.shield_list[shieldChoice][3]
    type        = itemlist.shield_list[shieldChoice][4]
    return name, weight, type, goldValue, blockValue        
        
         
         
