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
