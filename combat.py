import random
import time
import classes
import stringparse
import combatdisplay
import gameturn

def decideTurn(player, monster):
    playerWeight = player.weight
    monsterWeight = monster.weight
    if (playerWeight - monsterWeight) > 0:
        initiator = classes.creatures['monster']
        defender = classes.creatures['player']
    elif (playerWeight - monsterWeight) < 0:
        initiator = classes.creatures['player']
        defender = classes.creatures['monster']
    else:
        initiator = classes.creatures['player']
        defender = classes.creatures['monster']
    return initiator, defender

def determineDeath(defender):
    if defender.curhp <= 0:
        if defender.type is 'monster':
            gameturn.monsterDeath = True
            gameturn.deathblow = True
        elif defender.type is 'player':
            gameturn.playerDeath = True

        
def combatTurn(attacker, defender):
    if defender.curhp > 0 and attacker.curhp > 0:
        if attacker.atype is 'magic':
            spellToCast = attacker.getSpellToCast()
            attacker.cast(spellToCast, defender)
        else:
            attacker.melee(defender)
            
def fight():
    gameturn.endCombat = False
    combatdisplay.infoScreen('An enemy approaches!', 2)
    combatdisplay.blankCombatScreen(2)
    initiator, defender =  decideTurn(classes.creatures['player'], classes.creatures['monster'])
    while gameturn.endCombat is False:
        combatTurn(initiator, defender)
        if gameturn.playerDeath is True or gameturn.monsterDeath is True:
            time.sleep(1)
            combatdisplay.deathCombatScreen(2.5)
            gameturn.doGameTurn()
            break
        combatTurn(defender, initiator)
        if gameturn.playerDeath is True or gameturn.monsterDeath is True:
            time.sleep(1)
            combatdisplay.deathCombatScreen(2.5)
            gameturn.doGameTurn()
            break
        gameturn.doGameTurn()
        time.sleep(1)
