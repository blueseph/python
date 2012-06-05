import time
import random
import savegame

def getHPBar(unit):
    if unit.curhp < 0:
        unit.curhp = 0
    HPBarString = ('[' + ('-' * round((unit.curhp / unit.maxhp) * 10) + (' ' * (10 - round((unit.curhp / unit.maxhp) * 10)) + ']' )))
    return HPBarString

def spawnPlayerScreen(input):
    arrow1 = ' '
    arrow2 = ' '
    arrow3 = ' '
    arrow4 = ' '
    if input == 1:
        arrow1 = '>'
    if input == 2:
        arrow2 = '>'
    if input == 3:
        arrow3 = '>'
    if input == 4:
        arrow4 = '>'
    print('''

 




                                choose ur dude
                                


%s                                  Berserker
                (Prefers two-handed combat. Sturdy and hits hard.)


%s                                  Warrior   
                    (Uses a sword and shield. Very sturdy.)


%s                                  Rogue     
                (Uses two weapons. Hits hard, but very frail)  


%s                                  Wizard    
                    (Prefers spells. Can heal and damage)


''' % (arrow1, arrow2, arrow3, arrow4))


def blankCombatScreen(sleep):
    playerHPBar = getHPBar(savegame.creatures['player'])
    monsterHPBar = getHPBar(savegame.creatures['monster'])
    pb1, pb2 = personalBar()
    spacer = ' '
    if (len(str(savegame.creatures['player'].curhp)) + len(str(savegame.creatures['player'].maxhp))) > 4:
        spacer =  (' ' * ((len(str(savegame.creatures['player'].curhp)) + len(str(savegame.creatures['player'].maxhp))) - 4))
    print('''


       You: %s/%s %s                                         %s: %s/%s
       %s                                         %s




                                                        


                             
                             
                                    







%s
%s
''' % (savegame.creatures['player'].curhp, savegame.creatures['player'].maxhp, spacer, savegame.creatures['monster'].unitclass.title(), savegame.creatures['monster'].curhp, savegame.creatures['monster'].maxhp, playerHPBar, monsterHPBar, pb1, pb2))
    time.sleep(sleep)

def deathCombatScreen(sleep):
    playerHPBar = getHPBar(savegame.creatures['player'])
    monsterHPBar = getHPBar(savegame.creatures['monster'])
    pb1, pb2 = personalBar()
    spacer = ' '
    if (len(str(savegame.creatures['player'].curhp)) + len(str(savegame.creatures['player'].maxhp))) > 4:
        spacer =  (' ' * ((len(str(savegame.creatures['player'].curhp)) + len(str(savegame.creatures['player'].maxhp))) - 4))
    if gameturn.playerDeath is True:
        deathInfo = 'You have been slain!'
    if gameturn.monsterDeath is True:
        deathInfo = 'The %s has been slain!' % savegame.creatures['monster'].unitclass
    print('''


       You: %s/%s %s                                         %s: %s/%s
       %s                                         %s





                            
                            
                            %s
                                                                       
                                    







%s
%s
''' % (savegame.creatures['player'].curhp, savegame.creatures['player'].maxhp, spacer, savegame.creatures['monster'].unitclass.title(), savegame.creatures['monster'].curhp, savegame.creatures['monster'].maxhp, playerHPBar, monsterHPBar, deathInfo, pb1, pb2))
    time.sleep(sleep)

def inCombatScreen(infostring, sleep):
    playerHPBar = getHPBar(savegame.creatures['player'])
    monsterHPBar = getHPBar(savegame.creatures['monster'])
    pb1, pb2 = personalBar()
    spacer = ' '
    if (len(str(savegame.creatures['player'].curhp)) + len(str(savegame.creatures['player'].maxhp))) > 4:
        spacer =  (' ' * ((len(str(savegame.creatures['player'].curhp)) + len(str(savegame.creatures['player'].maxhp))) - 4))
    print('''


       You: %s/%s %s                                         %s: %s/%s
       %s                                         %s
  




                            
                            
        
        %s
           
                             
                                    





%s
%s
''' % (savegame.creatures['player'].curhp, savegame.creatures['player'].maxhp, spacer, savegame.creatures['monster'].unitclass.title(),
       savegame.creatures['monster'].curhp, savegame.creatures['monster'].maxhp, playerHPBar, monsterHPBar,
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
