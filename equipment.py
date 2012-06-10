import itemlist
import random

class Item:
    def __init__(self, name, weight, goldValue):
        self.name       = name
        self.weight     = weight
        self.goldValue  = goldValue

class Equippable(Item):
    def __init__(self, name, weight, type, goldValue):
        Item.__init__(self, name, weight, goldValue)
        self.type   = type

class Weapon(Equippable):
    def __init__(self, name, weight, type, goldValue, wepMin, wepMax, wepCrit, wepCritDmg, wepRange):
        Equippable.__init__(self, name, weight, type, goldValue)
        self.min     = wepMin
        self.max     = wepMax
        self.crit    = wepCrit
        self.critDmg = wepCritDmg
        self.range   = wepRange

class Shield(Equippable):
    def __init__(self, name, weight, type, goldValue, blockValue):
        Equippable.__init__(self, name, weight, type, goldValue)
        self.blockValue  = blockValue
        self.blockChance = 4             #base 40% block chance

class Armor(Equippable):
     def __init__(self, name, weight, type, goldValue, armorClass):
         Equippable.__init__(self, name, weight, type, goldValue)
         self.armorClass = armorClass

def itemDict(itemlist):
    itemDict = {}
    for item in itemlist:
        itemDict[item[0]] = item
    return itemDict
        
def createWeapon(weaponChoice): #getting weapon properties out of the itemlist
    name         = weaponList[weaponChoice][0]
    goldValue    = weaponList[weaponChoice][1]
    wepMin       = weaponList[weaponChoice][2]
    wepMax       = weaponList[weaponChoice][3]
    wepCrit      = weaponList[weaponChoice][4]
    wepCritDmg   = weaponList[weaponChoice][5]
    wepRange     = weaponList[weaponChoice][6]
    weight       = weaponList[weaponChoice][7]
    type         = weaponList[weaponChoice][8]
    return Weapon(name, weight, type, goldValue, wepMin, wepMax, wepCrit, wepCritDmg, wepRange)

def createArmor(armorChoice): #getting armor properties out of the itemlist
    name        = armorList[armorChoice][0]
    goldValue   = armorList[armorChoice][1]
    armorClass  = armorList[armorChoice][2]
    weight      = armorList[armorChoice][3]
    type        = armorList[armorChoice][4]
    return Armor(name, weight, type, goldValue, armorClass)

def createShield(shieldChoice): #getting shield properties out of the itemlist
    name        = shieldList[shieldChoice][0]
    goldValue   = shieldList[shieldChoice][1]
    blockValue  = shieldList[shieldChoice][2]
    weight      = shieldList[shieldChoice][3]
    type        = shieldList[shieldChoice][4]
    return Shield(name, weight, type, goldValue, blockValue)

weaponList = itemDict(itemlist.weapon_list)
armorList = itemDict(itemlist.armor_list)
shieldList = itemDict(itemlist.shield_list)
