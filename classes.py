import equipment
import itemlist
import random
import levelingstats
import gameturn

class Attributes:
    def __init__(self, unitclass, str, con, dex, wis, int, cun, curlvl):
        self.unitclass  = unitclass
        self.str        = str
        self.con        = con
        self.dex        = dex
        self.wis        = wis
        self.int        = int
        self.cun        = cun
        self. curlvl    = curlvl

class Creature(Attributes):
    
    ###############################
    #       sets initial stats    #
    ###############################

    def calculateStats(self):
        self.maxhp      = self.con * 14
        if self.dex > self.str:
            self.dmg    = int(self.dex//2.6)
        else:
            self.dmg    = int(self.str//1.3)
    
    def __init__(self, Attributes):
        self.unitclass      = Attributes.unitclass
        self.str            = Attributes.str
        self.con            = Attributes.con
        self.dex            = Attributes.dex
        self.wis            = Attributes.wis
        self.int            = Attributes.int
        self.cun            = Attributes.cun
        self.curlvl         = Attributes.curlvl
        self.type           = 'monster'
        self.calculateStats()
        self.curhp          = self.maxhp
        self.mainhand       = None
        self.offhand        = None
        self.offhandWeight  = 0
        self.armorWeight    = 0
        self.inventory      = []

    ###############################
    #       equipment system      #
    ###############################

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
        self.weight = self.mainhandWeight + self.offhandWeight + self.armorWeight

    ###############################
    #       inventory system      #
    ###############################

    def addInventoryItem(self, item): 
        self.inventory.append(item)

    ###############################
    #          xp system          #
    ###############################
    
    def giveXP(self):
        return int(10 + (self.curlvl ** 3.05))
        
class Player(Creature):            
    def __init__(self, Creature):
        self.unitclass      = Creature.unitclass
        self.str            = Creature.str
        self.type           = 'player'
        self.con            = Creature.con
        self.dex            = Creature.dex
        self.wis            = Creature.wis
        self.int            = Creature.int
        self.cun            = Creature.cun
        self.curlvl         = Creature.curlvl
        if self.curlvl is 1:
            self.curXP      = 0
        else:
            self.curXP      = levelingstats.xpToLevel[self.curLvl - 1]
        self.calculateStats()
        self.curhp          = self.maxhp
        self.mainhand       = None
        self.offhand        = None
        self.offhandWeight  = 0
        self.armorWeight    = 0
        self.inventory      = []

    ###############################
    #     player xp system        #
    ###############################
    
    def gainXP(self, xp):
        self.curXP += xp
        if self.curXP > levelingstats.xpToLevel[self.curlvl + 1]:
            gameturn.unitGainLvl = True

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
    player = Player(Creature(playerClass))
    player.addInventoryItem(weapon)
    player.addInventoryItem(armor)
    player.equip(weapon) 
    player.equip(armor)
    if hasOffhand is True:
        player.equip(offhand)
        player.addInventoryItem(offhand)

def chooseMonsterClass():
    monsterClass = Orc
    global monster
    monster = Creature(monsterClass)
    weapon = equipment.Weapon(*equipment.chooseWeapon(itemlist.weapon_list, random.randint(0, 7)))
    armor  = equipment.Armor(*equipment.chooseArmor(itemlist.armor_list, random.randint(0, 5)))
    monster.addInventoryItem(weapon)
    monster.addInventoryItem(armor)
    monster.equip(weapon)
    monster.equip(armor)
    

#                           str, con, dex, wis, int, cun, lvl
Berserker = Attributes('berserker', 16, 11, 5, 2, 4, 3, 1)
Warrior = Attributes('warrior', 14, 18, 7, 5, 4, 5, 1)
Rogue = Attributes('rogue', 4, 6, 17, 4, 5, 11, 1)
Wizard = Attributes('wizard', 3, 5, 4, 12, 22, 4, 1)
Orc = Attributes('orc', 3, 3, 3, 3, 3, 3, 1) 
