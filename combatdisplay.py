import time
import random
import classes
import gameturn
import levelingstats

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

def personalBar():
    equipBar = getEquipBar(classes.creatures['player'])
    pb1 = '%s | XP: %s [%s/%s] | str: %s con:%s dex:%s wis:%s int:%s cun:%s | turn: %s' % (classes.creatures['player'].unitclass.title(), classes.creatures['player'].curlvl, classes.creatures['player'].curXP, levelingstats.xpToLevel[classes.creatures['player'].curlvl + 1], classes.creatures['player'].str, classes.creatures['player'].con, classes.creatures['player'].dex, classes.creatures['player'].wis, classes.creatures['player'].int, classes.creatures['player'].cun, gameturn.gameTurnCount)
    pb2 = equipBar
    return pb1, pb2

def blankCombatScreen(sleep):
    playerHPBar = getHPBar(classes.creatures['player'])
    monsterHPBar = getHPBar(classes.creatures['monster'])
    pb1, pb2 = personalBar()
    spacer = ' '
    if (len(str(classes.creatures['player'].curhp)) + len(str(classes.creatures['player'].maxhp))) > 4:
        spacer =  (' ' * ((len(str(classes.creatures['player'].curhp)) + len(str(classes.creatures['player'].maxhp))) - 4))
    print('''


       You: %s/%s %s                                         %s: %s/%s
       %s                                         %s




                                                        


                             
                             
                                    







%s
%s
''' % (classes.creatures['player'].curhp, classes.creatures['player'].maxhp, spacer, classes.creatures['monster'].unitclass.title(), classes.creatures['monster'].curhp, classes.creatures['monster'].maxhp, playerHPBar, monsterHPBar, pb1, pb2))
    time.sleep(sleep)

def deathCombatScreen(sleep):
    playerHPBar = getHPBar(classes.creatures['player'])
    monsterHPBar = getHPBar(classes.creatures['monster'])
    pb1, pb2 = personalBar()
    spacer = ' '
    if (len(str(classes.creatures['player'].curhp)) + len(str(classes.creatures['player'].maxhp))) > 4:
        spacer =  (' ' * ((len(str(classes.creatures['player'].curhp)) + len(str(classes.creatures['player'].maxhp))) - 4))
    if gameturn.playerDeath is True:
        deathInfo = 'You have been slain!'
    if gameturn.monsterDeath is True:
        deathInfo = 'The %s has been slain!' % classes.creatures['monster'].unitclass
    print('''


       You: %s/%s %s                                         %s: %s/%s
       %s                                         %s





                            
                            
                            %s
                                                                       
                                    







%s
%s
''' % (classes.creatures['player'].curhp, classes.creatures['player'].maxhp, spacer, classes.creatures['monster'].unitclass.title(), classes.creatures['monster'].curhp, classes.creatures['monster'].maxhp, playerHPBar, monsterHPBar, deathInfo, pb1, pb2))
    time.sleep(sleep)

def inCombatScreen(infostring, sleep):
    playerHPBar = getHPBar(classes.creatures['player'])
    monsterHPBar = getHPBar(classes.creatures['monster'])
    pb1, pb2 = personalBar()
    spacer = ' '
    if (len(str(classes.creatures['player'].curhp)) + len(str(classes.creatures['player'].maxhp))) > 4:
        spacer =  (' ' * ((len(str(classes.creatures['player'].curhp)) + len(str(classes.creatures['player'].maxhp))) - 4))
    print('''


       You: %s/%s %s                                         %s: %s/%s
       %s                                         %s
  




                            
                            
        
        %s
           
                             
                                    





%s
%s
''' % (classes.creatures['player'].curhp, classes.creatures['player'].maxhp, spacer, classes.creatures['monster'].unitclass.title(),
       classes.creatures['monster'].curhp, classes.creatures['monster'].maxhp, playerHPBar, monsterHPBar,
       infostring, pb1, pb2))
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

# wip

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
