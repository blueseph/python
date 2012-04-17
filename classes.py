import equipment
import itemlist
import random

class Attributes:
    def __init__(self, unitclass, str, con, dex, wis, int, cun):
        self.unitclass  = unitclass
        self.str        = str
        self.con        = con
        self.dex        = dex
        self.wis        = wis
        self.int        = int
        self.cun        = cun

class Unit:
    def __init__(self, type):
        self.unitclass           = type.unitclass
        if self.unitclass is not 'berserker' and self.unitclass is not 'rogue' and self.unitclass is not 'warrior' and self.unitclass is not 'wizard':
            self.type       = 'monster'
        else:
            self.type       = 'player'
        self.str            = type.str
        self.con            = type.con
        self.dex            = type.dex
        self.wis            = type.wis
        self.int            = type.int
        self.cun            = type.cun
        self.maxhp          = self.con * 14
        self.curhp          = self.maxhp
        if self.dex > self.str:
            self.dmg        = self.dex//2.6
        else:
            self.dmg        = self.str//1.3
        self.mainhand       = None
        self.offhand        = None
        self.offhandWeight  = 0
        self.armorWeight    = 0

    def equip(self, item):
        if (item.type is '1h' or '2h') and (self.mainhand is None): #deletes currently equipped items. need to fix
            self.mainhand           = item.type
            self.mainhandWeaponName = item.name
            self.mainhandWeight     = item.weight
            self.mainhandGoldValue  = item.goldValue
            self.mainhandWepMin     = item.wepMin
            self.mainhandWepMax     = item.wepMax
            self.mainhandCrit       = item.wepCrit
            self.mainhandCritDmg    = item.wepCritDmg
            self.mainhandRange      = item.wepRange # need to impliment range
        elif self.mainhand is '1h' and item.type is '1h':
            self.offhand            = item.type
            self.offhandItemName    = item.name
            self.offhandWeight      = item.weight
            self.offhandGoldValue   = item.goldValue
            self.offhandWepMin      = item.wepMin
            self.offhandWepMax      = item.wepMax
            self.offhandCrit        = item.wepCrit
            self.offhandCritDmg     = item.wepCritDmg
            self.offhandRange       = item.wepRange
        elif item.type is 'shield':
            self.offhand            = item.type
            self.offhandItemName    = item.name
            self.offhandWeight      = item.weight
            self.offhandGoldValue   = item.goldValue
            self.offhandBlockValue  = item.blockValue
            self.offhandBlockChance = item.blockChance
        elif (item.type is not 'shield' or '1h' or '2h'):
            self.armorName          = item.name
            self.armorWeight        = item.weight
            self.armorGoldValue     = item.goldValue
            self.armorClass         = item.armorClass
#        elif (item.type is 'shield' and self.offhand is not None) or (item.type is '1h' and self.offhand is not None)
        self.weight = self.mainhandWeight + self.offhandWeight + self.armorWeight

def chooseClass():
    print('Choose your class')
    print(' ')
    print('''B: Berserker (STR, CON)
R: Rogue (DEX, CUN)
W: Warrior (CON, STR)
w: Wizard (INT, WIS)
''')
    playerClass = input()
    if playerClass.startswith('W'):
        playerClass = Warrior
        weapon = equipment.Weapon(*equipment.chooseWeapon(itemlist.weapon_list, 0))
        armor  = equipment.Armor(*equipment.chooseArmor(itemlist.armor_list, 4))
        offhand  = equipment.Shield(*equipment.chooseShield(itemlist.shield_list, 1))
        hasOffhand = True
    elif playerClass.startswith('B'):
        playerClass = Berserker
        weapon = equipment.Weapon(*equipment.chooseWeapon(itemlist.weapon_list, 5))
        armor  = equipment.Armor(*equipment.chooseArmor(itemlist.armor_list, 2))
        hasOffhand = False
    elif playerClass.startswith('R'):
        playerClass = Rogue
        weapon = equipment.Weapon(*equipment.chooseWeapon(itemlist.weapon_list, 3))
        offhand = equipment.Weapon(*equipment.chooseWeapon(itemlist.weapon_list, 3))
        armor  = equipment.Armor(*equipment.chooseArmor(itemlist.armor_list, 1))
        hasOffhand = True
    elif playerClass.startswith('w'):
        playerClass = Wizard
        weapon = equipment.Weapon(*equipment.chooseWeapon(itemlist.weapon_list, 8))
        armor  = equipment.Armor(*equipment.chooseArmor(itemlist.armor_list, 0))
        hasOffhand = False
    global player
    player = Unit(playerClass)
    Unit.equip(player, weapon) 
    Unit.equip(player, armor)
    if hasOffhand is True:
        Unit.equip(player, offhand)

def chooseMonsterClass():
    monsterClass = Orc
    global monster
    monster = Unit(monsterClass)
    weapon = equipment.Weapon(*equipment.chooseWeapon(itemlist.weapon_list, random.randint(0, 7)))
    armor  = equipment.Armor(*equipment.chooseArmor(itemlist.armor_list, random.randint(0, 5)))
    Unit.equip(monster, weapon)
    Unit.equip(monster, armor)

#                           str, con, dex, wis, int, cun
Berserker = Attributes('berserker', 16, 11, 5, 2, 4, 3)
Warrior = Attributes('warrior', 6, 18, 7, 5, 4, 5)
Rogue = Attributes('rogue', 4, 6, 17, 4, 5, 11)
Wizard = Attributes('wizard', 3, 5, 4, 12, 22, 4)
Orc = Attributes('orc', 3, 3, 3, 3, 3, 3) 
