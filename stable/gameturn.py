import levelingstats, time, combatdisplay, spells, random, savegame, classes

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
        monsterToDel = []
        for creature in savegame.creatures:
            if savegame.creatures[creature].curhp <= 0:
                savegame.creatures['player'].gainXP(savegame.creatures[creature].giveXP())
                monsterToDel.append(creature)
        monsterDeath = False
        for creature in monsterToDel:
            del savegame.creatures[creature]

    if playerDeath is True:
        time.sleep(1.5)
        combatdisplay.infoScreen('You have died', 5)

    ###############################
    #   checks for unit levelup   #
    #      and applies stats      #
    ###############################

    if unitGainLvl is True:
        savegame.creatures['player'].curlvl += 1
        savegame.creatures['player'].str    += levelingstats.levelStatInc[savegame.creatures['player'].unitclass][savegame.creatures['player'].curlvl][0]
        savegame.creatures['player'].con    += levelingstats.levelStatInc[savegame.creatures['player'].unitclass][savegame.creatures['player'].curlvl][1]
        savegame.creatures['player'].dex    += levelingstats.levelStatInc[savegame.creatures['player'].unitclass][savegame.creatures['player'].curlvl][2]
        savegame.creatures['player'].wis    += levelingstats.levelStatInc[savegame.creatures['player'].unitclass][savegame.creatures['player'].curlvl][3]
        savegame.creatures['player'].int    += levelingstats.levelStatInc[savegame.creatures['player'].unitclass][savegame.creatures['player'].curlvl][4]
        savegame.creatures['player'].cun    += levelingstats.levelStatInc[savegame.creatures['player'].unitclass][savegame.creatures['player'].curlvl][5]
        savegame.creatures['player'].calculateStats()
        savegame.creatures['player'].curhp  = savegame.creatures['player'].maxhp
        unitGainLvl = False
        combatdisplay.infoScreen('You feel more experienced!', 1.5)
        combatdisplay.infoScreen('You have reached level %s!' % savegame.creatures['player'].curlvl, 1.5)

def doGameTurn():
    global gameTurnCount
    gameTurnCount += 1
    flagCheck()

    spellsToRemove = []
    buffsToRemove = []
    for creature in savegame.creatures:

    ###############################
    #    reduce spell cooldowns   #
    ###############################

        for spell in savegame.creatures[creature].spellCooldowns:
            savegame.creatures[creature].spellCooldowns[spell] -= 1
            if savegame.creatures[creature].spellCooldowns[spell] < 0:
                spellsToRemove.append(spell)
        for spell in spellsToRemove:
            del savegame.creatures[creature].spellCooldowns[spell]

    ###############################
    #    reduce buff duration     #
    ###############################

        for buff in savegame.creatures[creature].buffDuration:
            savegame.creatures[creature].buffDuration[buff] =- 1
            if savegame.creatures[creature].buffDuration[buff] < 0:
                BuffsToRemove.append(buff)
        for buff in savegame.creatures[creature].initBuffs:
            if buff in buffsToRemove:
                savegame.creatures[creature].initBuffs.remove(buff)
        for buff in savegame.creatures[creature].midBuffs:
            if buff in buffsToRemove:
                savegame.creatures[creature].midBuffs.remove(buff)
        for buff in savegame.creatures[creature].endBuffs:
            if buff in buffsToRemove:
                savegame.creatures[creature].endBuffs.remove(buff) 
        for buff in buffsToRemove:
            del savegame.creatures[creature].buffDuration[buff]
        savegame.creatures[creature].resetStats() # doesnt work correctly

    ###############################
    #       creature move         #
    ###############################

        if creature is 'player':
            pass
        else:
            if (abs((savegame.creatures[creature].xPos - savegame.creatures['player'].xPos)) + abs(savegame.creatures[creature].yPos - savegame.creatures['player'].yPos)) < 20:
                yPosition, xPosition = savegame.creatures[creature].pathfind()
                xPosition -= savegame.creatures[creature].xPos
                yPosition -= savegame.creatures[creature].yPos
                savegame.creatures[creature].move(xPosition, yPosition)

    ###############################
    #         spawn mobs          #
    ###############################

    if gameTurnCount % 3 == 0:  
        spawnFailed = 0
        while spawnFailed is not 2:
            if random.randint(1, 100) <= (70/len(savegame.creatures)):
                classes.spawnMonster()
            else:
                spawnFailed += 1

    savegame.current_dungeon_map[1].draw()