import random
import time
import itemlist
import classes
import stringparse
import equipment
import abilities

class Unit:
    def __init__(self, type):
        self.type           = type.type
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

def chooseClass():
    print('Choose your class')
    print(' ')
    print('''B: Berserker (STR, CON)
R: Rogue (DEX, CUN)
W: Warrior (CON, STR)
''')
    playerClass = input()
    if playerClass.lower().startswith('w'):
        playerClass = classes.Warrior
        weapon = equipment.Weapon(*chooseWeapon(itemlist.weapon_list, 0))
        armor  = equipment.Armor(*chooseArmor(itemlist.armor_list, 4))
        offhand  = equipment.Shield(*chooseShield(itemlist.shield_list, 1))
        hasOffhand = True
    elif playerClass.lower().startswith('b'):
        playerClass = classes.Berserker
        weapon = equipment.Weapon(*chooseWeapon(itemlist.weapon_list, 5))
        armor  = equipment.Armor(*chooseArmor(itemlist.armor_list, 2))
        hasOffhand = False
    elif playerClass.lower().startswith('r'):
        playerClass = classes.Rogue
        weapon = equipment.Weapon(*chooseWeapon(itemlist.weapon_list, 3))
        offhand = equipment.Weapon(*chooseWeapon(itemlist.weapon_list, 3))
        armor  = equipment.Armor(*chooseArmor(itemlist.armor_list, 1))
        hasOffhand = True
    global player
    player = Unit(playerClass)
    Unit.equip(player, weapon) 
    Unit.equip(player, armor)
    if hasOffhand is True:
        Unit.equip(player, offhand)

def chooseMonsterClass():
    monsterClass = classes.Orc
    global monster
    monster = Unit(monsterClass)
    weapon = equipment.Weapon(*chooseWeapon(itemlist.weapon_list, random.randint(0, 7)))
    armor  = equipment.Armor(*chooseArmor(itemlist.armor_list, random.randint(0, 5)))
    Unit.equip(monster, weapon)
    Unit.equip(monster, armor)
    
def decideTurn(playerWeight, monsterWeight): 
    if (playerWeight - monsterWeight) > 0:
        initiator = monster
        defender = player
        if playerWeight//monsterWeight < 1:
            tpr = 1
        elif playerWeight//monsterWeight > 3:
            tpr = 3
        else:
            tpr = playerWeight//monsterWeight
    elif (playerWeight - monsterWeight) <0:
        initiator = player
        defender = monster
        if (playerWeight//playerWeight * -1) < 1:
            tpr = 1
        elif (playerWeight//playerWeight * -1) > 3:
            tpr = 3
        else:
            tpr = playerWeight//playerWeight * -1
    else:
        initiator = player
        defender = monster
        tpr = 1
    return tpr, initiator, defender

def meleeAttack(attacker, defender):
    offhand = False
    unitDeath = (False, 'nobody')
    if attacker.offhand is not None:
        offhand = attacker.offhand
    wepMhDmg, wepOhDmg = getDmgRoll(attacker)
    unitHasCrit = attackCrit(attacker)
    unitHasDodged = cunningDodge(defender)
    unitHasBlocked = blockAttack(defender)
    unitCunAtk = cunningAttack(attacker)
    if unitHasBlocked is True:
        wepMhDmg -= defender.offhandBlockValue
        wepOhDmg -= defender.offhandBlockValue
    if unitCunAtk is False:
        wepMhDmg -= int(defender.armorClass/1.6)
        wepOhDmg -= int(defender.armorClass/1.6)
    if unitHasCrit[0] is True:
        if unitHasCrit[1] is True:
            wepMhDmg *= attacker.mainhandCrit
        elif unitHasCrit[0] is True:
            wepOhDmg *= attacker.offhandCrit
    if wepOhDmg < 0:
        wepOhDmg = 0
    wepTotDmg = int(wepMhDmg) + int(wepOhDmg)
    if wepTotDmg < 0:
        wepTotDmg = 0
    if unitHasDodged == True:
        wepTotDmg = 0
    defender.curhp -= wepTotDmg
    if defender.curhp <= 0:
        if defender.type is not 'berserker' and defender.type is not 'rogue' and defender.type is not 'warrior':
            unitDeath = (True, 'monster')
        else:
            unitDeath = (True, 'player')
    stringparse.meleeStringParse(unitHasDodged, unitHasCrit, unitCunAtk, defender, attacker, unitDeath, wepTotDmg, unitHasBlocked)
    return unitDeath

def getDmgRoll(unit):
    wepOhDmg = 0
    wepMhDmg = random.randint(unit.mainhandWepMin, unit.mainhandWepMax) + unit.dmg
    if unit.offhand is not None and unit.offhand is not 'shield':
        wepOhDmg = random.randint(unit.offhandWepMin, unit.offhandWepMax) + unit.dmg
    return wepMhDmg, wepOhDmg

def attackCrit(unit):
    unitHasCrit = False
    unitOffhandCrit = False
    unitMainhandCrit = False
    unitCritMod = unit.dex//4
    if (random.randint(1, 20) <= (unitCritMod + unit.mainhandCrit)):
            unitMainhandCrit = True
    if unit.offhand is not None and unit.offhand is not 'shield':
        if (random.randint(1, 20) <= (unitCritMod + unit.offhandCrit)):
            unitOffhandCrit = True
    if unitMainhandCrit is True or unitOffhandCrit is True:
            unitHasCrit = True
    return unitHasCrit, unitMainhandCrit, unitOffhandCrit

def blockAttack(unit):
        unitHasBlocked = False
        if unit.offhand is 'shield':
            if random.randint(1, 10) <= unit.offhandBlockChance:
                unitHasBlocked = True
        return unitHasBlocked
	
def cunningDodge(unit):
    unitHasDodged = False
    if (random.randint(1, 20)  <= (unit.cun//3)):
        unitHasDodged = True
    return unitHasDodged

def cunningAttack(unit):
    unitCunAtk = False
    if (random.randint(1, 20)  <= (unit.cun//3)):
        unitCunAtk = True
    return unitCunAtk
        
def gameTurn(tpr, attacker, defender):
    if defender.curhp > 0 and attacker.curhp > 0:
        for i in range(tpr):
            unitDeath = meleeAttack(attacker, defender)
            if unitDeath[0] is True:
                break
        return unitDeath
            
def fight(initiator):
    print(' ')
    print('An enemy approaches!')
    print(' ')
    time.sleep(1)
    print('Equipment:')
    time.sleep(1)
    if player.offhand is not None:
        print('You: %s (mainhand), %s (offhand), %s (%s ac)' % (player.mainhandWeaponName, player.offhandItemName, player.armorName, player.armorClass))
    elif player.mainhand is '2h':
        print('You: %s (two-handed), %s (%s ac)' % (player.mainhandWeaponName, player.armorName, player.armorClass))
    else:
        print('You: %s (mainhand), %s (%s ac)' % (player.mainhandWeaponName, player.armorName, player.armorClass))
    time.sleep(.5)
    if monster.offhand is not None:
        print('%s: %s (mainhand), %s (offhand), %s (%s ac)' % (monster.type, monster.mainhandWeaponName, monster.offhandItemName, monster.armorName, monster.armorClass))
    elif monster.mainhand is '2h':
        print('%s: %s (two-handed), %s (%s ac)' % (monster.type, monster.mainhandWeaponName, monster.armorName, monster.armorClass))
    else:
        print('%s: %s (mainhand), %s (%s ac)' % (monster.type, monster.mainhandWeaponName, monster.armorName, monster.armorClass))
    stringparse.dispHP(player.curhp, player.maxhp, monster.curhp, monster.maxhp)
    time.sleep(1)
    while player.curhp > 0 and monster.curhp > 0:
        unitDeath = gameTurn(tpr, initiator, defender)
        if unitDeath[0] is True:
            stringparse.dispHP(player.curhp, player.maxhp, monster.curhp, monster.maxhp)
            break
        unitDeath = gameTurn(1, defender, initiator)
        stringparse.dispHP(player.curhp, player.maxhp, monster.curhp, monster.maxhp)
    return unitDeath

chooseClass()                                                       #chooses player class
chooseMonsterClass()                                                #chooses monster class
tpr, initiator, defender = decideTurn(player.weight, monster.weight)   #determines who goes first and how many turns per round
kill_count = 0
unitDeath = fight(initiator)          #initiates fight

while 'player' not in unitDeath:
        kill_count += 1
        chooseMonsterClass()
        tpr, initiator, defender = decideTurn(player.weight, monster.weight)
        unitDeath = fight(initiator) #rerolls monster and fights again

if kill_count is 1:
	print('You have died. You killed %s monster.' % kill_count)
else:
	print('You have died. You killed %s monsters.' % kill_count)
time.sleep(10)
