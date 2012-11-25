import time
import random
import savegame

def bottomMenu():
    fl = '      Character    |   Inventory   |   Abilities   |    Spells    |   Menu'
    sl = '         [c]       |      [i]      |      [z]      |      [Z]     |   [m]'
    return fl, sl

def inventoryScreen(arrow=1, invarrow=0):
    spacer1 = spacer2 = spacer3 = spacer4 = spacer5 = ' ' * 42
    realItemDict = {}
    itNum = 1
    itemDict = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' '}
    for item in savegame.creatures['player'].inventory:
        itemDict[itNum] = item.name
        realItemDict[itNum] = item
        itNum += 1
    invarrowDict = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' '}
    spacer1 = ' ' * abs((len(str(itemDict[1])) - 42))
    spacer2 = ' ' * abs((len(str(itemDict[3])) - 42))
    spacer3 = ' ' * abs((len(str(itemDict[5])) - 42))
    spacer4 = ' ' * abs((len(str(itemDict[7])) - 42))
    spacer5 = ' ' * abs((len(str(itemDict[9])) - 42))
    arrowDict = {1: ' ', 2: ' ', 3: ' ', 4: ' '}
    arrowDict[arrow] = '>'
    invarrowDict[invarrow] = '>'
    fl, sl = bottomMenu()
    print('''
        
 ---------------------------------------------------------------------------------------
            %s Use           %s Description           %s Sort           %s Drop
 ---------------------------------------------------------------------------------------



 
        %s %s%s %s %s                               


        %s %s%s %s %s        
   

        %s %s%s %s %s          

  
        %s %s%s %s %s         

 
        %s %s%s %s %s             




  %s
  %s''' % (arrowDict[1], arrowDict[2], arrowDict[3], arrowDict[4], invarrowDict[1], itemDict[1], spacer1, invarrowDict[2], itemDict[2], invarrowDict[3], itemDict[3], spacer2, invarrowDict[4], itemDict[4], invarrowDict[5], itemDict[5], spacer3, invarrowDict[6], itemDict[6], invarrowDict[7], itemDict[7], spacer4, invarrowDict[8], itemDict[8], invarrowDict[9], itemDict[9], spacer5, invarrowDict[10], itemDict[10], fl, sl))

def characterScreen():
    classSpacer = ' ' * abs((len(str(savegame.creatures['player'].unitclass))) - 45)
    mainhandSpacer = ' ' * abs((len(str(savegame.creatures['player'].mainhand.name)) + len(str(savegame.creatures['player'].mainhand.min)) + len(str(savegame.creatures['player'].mainhand.max))) - 23) 

    ###############################
    #          stats panel        #
    ###############################

    #           damage range

    if savegame.creatures['player'].offhand.type is not 'shield':
        damageRangeMin = int((savegame.creatures['player'].mainhand.min + savegame.creatures['player'].dmg) + ((savegame.creatures['player'].offhand.min + savegame.creatures['player'].dmg)/2))
        damageRangeMax = int((savegame.creatures['player'].mainhand.max + savegame.creatures['player'].dmg) + ((savegame.creatures['player'].offhand.max + savegame.creatures['player'].dmg)/2))
    else:
        damageRangeMin = int((savegame.creatures['player'].mainhand.min + savegame.creatures['player'].dmg))
        damageRangeMax = int((savegame.creatures['player'].mainhand.max + savegame.creatures['player'].dmg))
    damageSpacer = ' ' * abs(len(str(damageRangeMin)) + len(str(damageRangeMax)) - 2)

    #           total ac

    totalAC = savegame.creatures['player'].chestArmor.armorClass

    ###############################
    #           offhand           #
    ###############################

    offhandStats = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' '}
    if savegame.creatures['player'].offhand.type is '1h':
        offhandStats[1] = 'Offhand:'
        offhandStats[2] = savegame.creatures['player'].offhand.name
        offhandStats[3] = '('
        offhandStats[4] = savegame.creatures['player'].offhand.min
        offhandStats[5] = '-'
        offhandStats[6] = savegame.creatures['player'].offhand.max
        offhandSpacer = ' ' * abs((len(str(savegame.creatures['player'].offhand.name)) + len(str(savegame.creatures['player'].offhand.min)) + len(str(savegame.creatures['player'].offhand.max))) - 23)
        offhandStats[7] = ')'
    elif savegame.creatures['player'].offhand.type is 'shield':
        offhandStats[1] = 'Offhand:'
        offhandStats[2] = savegame.creatures['player'].offhand.name
        offhandStats[3] = '('
        offhandStats[4] = savegame.creatures['player'].offhand.blockValue
        offhandStats[5] = ''
        offhandStats[6] = 'block'
        offhandStats[7] = ')'
        offhandSpacer = ' ' * abs((len(str(savegame.creatures['player'].offhand.name)) + len(str(savegame.creatures['player'].offhand.blockValue))) - 19)
    else:
        offhandSpacer = ' ' * abs((len(str(savegame.creatures['player'].offhand.name))) - 28)

    ###############################
    #           chest             #
    ###############################

    chestArmor = {1: savegame.creatures['player'].chestArmor.name, 2: ' ', 3: ' ', 4: ' ', 5: ' '}
    if chestArmor[1] is not 'Empty':
        chestArmor[2] = '('
        chestArmor[3] = savegame.creatures['player'].chestArmor.armorClass
        chestArmor[4] = 'ac'
        chestArmor[5] = ')'
        chestSpacer = ' ' * abs((len(str(savegame.creatures['player'].chestArmor.name)) + len(str(savegame.creatures['player'].chestArmor.armorClass))) - 26)

    print('''

%s Level %s %s
   

   _________________________       __________________________________________________
   |                       |       |                                                |
   |   Strength:        %s  |       |       Mainhand: %s   (%s - %s)%s|
   |   Consitution:     %s  |       |       %s  %s   %s%s %s %s%s%s|
   |   Dexterity:       %s  |       |                                                |
   |   Wisdom:          %s  |       |       Gloves:                                  |
   |   Intelligence:    %s  |       |       Chest:   %s %s%s %s%s%s|
   |   Cunning:         %s  |       |       Boots:                                   |
   |                       |       |                                                |
   |                       |       |                                                |
   |   Damage:  (%s - %s)%s|       |                                                |
   |   Armor:       %s      |       |                                                |
   |_______________________|       |________________________________________________|               
   ______________________________________       ______________________________________  
   |               Abilities            |       |               Spells               |
   |                                    |       |                                    |
   |                                    |       |                                    |
   |                                    |       |                                    |
   |                                    |       |                                    |
   |                                    |       |                                    |
   |                                    |       |                                    |
   |                                    |       |                                    |
   |____________________________________|       |____________________________________|''' % (classSpacer, savegame.creatures['player'].curlvl, savegame.creatures['player'].unitclass.title(), savegame.creatures['player'].str, savegame.creatures['player'].mainhand.name, 
        savegame.creatures['player'].mainhand.min, savegame.creatures['player'].mainhand.max, mainhandSpacer, savegame.creatures['player'].con, offhandStats[1], offhandStats[2], offhandStats[3], 
        offhandStats[4], offhandStats[5], offhandStats[6], offhandStats[7], offhandSpacer, savegame.creatures['player'].dex, savegame.creatures['player'].wis, savegame.creatures['player'].int, 
        chestArmor[1], chestArmor[2], chestArmor[3], chestArmor[4], chestArmor[5], chestSpacer, savegame.creatures['player'].cun, damageRangeMin, damageRangeMax, damageSpacer, totalAC))

def spawnPlayerScreen(arrow=1):
    arrowDict = {1: ' ', 2: ' ', 3: ' ', 4: ' '}
    arrowDict[arrow] = '>'
    print('''

 



                                        Choose your class
                                


        %s                                  Berserker
                        (Prefers two-handed combat. Sturdy and hits hard.)


        %s                                  Warrior   
                            (Uses a sword and shield. Very sturdy.)


        %s                                  Rogue     
                        (Uses two weapons. Hits hard, but very frail)  


        %s                                  Wizard    
                            (Prefers spells. Can heal and damage)




''' % (arrowDict[1], arrowDict[2], arrowDict[3], arrowDict[4]))

def infoScreen(string, sleep):
    print('''












 
                              %s
                                    











''' % string)
    time.sleep(sleep)
