import time
import random
import classes
import gameturn
import levelingstats
import gameturn

tempWords = ('bam pow ouch splat slam slice crack wham whack').split()

def getHPBar(unit):
    if unit.curhp < 0:
        unit.curhp = 0
    HPBarString = ('[' + ('-' * round((unit.curhp / unit.maxhp) * 10) + (' ' * (10 - round((unit.curhp / unit.maxhp) * 10)) + ']' )))
    return HPBarString

def getEquipBar(unit):
    if unit.offhand is not None:
        equipBar = ('%s (mainhand) %s (offhand), %s (%s ac)' % (unit.mainhandWeaponName, unit.offhandItemName, unit.armorName, unit.armorClass))
    elif unit.mainhand is '2h':
         equipBar = ('%s (two-handed) %s (%s ac)' % (unit.mainhandWeaponName, unit.armorName, unit.armorClass))
    else:
         equipBar = ('%s (mainhand) %s (%s ac)' % (unit.mainhandWeaponName, unit.armorName, unit.armorClass))
    return equipBar

def personalBar(player):
    equipBar = getEquipBar(player)
    pb1 = '%s | XP: %s [%s/%s] | str: %s con:%s dex:%s wis:%s int:%s cun:%s | turn: %s' % (player.unitclass.title(), player.curlvl, player.curXP, levelingstats.xpToLevel[player.curlvl + 1], player.str, player.con, player.dex, player.wis, player.int, player.cun, gameturn.gameTurnCount)
    pb2 = equipBar
    return pb1, pb2

def blankCombatScreen(player, monster, sleep):
    playerHPBar = getHPBar(player)
    monsterHPBar = getHPBar(monster)
    pb1, pb2 = personalBar(player)
    spacer = ' '
    if (len(str(player.curhp)) + len(str(player.maxhp))) > 4:
        spacer =  (' ' * ((len(str(player.curhp)) + len(str(player.maxhp))) - 4))
    print('''


       You: %s/%s %s                                         %s: %s/%s
       %s                                         %s




                                                        


                             
                             
                                    







%s
%s
''' % (player.curhp, player.maxhp, spacer, monster.unitclass.title(), monster.curhp, monster.maxhp, playerHPBar, monsterHPBar, pb1, pb2))
    time.sleep(sleep)

def deathCombatScreen(player, monster, sleep):
    playerHPBar = getHPBar(player)
    monsterHPBar = getHPBar(monster)
    pb1, pb2 = personalBar(player)
    spacer = ' '
    if (len(str(player.curhp)) + len(str(player.maxhp))) > 4:
        spacer =  (' ' * ((len(str(player.curhp)) + len(str(player.maxhp))) - 4))
    if gameturn.playerDeath is True:
        deathInfo = 'You have been slain!'
    if gameturn.monsterDeath is True:
        deathInfo = 'The %s has been slain!' % monster.unitclass
    print('''


       You: %s/%s %s                                         %s: %s/%s
       %s                                         %s





                            
                            
                            %s
                                                                       
                                    







%s
%s
''' % (player.curhp, player.maxhp, spacer, monster.unitclass.title(), monster.curhp, monster.maxhp, playerHPBar, monsterHPBar, deathInfo, pb1, pb2))
    time.sleep(sleep)

def inCombatScreen(player, monster, attacksInTurn, sleep):
    playerHPBar = getHPBar(player)
    monsterHPBar = getHPBar(monster)
    pb1, pb2 = personalBar(player)
    spacer = ' '
    if (len(str(player.curhp)) + len(str(player.maxhp))) > 4:
        spacer =  (' ' * ((len(str(player.curhp)) + len(str(player.maxhp))) - 4))
    displayAttack   = { 1: ' ', 2: ' ', 3: ' ' }
    for i in range(len(attacksInTurn)):
        displayAttack[i] = attacksInTurn[i]
    print('''


       You: %s/%s %s                                         %s: %s/%s
       %s                                         %s
  




                            
                            
        %s
        %s
        %s   
                             
                                    





%s
%s
''' % (player.curhp, player.maxhp, spacer, monster.unitclass.title(), monster.curhp, monster.maxhp, playerHPBar, monsterHPBar, displayAttack[0], displayAttack[1], displayAttack[2], pb1, pb2))
    time.sleep(sleep)
    
    

def blankScreen(sleep):
        print('''







                            
                            


                             
                             
                                    









''')
        time.sleep(sleep)

def infoScreen(string, sleep):
    print('''










 
                              %s
                                    









''' % string)
    time.sleep(sleep)

def displayInventory(unit):
    itemslot = {}
    for i in range(1, 13):
        itemslot[i] = ' '
    for i in range(len(unit.inventory) + 1):
        itemslot[i] = '[' + unit.inventory[i - 1].name.title() + ']'
    print('''



                                  Inventory:


                    %s      |     %s      |     %s


                    %s      |     %s      |     %s 
                              
                                    
                    %s      |     %s      |     %s


                    %s      |     %s      |     %s




''' %  (itemslot[1], itemslot[2], itemslot[3], itemslot[4], itemslot[5], itemslot[6], itemslot[7], itemslot[8], itemslot[9], itemslot[10], itemslot[11], itemslot[12]))
