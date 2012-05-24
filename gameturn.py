import levelingstats
import time
import classes
import combatdisplay
import spells
import board

    ###############################
    #     sets initial flags      #
    ###############################
    
unitGainLvl = False
playerDeath = False
monsterDeath = False
endCombat = False
deathblow = False
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
        classes.creatures['player'].gainXP(classes.creatures['monster'].giveXP())
        del classes.creatures['monster']
        monsterDeath = False

    if playerDeath is True:
        endCombat = True

    ###############################
    #   checks for unit levelup   #
    #      and applies stats      #
    ###############################

    if unitGainLvl is True:
        classes.creatures['player'].curlvl += 1
        classes.creatures['player'].str    += levelingstats.levelStatInc[classes.creatures['player'].unitclass][classes.creatures['player'].curlvl][0]
        classes.creatures['player'].con    += levelingstats.levelStatInc[classes.creatures['player'].unitclass][classes.creatures['player'].curlvl][1]
        classes.creatures['player'].dex    += levelingstats.levelStatInc[classes.creatures['player'].unitclass][classes.creatures['player'].curlvl][2]
        classes.creatures['player'].wis    += levelingstats.levelStatInc[classes.creatures['player'].unitclass][classes.creatures['player'].curlvl][3]
        classes.creatures['player'].int    += levelingstats.levelStatInc[classes.creatures['player'].unitclass][classes.creatures['player'].curlvl][4]
        classes.creatures['player'].cun    += levelingstats.levelStatInc[classes.creatures['player'].unitclass][classes.creatures['player'].curlvl][5]
        classes.creatures['player'].calculateStats()
        classes.creatures['player'].curhp  = classes.creatures['player'].maxhp
        unitGainLvl = False
        combatdisplay.infoScreen('You feel more experienced!', 1.5)
        combatdisplay.infoScreen('You have reached level %s!' % classes.creatures['player'].curlvl, 1.5)

def doGameTurn():
    global gameTurnCount
    gameTurnCount += 1

    spellsToRemove = []
    buffsToRemove = []
    for creature in classes.creatures:

    ###############################
    #    reduce spell cooldowns   #
    ###############################

        for spell in classes.creatures[creature].spellCooldowns:
            classes.creatures[creature].spellCooldowns[spell] -= 1
            if classes.creatures[creature].spellCooldowns[spell] < 0:
                spellsToRemove.append(spell)
        for spell in spellsToRemove:
            del classes.creatures[creature].spellCooldowns[spell]

    ###############################
    #    reduce buff duration     #
    ###############################

        for buff in classes.creatures[creature].buffDuration:
            classes.creatures[creature].buffDuration[buff] =- 1
            if classes.creatures[creature].buffDuration[buff] < 0:
                BuffsToRemove.append(buff)
        for buff in classes.creatures[creature].initBuffs:
            if buff in buffsToRemove:
                classes.creatures[creature].initBuffs.remove(buff)
        for buff in classes.creatures[creature].midBuffs:
            if buff in buffsToRemove:
                classes.creatures[creature].midBuffs.remove(buff)
        for buff in classes.creatures[creature].endBuffs:
            if buff in buffsToRemove:
                classes.creatures[creature].endBuffs.remove(buff) 
        for buff in buffsToRemove:
            del classes.creatures[creature].buffDuration[buff]
        classes.creatures[creature].resetStats()

    flagCheck()
    board.current_dungeon_map[1].draw()