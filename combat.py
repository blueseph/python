import random
import time
import itemlist
import classes

weapon_min = ''
weapon_max = ''
weapon_name = 'unarmed'
weapon_weight = 0
armor_class = ''
armor_weight = 0
initiator = ''
initiate = 0
otpr = 0
ptpr = 0
player_death = False
orc_death = False
kill_count = 0
weapon_crit = 0
weapon_critdmg = 0
unitHasCrit = False

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
            self.dmg    = dex//3
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
            otpr = 5
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
    return unitHasCrit

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
        for i in range(ptpr):
            wep_dmg = random.randint(player.wepmin, player.wepmax)
            unitHasCrit = attackCrit(player.dex, player.wepcrit)
            unitHasDodged = cunningDodge(orc.cun)
            unitCunAtk = cunningAttack(player.cun)
            if unitHasDodged == True:
                print('You attack. The orc dodges!')
                time.sleep(1)
            else:
                if unitHasCrit == True:
                    dmg = (wep_dmg + player.dmg) * player.wepcritdmg
                else:
                    dmg = wep_dmg + player.dmg
                if unitCunAtk == False:
                    dmg -= orc.ac
                if dmg <= 0:
                    print('You attack! It does no damage.')
                    time.sleep(1)
                else:
                    orc.curhp -= dmg
                    if orc.curhp <= 0 and unitHasCrit == False and unitCunAtk == False:
                            print('You attack! The orc takes %s damage. The damage is fatal!' % dmg)
                            time.sleep(2)
                            print('You have slain the orc!')
                            orc_death = True
                            break
                    elif orc.curhp <= 0 and unitHasCrit == True and unitCunAtk == False:
                            print('You critically hit the orc! The orc takes %s damage. The damage is fatal!' % dmg)
                            time.sleep(2)
                            print('You have slain the orc!')
                            orc_death = True
                            unitHasCrit == False
                            break
                    elif orc.curhp <= 0 and unitHasCrit == False and unitCunAtk == True:
                            print('You find a hole in the orc\'s armor! The orc takes %s damage. The damage is fatal!' % dmg)
                            time.sleep(2)
                            print('You have slain the orc!')
                            orc_death = True
                            break
                    elif orc.curhp <= 0 and unitHasCrit == True and unitCunAtk == True:
                            print('You find a hole in the orc\'s armor! You also strike critically! The orc takes %s damage. The damage is fatal!' % dmg)
                            time.sleep(2)
                            print('You have slain the orc!')
                            orc_death = True
                            break
                    elif unitHasCrit == True and unitCunAtk == False:
                            print('You critically hit the orc! The attack does %s damage.' % dmg)
                            time.sleep(1)
                    elif unitHasCrit == True and unitCunAtk == True:
                            print('You find a hole in the orc\'s armor! You also strike critically! The attack does %s damage.' % dmg)
                            time.sleep(1)
                    elif unitHasCrit == False and unitCunAtk == True:
                            print('You find a hole in the orc\'s armor! The attack does %s damage.' % dmg)
                            time.sleep(1)
                    else:
                            print('You attack. You deal %s damage to the orc.' % dmg )
                            time.sleep(1)
                        
def orcTurn(otpr):
    if orc.curhp > 0 and player.curhp > 0:
        for i in range(otpr):
            wep_dmg = random.randint(orc.wepmin, orc.wepmax)
            unitHasCrit = attackCrit(orc.dex, orc.wepcrit)
            unitHasDodged = cunningDodge(player.cun)
            unitCunAtk = cunningAttack(orc.cun)
            if unitHasDodged == True:
                print('The orc attacks. You dodge!')
                time.sleep(1)
            else:
                if unitHasCrit == True:
                    dmg = (wep_dmg + orc.dmg) * orc.wepcritdmg
                else:
                    dmg = wep_dmg + orc.dmg
                if unitCunAtk == False:
                    dmg -= player.ac
                if dmg <= 0:
                    print('The orc attacks. It does no damage.')
                    time.sleep(1)
                else:
                    player.curhp -= dmg
                    if player.curhp <= 0 and unitHasCrit == False and unitCunAtk == False:
                            print('The orc attacks! You takes %s damage. The damage is fatal!' % dmg)
                            time.sleep(2)
                            print('You have been slain!')
                            player_death = True
                            break
                    elif player.curhp <= 0 and unitHasCrit == True and unitCunAtk == False:
                            print('The orc critically hits you! You take %s damage. The damage is fatal!' % dmg)
                            time.sleep(2)
                            print('You have been slain!')
                            player_death = True
                            break
                    elif player.curhp <= 0 and unitHasCrit == False and unitCunAtk == True:
                            print('The orc finds a hole in your armor! You take %s damage. The damage is fatal!' % dmg)
                            time.sleep(2)
                            print('You have been slain')
                            player_death = True
                            break
                    elif player.curhp <= 0 and unitHasCrit == True and unitCunAtk == True:
                            print('The orc finds a hole in your armor! It also attacks critically! You take %s damage. The damage is fatal!' % dmg)
                            time.sleep(2)
                            print('You have been slain')
                            player_death = True
                            break
                    elif unitHasCrit == True and unitCunAtk == False:
                            print('The orc critically hits you! The attack does %s damage.' % dmg)
                            time.sleep(1)
                    elif unitHasCrit == True and unitCunAtk == True:
                            print('The orc finds a hole in your armor! It also attacks critically! The attack does %s damage.' % dmg)
                            time.sleep(1)
                    elif unitHasCrit == False and unitCunAtk == True:
                            print('The orc finds a hole in your armor! The attack does %s damage.' % dmg)
                            time.sleep(1)
                    else:
                            print('The orc attacks. It deals %s damage to you.' % dmg )
                            time.sleep(1)

def fight(initiator):
    player_death = False
    orc_death = False
    print('otpr: %s   ptpr: %s   orc weight: %s   player weight: %s' % (otpr, ptpr, orc.weight, player.weight))
    print('An orc approaches!')
    print(' ')
    time.sleep(2)
    print('You: (%s/%s HP) (Equip: %s (%s-%s), %s (%s ac))' % (player.curhp, player.maxhp, player.weapon, player.wepmin, player.wepmax, player.armor, player.ac) )
    time.sleep(1)
    print('Him: (%s/%s HP)   (Equip: %s (%s-%s), %s (%s ac))' % (orc.curhp, orc.maxhp, orc.weapon, orc.wepmin, orc.wepmax, orc.armor, orc.ac) )
    print(' ')
    time.sleep(2)

    while player.curhp > 0 and orc.curhp > 0:
        if initiator == 'player' and player_death == False and orc_death == False:
            playerTurn(ptpr)
            time.sleep(.5)
            orcTurn(otpr)
            if player.curhp <= 0:    #sets current hp to 0 if player or orc has died
                player.curhp = 0
                player_death = True
            elif orc.curhp <= 0:
                orc.curhp = 0
                orc_death = True
            time.sleep(.5)
            print(' ')
            print('         You: (%s/%s HP)       Him: (%s/%s HP)' % (player.curhp, player.maxhp, orc.curhp, orc.maxhp) )
            print(' ')
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
            time.sleep(.5)
            print(' ')
            print('         You: (%s/%s HP)       Him: (%s/%s HP)' % (player.curhp, player.maxhp, orc.curhp, orc.maxhp) )
            print(' ')
            time.sleep(.5)
    return player_death, orc_death, kill_count
            
ptpr, otpr, initiator = decideTurn(player.weight, orc.weight)   #determines who goes first and how many turns per round
player_death, orc_death, kill_count = fight(initiator)

while player_death == False:
        orc_death = False
        kill_count += 1
        weapon_name, weapon_min, weapon_max, weapon_weight = chooseweapon(itemlist.weapon_list) #randomly assigns weapon
        armor_name, armor_class, armor_weight = choosearmor(itemlist.armor_list) # randomly assigns armor
        weight = armor_weight + weapon_weight # adds total weight
        orc = Unit(weapon_name, weapon_min, weapon_max, weapon_crit, weapon_critdmg, weapon_weight, armor_name, armor_class, armor_weight, monster_class.str, monster_class.con, monster_class.dex, monster_class.wis, monster_class.int, monster_class.cun) # gives orc stats
        ptpr, otpr, initiator = decideTurn(player.weight, orc.weight)   #determines who goes first and how many turns per round
        player_death, orc_death, kill_count = fight(initiator)

print('You have died. You killed %s orcs.' % kill_count)
