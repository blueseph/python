import random
import time
import itemlist
import classes
import stringparse
import equipment

class Unit:
    def __init__(self, type):
        self.type           = type.type
        self.str            = type.str
        self.con            = type.con
        self.dex            = type.dex
        self.wis            = type.wis
        self.int            = type.int
        self.cun            = type.cun
        self.maxhp          = self.con * 8
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
            self.offhandRange       = item.weaponRange
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
        self.weight = self.mainhandWeight + self.offhandWeight + self.armorWeight # works in a very ugly way
            
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

def chooseClass():
    print('Choose your class')
    print(' ')
    print('''B: Berserker (STR, CON)
R: Rogue (DEX, CUN)
W: Warrior (CON, STR)''')
    playerClass = input()
    if playerClass.lower().startswith('w'):
        playerClass = classes.Warrior
        startWeapon = 0
        startArmor = 4
    elif playerClass.lower().startswith('b'):
        playerClass = classes.Berserker
        startWeapon = 5
        startArmor = 2
    elif playerClass.lower().startswith('r'):
        playerClass = classes.Rogue
        startWeapon = 3
        startArmor = 1
    global player
    player = Unit(playerClass)
    weapon = equipment.Weapon(*chooseWeapon(itemlist.weapon_list, startWeapon))
    armor  = equipment.Armor(*chooseArmor(itemlist.armor_list, startArmor))
    Unit.equip(player, weapon) 
    Unit.equip(player, armor)

def chooseMonsterClass():
    monsterClass = classes.Orc
    global monster
    monster = Unit(monsterClass)
    weapon = equipment.Weapon(*chooseWeapon(itemlist.weapon_list, random.randint(0, 7)))
    armor  = equipment.Armor(*chooseArmor(itemlist.armor_list, random.randint(0, 5)))
    Unit.equip(monster, weapon)
    Unit.equip(monster, armor)
    
def decideTurn(player_weight, monster_weight): #todo cleanup?
    initiate = player_weight - monster_weight
    if initiate > 0:
        initiator = 'monster'
        if initiate//monster_weight < 1:
            mtpr = 1
        elif initiate//monster_weight > 5:
            mtpr = 5
        else:
            mtpr = initiate//monster_weight
        ptpr = 1
    elif initiate <0:
        initiator = 'player'
        if (initiate//player_weight * -1) < 1:
            ptpr = 1
        elif (initiate//player_weight * -1) > 5:
            ptpr = 5
        else:
            ptpr = initiate//player_weight * -1
        mtpr = 1
    else:
        initiator = 'player'
        ptpr = 1
        mtpr = 1
    return ptpr, mtpr, initiator

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
        
def playerTurn(ptpr):
    offhand = False
    if player.offhand is not None:
        offhand = player.offhandType
    if monster.curhp > 0 and player.curhp > 0:
        for i in range(ptpr):
            wepMhDmg, wepOhDmg = getDmgRoll(player)
            unitHasCrit = attackCrit(player)
            unitHasDodged = cunningDodge(monster)
            unitCunAtk = cunningAttack(player)
            if unitCunAtk is False:
                wepMhDmg -= int(monster.armorClass/1.6)
                wepOhDmg -= int(monster.armorClass/1.6)
            if unitHasCrit is True:
                if unitMainhandCrit is True:
                    wepMhDmg *= player.mainhandCrit
                elif unitOffhandCrit is True:
                    wepOhDmg *= player.offhandCrit
            if wepOhDmg < 0:
                wepOhDmg = 0
            wepTotDmg = int(wepMhDmg) + int(wepOhDmg)
            if wepTotDmg < 0:
                wepTotDmg = 0
            if unitHasDodged == True:
                wepTotDmg = 0
            monster.curhp -= wepTotDmg
            if monster.curhp <= 0:
                monsterDeath = True
            elif monster.curhp > 0:
                monsterDeath = False
            unitHasDied = stringparse.StringParse(unitHasDodged, unitHasCrit, unitCunAtk, monster.type, 'player', monsterDeath, wepTotDmg, offhand)
            if unitHasDied == True:
                break
            
def monsterTurn(mtpr):
    offhand = False
    if player.offhand is not None:
        offhand = player.offhandType
    if monster.curhp > 0 and player.curhp > 0:
        for i in range(mtpr):
            wepMhDmg, wepOhDmg = getDmgRoll(monster)
            unitHasCrit = attackCrit(monster)
            unitHasDodged = cunningDodge(player)
            unitCunAtk = cunningAttack(monster)
            if unitCunAtk is False:
                wepMhDmg -= int(player.armorClass/1.6)
                wepOhDmg -= int(player.armorClass/1.6)
            if unitHasCrit is True:
                if unitMainhandCrit is True:
                    wepMhDmg *= monster.mainhandCrit
                elif unitOffhandCrit is True:
                    wepOhDmg *= monster.offhandCrit
            if wepOhDmg < 0:
                wepOhDmg = 0
            wepTotDmg = int(wepMhDmg) + int(wepOhDmg)
            if wepTotDmg < 0:
                wepTotDmg = 0
            if unitHasDodged == True:
                wepTotDmg = 0
            player.curhp -= wepTotDmg
            if player.curhp <= 0:
                playerDeath = True
            elif player.curhp > 0:
                playerDeath = False
            unitHasDied = stringparse.StringParse(unitHasDodged, unitHasCrit, unitCunAtk, 'player', monster.type, playerDeath, wepTotDmg, offhand)
            if unitHasDied == True:
                break
def fight(initiator):  #todo cleanup?
    playerDeath = False
    monsterDeath = False
    print('An enemy approaches!')
    print(' ')
    time.sleep(1)
    print('Equipment:')
    time.sleep(.5)
    if player.offhand is not None:
        print('You: %s (mainhand), %s (offhand), %s (%s ac)' % (player.mainhandWeaponName, player.offhandItemName, player.armorName, player.armorClass))
    else:
        print('You: %s (mainhand), %s (%s ac)' % (player.mainhandWeaponName, player.armorName, player.armorClass))
    time.sleep(.5)
    if monster.offhand is not None:
        print('%s: %s (mainhand), %s (offhand), %s (%s ac)' % (monster.type, monster.mainhandWeaponName, monster.offhandItemName, monster.armorName, monster.armorClass))
    else:
        print('%s: %s (mainhand), %s (%s ac)' % (monster.type, monster.mainhandWeaponName, monster.armorName, monster.armorClass))
    time.sleep(1)
    stringparse.dispHP(player.curhp, player.maxhp, monster.curhp, monster.maxhp, 2)
    time.sleep(1)

    while player.curhp > 0 and monster.curhp > 0:
        if initiator is 'player' and playerDeath is False and monsterDeath is False:
            playerTurn(ptpr)
            time.sleep(1)
            monsterTurn(mtpr)
            if player.curhp <= 0:    
                player.curhp = 0
                playerDeath = True
            elif monster.curhp <= 0:
                monster.curhp = 0
                monsterDeath = True
            stringparse.dispHP(player.curhp, player.maxhp, monster.curhp, monster.maxhp, .5)
            time.sleep(2)         
        elif initiator is 'monster' and playerDeath is False and monsterDeath is False:
            monsterTurn(mtpr)
            time.sleep(1)
            playerTurn(ptpr)
            if player.curhp <= 0:        
                player.curhp = 0
                playerDeath = True
            elif monster.curhp <= 0:
                monster.curhp = 0
                monsterDeath = True
            stringparse.dispHP(player.curhp, player.maxhp, monster.curhp, monster.maxhp, .5)
            time.sleep(.5)
    return playerDeath, monsterDeath, kill_count

chooseClass()                                                       #chooses player class
chooseMonsterClass()                                                #chooses monster class
ptpr, mtpr, initiator = decideTurn(player.weight, monster.weight)   #determines who goes first and how many turns per round
kill_count = 0                                                      
playerDeath, monsterDeath, kill_count = fight(initiator)          #initiates fight

while playerDeath == False:
        monsterDeath = False
        kill_count += 1
        chooseMonsterClass()
        ptpr, mtpr, initiator = decideTurn(player.weight, monster.weight)
        playerDeath, monsterDeath, kill_count = fight(initiator) #rerolls monster and fights again

if kill_count is 1:
	print('You have died. You killed %s monster.' % kill_count)
else:
	print('You have died. You killed %s monsters.' % kill_count)
time.sleep(10)
