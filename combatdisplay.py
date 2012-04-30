import time
import random
import classes
import gameturn

tempWords = ('bam pow ouch splat slam slice crack wham whack').split()

def gainLevel():
    print('''







                            You feel more experienced!
                            


 
                              
                                    









''')
    time.sleep(1)
    print('''







                            You feel more experienced!
                            You are now level %s.


 
                              
                                    









''' % classes.player.curlvl)

def displayInventory(unit):
    evenout = {}
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
    

def drawDeathWindow(player, monster):
    playerHPBar = getHPBar(player)
    monsterHPBar = getHPBar(monster)
    if gameturn.playerDeath is True:
        print('         You: %s/%s' % (player.curhp, player.maxhp))
        print('         %s' % playerHPBar)
        print('''



                            You have been slain!





''')
        print('                                                       %s: %s/%s' % (monster.unitclass.title(), monster.curhp, monster.maxhp))
        print('                                                       %s' % monsterHPBar)
        print('''





''')

    elif gameturn.monsterDeath:
        print('         You: %s/%s' % (player.curhp, player.maxhp))
        print('         %s' % playerHPBar)
        print('''



                             The %s has been slain!





''' % monster.unitclass )
        print('                                                       %s: %s/%s' % (monster.unitclass.title(), monster.curhp, monster.maxhp))
        print('                                                       %s' % monsterHPBar)
        print('''





''')

def drawEnemyApproachesWindow():
    print('''










 
                              An enemy approaches!
                                    









''')

def drawInitialCombatWindow(player, monster):
    playerHPBar     = getHPBar(player)
    playerEquipBar  = getEquipBar(player)
    monsterHPBar    = getHPBar(monster)
    monsterEquipBar = getEquipBar(monster)
    print('         You: %s/%s' % (player.curhp, player.maxhp))
    print('         %s' % playerHPBar)
    print('''








''')
    print('                                                       %s: %s/%s' % (monster.unitclass.title(), monster.curhp, monster.maxhp))
    print('                                                       %s' % monsterHPBar)
    print('''






''')



def drawInCombatWindow(player, monster, attacksInTurn):
    playerHPBar     = getHPBar(player)
    playerEquipBar  = getEquipBar(player)
    monsterHPBar    = getHPBar(monster)
    monsterEquipBar = getEquipBar(monster)
    displayAttack   = { 1: ' ', 2: ' ', 3: ' ' }
    for i in range(len(attacksInTurn)):
        displayAttack[i] = attacksInTurn[i]
    print(' ')
    print(' ')
    print('         You: %s/%s' % (player.curhp, player.maxhp))
    print('         %s' % playerHPBar)
    print('''

''')
    print('                                    ' + tempWords[random.randint(0,(len(tempWords) - 1))].upper() + '!')
    print('''




''')
    print('                                                       %s: %s/%s' % (monster.unitclass.title(), monster.curhp, monster.maxhp))
    print('                                                       %s' % monsterHPBar)
    print('''



''')
    print('         %s' % displayAttack[0])
    print('         %s' % displayAttack[1])
    print('         %s' % displayAttack[2])

    
def getHPBar(unit):
    if unit.curhp < 0:
        unit.curhp = 0
    HPBarString = ('[' + ('-' * round((unit.curhp / unit.maxhp) * 10) + (' ' * (10 - round((unit.curhp / unit.maxhp) * 10)) + ']' )))
    return HPBarString

def getEquipBar(unit):
    if unit.type is 'player':
        equipUnit = 'you'
    else:
        equipUnit = unit.unitclass
    if unit.offhand is not None:
        equipBar = ('%s: %s (mainhand), %s (offhand, %s (%s ac)' % (equipUnit.title(), unit.mainhandWeaponName, unit.offhandItemName, unit.armorName, unit.armorClass))
    elif unit.mainhand is '2h':
         equipBar = ('%s: %s (two-handed), %s (%s ac)' % (equipUnit.title(), unit.mainhandWeaponName, unit.armorName, unit.armorClass))
    else:
         equipBar = ('%s: %s (mainhand), %s (%s ac)' % (equipUnit.title(), unit.mainhandWeaponName, unit.armorName, unit.armorClass))
    return equipBar
