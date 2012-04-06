import random
import time
import itemlist
import classes
import stringparse

kill_count = 0

class Unit:
    def __init__(self, type, weapon_name, weapon_min, weapon_max, weapon_crit, weapon_critdmg, wepweight, wepmainhand, armor, ac, armorweight, str, con, dex, wis, int, cun):
        self.type           = type
        self.weapon         = weapon_name
        self.wepmin         = weapon_min
        self.wepmax         = weapon_max
        self.wepcrit        = weapon_crit
        self.wepcritdmg     = weapon_critdmg
        self.wephhand       = wepmainhand
        self.armor          = armor
        self.ac             = ac
        self.str            = str
        self.con            = con
        self.dex            = dex
        self.wis            = wis
        self.int            = int
        self.cun            = cun
        self.weight         = wepweight + armorweight
        self.maxhp          = con * 8
        self.curhp          = self.maxhp
        if dex > str:
            self.dmg        = dex//2
        else:
            self.dmg        = str//1.3
    

def chooseweapon(weapon_list, weaponChoice): #getting weapon properties out of the itemlist
    weapon_name = {}
    weapon_name = itemlist.weapon_list[weaponChoice][0]
    weapon_min = itemlist.weapon_list[weaponChoice][2]
    weapon_max = itemlist.weapon_list[weaponChoice][3]
    weapon_crit = itemlist.weapon_list[weaponChoice][4]
    weapon_critdmg = itemlist.weapon_list[weaponChoice][5]
    weapon_weight = itemlist.weapon_list[weaponChoice][7]
    weapon_hand = itemlist.weapon_list[weaponChoice][8]
    return weapon_name, weapon_min, weapon_max, weapon_crit, weapon_critdmg, weapon_weight, weapon_hand

def choosearmor(armor_list, armorChoice): #getting armor properties out of the itemlist
    armor_name = {}
    armor_name = itemlist.armor_list[armorChoice][0]
    armor_class = itemlist.armor_list[armorChoice][2]
    armor_weight = itemlist.armor_list[armorChoice][3]
    return armor_name, armor_class, armor_weight

def chooseClass():
    print('Choose your class')
    print(' ')
    print('''B: Berserker (STR, CON)
R: Rogue (DEX, CUN)
W: Warrior (CON, STR)''')
    player_class = input()
    if player_class.lower().startswith('w'):
        player_class = classes.Warrior
        player_weapon_name, player_weapon_min, player_weapon_max, player_weapon_crit, player_weapon_critdmg, player_weapon_weight, player_weapon_mainhand = chooseweapon(itemlist.weapon_list, 0)
        player_armor_name, player_armor_class, player_armor_weight = choosearmor(itemlist.armor_list, 4)
    elif player_class.lower().startswith('b'):
        player_class = classes.Berserker
        player_weapon_name, player_weapon_min, player_weapon_max, player_weapon_crit, player_weapon_critdmg, player_weapon_weight, player_weapon_mainhand = chooseweapon(itemlist.weapon_list, 5)
        player_armor_name, player_armor_class, player_armor_weight = choosearmor(itemlist.armor_list, 2)
    elif player_class.lower().startswith('r'):
        player_class = classes.Rogue
        player_weapon_name, player_weapon_min, player_weapon_max, player_weapon_crit, player_weapon_critdmg, player_weapon_weight, player_weapon_mainhand = chooseweapon(itemlist.weapon_list, 3)
        player_armor_name, player_armor_class, player_armor_weight = choosearmor(itemlist.armor_list, 1)
    global player
    player = Unit(player_class.type, player_weapon_name, player_weapon_min, player_weapon_max, player_weapon_crit, player_weapon_critdmg, player_weapon_weight, player_weapon_mainhand, player_armor_name, player_armor_class, player_armor_weight, player_class.str, player_class.con, player_class.dex, player_class.wis, player_class.int, player_class.cun)

def chooseMonsterClass():
    monster_class = classes.Orc
    monster_weapon_name, monster_weapon_min, monster_weapon_max, monster_weapon_crit, monster_weapon_critdmg, monster_weapon_weight, monster_weapon_mainhand = chooseweapon(itemlist.weapon_list, random.randint(0, 7)) #randomly assigns weapon
    monster_armor_name, monster_armor_class, monster_armor_weight = choosearmor(itemlist.armor_list, random.randint(0, 5)) # randomly assigns armor
    global monster
    monster = Unit(monster_class.type, monster_weapon_name, monster_weapon_min, monster_weapon_max, monster_weapon_crit, monster_weapon_critdmg, monster_weapon_weight, monster_weapon_mainhand, monster_armor_name, monster_armor_class, monster_armor_weight, monster_class.str, monster_class.con, monster_class.dex, monster_class.wis, monster_class.int, monster_class.cun) # gives monster stats

def decideTurn(player_weight, monster_weight):
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

def attackCrit(unit_dex, weapon_crit_mod):
    unitHasCrit = False
    unit_crit_mod = unit_dex//4
    if (random.randint(1, 20) <= (unit_crit_mod + weapon_crit_mod)):
        unitHasCrit = True
    else:
        unitHasCrit = False
    return unitHasCrit

def cunningDodge(unit_cunning):
    unitHasDodged = False
    unit_cunning = unit_cunning//3
    if (random.randint(1, 20)  <= (unit_cunning)):
        unitHasDodged = True
    else:
        unitHasDodged = False
    return unitHasDodged

def cunningAttack(unit_cunning):
    unitCunAtk = False
    unit_cunning = unit_cunning//3
    if (random.randint(1, 20)  <= (unit_cunning)):
        unitCunAtk = True
    else:
        unitCunningAttack = False
    return unitCunAtk
        
def playerTurn(ptpr):
    if monster.curhp > 0 and player.curhp > 0:
        for i in range(mtpr):
            wep_dmg = random.randint(player.wepmin, player.wepmax)
            unitHasCrit = attackCrit(player.dex, player.wepcrit)
            unitHasDodged = cunningDodge(monster.cun)
            unitCunAtk = cunningAttack(player.cun)
            dmg = wep_dmg + player.dmg
            if unitCunAtk == False:
                dmg -= int(monster.ac/1.6)
            if unitHasCrit == True:
                dmg *= player.wepcritdmg
            dmg = int(dmg)
            if dmg < 0:
                dmg = 0
            if unitHasDodged == True:
                dmg = 0
            monster.curhp -= dmg
            if monster.curhp <= 0:
                monster_death = True
            elif monster.curhp > 0:
                monster_death = False
            unitHasDied = stringparse.StringParse(unitHasDodged, unitHasCrit, unitCunAtk, monster.type, 'player', monster_death, dmg)
            if unitHasDied == True:
                break
            
def monsterTurn(mtpr):    
    if monster.curhp > 0 and player.curhp > 0:
        for i in range(mtpr):
            wep_dmg = random.randint(monster.wepmin, monster.wepmax)
            unitHasCrit = attackCrit(monster.dex, monster.wepcrit)
            unitHasDodged = cunningDodge(player.cun)
            unitCunAtk = cunningAttack(monster.cun)
            dmg = wep_dmg + monster.dmg
            if unitCunAtk == False:
                dmg -= int(player.ac/1.6)
            if unitHasCrit == True:
                dmg *= monster.wepcritdmg
            dmg = int(dmg)
            if dmg < 0:
                dmg = 0
            if unitHasDodged == True:
                dmg = 0
            player.curhp -= dmg
            if player.curhp <= 0:
                player_death = True
            elif player.curhp > 0:
                player_death = False
            unitHasDied = stringparse.StringParse(unitHasDodged, unitHasCrit, unitCunAtk, 'player', monster.type, player_death, dmg)
            if unitHasDied == True:
                break

def fight(initiator):
    player_death = False
    monster_death = False
    print('An enemy approaches!')
    print(' ')
    time.sleep(2)
    print('You: (%s/%s HP) (Equip: %s (%s-%s), %s (%s ac))' % (player.curhp, player.maxhp, player.weapon, player.wepmin, player.wepmax, player.armor, player.ac) )
    time.sleep(1)
    print('Him: (%s/%s HP)  (Equip: %s (%s-%s), %s (%s ac))' % (monster.curhp, monster.maxhp, monster.weapon, monster.wepmin, monster.wepmax, monster.armor, monster.ac) )
    stringparse.dispHP(player.curhp, player.maxhp, monster.curhp, monster.maxhp, 2)
    time.sleep(2)

    while player.curhp > 0 and monster.curhp > 0:
        if initiator == 'player' and player_death == False and monster_death == False:
            playerTurn(ptpr)
            time.sleep(.5)
            monsterTurn(mtpr)
            if player.curhp <= 0:    
                player.curhp = 0
                player_death = True
            elif monster.curhp <= 0:
                monster.curhp = 0
                monster_death = True
            stringparse.dispHP(player.curhp, player.maxhp, monster.curhp, monster.maxhp, .5)
            time.sleep(2)         
        elif initiator == 'monster' and player_death == False and monster_death == False:
            monsterTurn(mtpr)
            time.sleep(.5)
            playerTurn(ptpr)
            if player.curhp <= 0:        
                player.curhp = 0
                player_death = True
            elif monster.curhp <= 0:
                monster.curhp = 0
                monster_death = True
            stringparse.dispHP(player.curhp, player.maxhp, monster.curhp, monster.maxhp, .5)
            time.sleep(.5)
    return player_death, monster_death, kill_count

chooseClass()
print(player.type)
chooseMonsterClass()
print(monster.type)
ptpr, mtpr, initiator = decideTurn(player.weight, monster.weight)   #determines who goes first and how many turns per round
player_death, monster_death, kill_count = fight(initiator)

while player_death == False:
        monster_death = False
        kill_count += 1
        chooseMonsterClass()
        ptpr, mtpr, initiator = decideTurn(player.weight, monster.weight)
        player_death, monster_death, kill_count = fight(initiator) #rerolls monster and fights again

print('You have died. You killed %s monsters.' % kill_count)
time.sleep(10)
