import levelingstats
import time
import main
import classes
import combatdisplay

    ###############################
    #     sets initial flags      #
    ###############################
    
unitGainLvl = False
playerDeath = False
monsterDeath = False
endCombat = False
gameTurnCount = 0

def flagCheck():

    global unitGainLvl
    global playerDeath
    global monsterDeath
    global endCombat

    ###############################
    #    checks for monster death #
    #    ends combat, and gives   #
    #           xp to winner      #
    ###############################

    if monsterDeath is True:
        endCombat = True
        classes.player.gainXP(classes.monster.giveXP())
        monsterDeath = False

    if playerDeath is True:
        endCombat = True

    ###############################
    #   checks for unit levelup   #
    #      and applies stats      #
    ###############################

    if unitGainLvl is True:
        classes.player.curlvl += 1
        classes.player.str    += levelingstats.levelStatInc[classes.player.unitclass][classes.player.curlvl][0]
        classes.player.con    += levelingstats.levelStatInc[classes.player.unitclass][classes.player.curlvl][1]
        classes.player.dex    += levelingstats.levelStatInc[classes.player.unitclass][classes.player.curlvl][2]
        classes.player.wis    += levelingstats.levelStatInc[classes.player.unitclass][classes.player.curlvl][3]
        classes.player.int    += levelingstats.levelStatInc[classes.player.unitclass][classes.player.curlvl][4]
        classes.player.cun    += levelingstats.levelStatInc[classes.player.unitclass][classes.player.curlvl][5]
        unitGainLvl = False
        combatdisplay.gainLevel()

def doGameTurn():
    global gameTurnCount
    gameTurnCount += 1
    flagCheck()
