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
        
        
        
        
         
         
