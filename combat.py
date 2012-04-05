import random
import time
import itemlist
import classes
import stringparse

kill_count = 0
weapon_crit = 0
weapon_critdmg = 0

class Unit:
    def __init__(self, weapon_name, weapon_min, weapon_max, weapon_crit, weapon_critdmg, wepweight, armor, ac, armorweight, str, con, dex, wis, int, cun): 
        self.weapon     = weapon_name
        self.wepmin     = weapon_min
        self.wepmax     = weapon_max
        self.wepcrit    = weapon_crit
        self.wepcritdmg = weapon_critdmg//1
        self.armor      = armor
        self.ac         = ac
        self.str        = str
        self.con        = con
        self.dex        = dex
        self.wis        = wis
        self.int        = int
        self.cun        = cun
        self.weight     = wepweight + armorweight
        self.maxhp      = con * 8
        self.curhp      = self.maxhp
        if dex > str:
            self.dmg    = dex//2
        else:
            self.dmg    = str//1.3

def chooseweapon(weapon_list): #getting weapon properties out of the itemlist
    weapon_name = {}
    weaponChoice = random.randint(0, 7)
    weapon_name = itemlist.weapon_list[weaponChoice][0]
    weapon_min = itemlist.weapon_list[weaponChoice][2]
    weapon_max = itemlist.weapon_list[weaponChoice][3]
    weapon_crit = itemlist.weapon_list[weaponChoice][4]
    weapon_critdmg = itemlist.weapon_list[weaponChoice][5]
    weapon_weight = itemlist.weapon_list[weaponChoice][7]
    return weapon_name, weapon_min, weapon_max, weapon_weight

def choosearmor(armor_list): #getting armor properties out of the itemlist
    armor_name = {}
    armorChoice = random.randint(0, 5)
    armor_name = itemlist.armor_list[armorChoice][0]
    armor_class = itemlist.armor_list[armorChoice][2]
    armor_weight = itemlist.armor_list[armorChoice][3]
    return armor_name, armor_class, armor_weight

print('Choose your class')
print(' ')
print('''B: Berserker (STR, CON)
R: Rogue (DEX, CUN)
W: Warrior (CON, STR)''')

player_class = input()
if player_class.lower().startswith('w'):
    player_class = classes.Warrior
    player = Unit(itemlist.weapon_list[0][0], itemlist.weapon_list[0][2], itemlist.weapon_list[0][3], itemlist.weapon_list[0][4], itemlist.weapon_list[0][5], itemlist.weapon_list[0][7], itemlist.armor_list[4][0], itemlist.armor_list[4][2], itemlist.armor_list[4][3], player_class.str, player_class.con, player_class.dex, player_class.wis, player_class.int, player_class.cun)
elif player_class.lower().startswith('b'):
    player_class = classes.Berserker
    player = Unit(itemlist.weapon_list[5][0], itemlist.weapon_list[5][2], itemlist.weapon_list[5][3], itemlist.weapon_list[5][4], itemlist.weapon_list[5][5], itemlist.weapon_list[0][7], itemlist.armor_list[2][0], itemlist.armor_list[2][2], itemlist.armor_list[2][3], player_class.str, player_class.con, player_class.dex, player_class.wis, player_class.int, player_class.cun)
elif player_class.lower().startswith('r'):
    player_class = classes.Rogue
    player = Unit(itemlist.weapon_list[3][0], itemlist.weapon_list[3][2], itemlist.weapon_list[3][3], itemlist.weapon_list[3][4], itemlist.weapon_list[3][5], itemlist.weapon_list[3][7], itemlist.armor_list[1][0], itemlist.armor_list[1][2], itemlist.armor_list[1][3], player_class.str, player_class.con, player_class.dex, player_class.wis, player_class.int, player_class.cun)

monster_class = classes.Orc

weapon_name, weapon_min, weapon_max, weapon_weight = chooseweapon(itemlist.weapon_list) #randomly assigns weapon
armor_name, armor_class, armor_weight = choosearmor(itemlist.armor_list) # randomly assigns armor
orc = Unit(weapon_name, weapon_min, weapon_max, weapon_crit, weapon_critdmg, weapon_weight, armor_name, armor_class, armor_weight, monster_class.str, monster_class.con, monster_class.dex, monster_class.wis, monster_class.int, monster_class.cun) # gives orc stats

def decideTurn(playerweight, orcweight):
    initiate = playerweight - orcweight
    if initiate > 0:
        initiator = 'orc'
        if initiate//orcweight < 1:
            otpr = 1
        elif initiate//orcweight > 5:
            otpr = 5
        else:
            otpr = initiate//orcweight
        ptpr = 1
    elif initiate <0:
        initiator = 'player'
        if (initiate//playerweight * -1) < 1:
            ptpr = 1
        elif (initiate//playerweight * -1) > 5:
            ptpr = 5
        else:
            ptpr = initiate//playerweight * -1
        otpr = 1
    else:
        initiator = 'player'
        ptpr = 1
        otpr = 1
    return ptpr, otpr, initiator

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
    if orc.curhp > 0 and player.curhp > 0:
        for i in range(otpr):
            wep_dmg = random.randint(player.wepmin, player.wepmax)
            unitHasCrit = attackCrit(player.dex, player.wepcrit)
            unitHasDodged = cunningDodge(orc.cun)
            unitCunAtk = cunningAttack(player.cun)
            dmg = wep_dmg + player.dmg
            if unitCunAtk == False:
                dmg -= int(orc.ac/1.6)
            if unitHasCrit == True:
                dmg *= player.wepcritdmg
            dmg = int(dmg)
            if dmg < 0:
                dmg = 0
            if unitHasDodged == True:
                dmg = 0
            orc.curhp -= dmg
            if orc.curhp <= 0:
                orc_death = True
            elif player.curhp > 0:
                orc_death = False
            unitHasDied = stringparse.StringParse(unitHasDodged, unitHasCrit, unitCunAtk, 'orc', 'player', orc_death, dmg)
            if unitHasDied == True:
                break
            
def orcTurn(otpr):    
    if orc.curhp > 0 and player.curhp > 0:
        for i in range(otpr):
            wep_dmg = random.randint(orc.wepmin, orc.wepmax)
            unitHasCrit = attackCrit(orc.dex, orc.wepcrit)
            unitHasDodged = cunningDodge(player.cun)
            unitCunAtk = cunningAttack(orc.cun)
            dmg = wep_dmg + orc.dmg
            if unitCunAtk == False:
                dmg -= int(player.ac/1.6)
            if unitHasCrit == True:
                dmg *= orc.wepcritdmg
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
            unitHasDied = stringparse.StringParse(unitHasDodged, unitHasCrit, unitCunAtk, 'player', 'orc', player_death, dmg)
            if unitHasDied == True:
                break

def fight(initiator):
    player_death = False
    orc_death = False
    print('An orc approaches!')
    print(' ')
    time.sleep(2)
    print('You: (%s/%s HP) (Equip: %s (%s-%s), %s (%s ac))' % (player.curhp, player.maxhp, player.weapon, player.wepmin, player.wepmax, player.armor, player.ac) )
    time.sleep(1)
    print('Him: (%s/%s HP)  (Equip: %s (%s-%s), %s (%s ac))' % (orc.curhp, orc.maxhp, orc.weapon, orc.wepmin, orc.wepmax, orc.armor, orc.ac) )
    stringparse.dispHP(player.curhp, player.maxhp, orc.curhp, orc.maxhp, 2)
    time.sleep(2)

    while player.curhp > 0 and orc.curhp > 0:
        if initiator == 'player' and player_death == False and orc_death == False:
            playerTurn(ptpr)
            time.sleep(.5)
            orcTurn(otpr)
            if player.curhp <= 0:    
                player.curhp = 0
                player_death = True
            elif orc.curhp <= 0:
                orc.curhp = 0
                orc_death = True
            stringparse.dispHP(player.curhp, player.maxhp, orc.curhp, orc.maxhp, .5)
            time.sleep(2)         
        elif initiator == 'orc' and player_death == False and orc_death == False:
            orcTurn(otpr)
            time.sleep(.5)
            playerTurn(ptpr)
            if player.curhp <= 0:        
                player.curhp = 0
                player_death = True
            elif orc.curhp <= 0:
                orc.curhp = 0
                orc_death = True
            stringparse.dispHP(player.curhp, player.maxhp, orc.curhp, orc.maxhp, .5)
            time.sleep(.5)
    return player_death, orc_death, kill_count
            
ptpr, otpr, initiator = decideTurn(player.weight, orc.weight)   #determines who goes first and how many turns per round
player_death, orc_death, kill_count = fight(initiator)

while player_death == False:
        orc_death = False
        kill_count += 1
        weapon_name, weapon_min, weapon_max, weapon_weight = chooseweapon(itemlist.weapon_list)
        armor_name, armor_class, armor_weight = choosearmor(itemlist.armor_list) 
        weight = armor_weight + weapon_weight 
        orc = Unit(weapon_name, weapon_min, weapon_max, weapon_crit, weapon_critdmg, weapon_weight, armor_name, armor_class, armor_weight, monster_class.str, monster_class.con, monster_class.dex, monster_class.wis, monster_class.int, monster_class.cun) 
        ptpr, otpr, initiator = decideTurn(player.weight, orc.weight)
        player_death, orc_death, kill_count = fight(initiator) #rerolls orc and fights again

print('You have died. You killed %s orcs.' % kill_count)
time.sleep(10)
