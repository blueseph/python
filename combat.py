import random
import time
import classes
import stringparse
import spells
import combatdisplay

def decideTurn(player, monster):
    playerWeight = player.weight
    monsterWeight = monster.weight
    if (playerWeight - monsterWeight) > 0:
        initiator = classes.monster
        defender = classes.player
        if playerWeight//monsterWeight < 1:
            tpr = 1
        elif playerWeight//monsterWeight > 3:
            tpr = 3
        else:
            tpr = playerWeight//monsterWeight
    elif (playerWeight - monsterWeight) < 0:
        initiator = classes.player
        defender = classes.monster
        if (monsterWeight//playerWeight * -1) < 1:
            tpr = 1
        elif (monsterWeight//playerWeight * -1) > 3:
            tpr = 3
        else:
            tpr = monsterWeight//playerWeight * -1
    else:
        initiator = classes.player
        defender = classes.monster
        tpr = 1
    return tpr, initiator, defender

def meleeAttack(attacker, defender):
    offhand = False
    unitDeath = (False, 'nobody')
    attackType = 'melee'
    if attacker.offhand is not None:
        offhand = attacker.offhand
    wepMhDmg, wepOhDmg = getDmgRoll(attacker)
    unitHasCrit = attackCrit(attacker)
    unitHasDodged = cunningDodge(defender)
    unitHasBlocked = blockAttack(defender)
    unitCunAtk = cunningAttack(attacker)
    if unitHasBlocked is True:
        wepMhDmg -= defender.offhandBlockValue
        wepOhDmg -= defender.offhandBlockValue
    if unitCunAtk is False:
        wepMhDmg -= int(defender.armorClass/1.6)
        wepOhDmg -= int(defender.armorClass/1.6)
    if unitHasCrit[0] is True:
        if unitHasCrit[1] is True:
            wepMhDmg *= attacker.mainhandCrit
        elif unitHasCrit[0] is True:
            wepOhDmg *= attacker.offhandCrit
    if wepOhDmg < 0:
        wepOhDmg = 0
    wepTotDmg = int(wepMhDmg) + int(wepOhDmg/2)
    if wepTotDmg < 0:
        wepTotDmg = 0
    if unitHasDodged == True:
        wepTotDmg = 0
    defender.curhp -= wepTotDmg
    unitDeath = determineDeath(defender)
    damageInfo = (unitHasDodged, unitHasCrit, unitCunAtk, unitDeath, wepTotDmg, unitHasBlocked, attackType)
    return unitDeath, damageInfo

def determineDeath(defender):
    unitDeath = (False, 'nobody')
    if defender.curhp <= 0:
        if defender.type is 'monster':
            unitDeath = (True, 'monster')
        else:
            unitDeath = (True, 'player')
    return unitDeath

def getDmgRoll(unit):
    wepOhDmg = 0
    wepMhDmg = random.randint(unit.mainhandWepMin, unit.mainhandWepMax) + unit.dmg
    if unit.offhand is not None and unit.offhand is not 'shield':
        wepOhDmg = random.randint(unit.offhandWepMin, unit.offhandWepMax) + unit.dmg
    return wepMhDmg, wepOhDmg

def attackCrit(unit):
    unitHasCrit = False
    unitOffhandCrit = False
    unitMainhandCrit = False
    unitCritMod = unit.dex//4
    if (random.randint(1, 20) <= (unitCritMod + unit.mainhandCrit)):
            unitMainhandCrit = True
    if unit.offhand is not None and unit.offhand is not 'shield':
        if (random.randint(1, 20) <= (unitCritMod + unit.offhandCrit)):
            unitOffhandCrit = True
    if unitMainhandCrit is True or unitOffhandCrit is True:
            unitHasCrit = True
    return unitHasCrit, unitMainhandCrit, unitOffhandCrit

def blockAttack(unit):
        unitHasBlocked = False
        if unit.offhand is 'shield':
            if random.randint(1, 10) <= unit.offhandBlockChance:
                unitHasBlocked = True
        return unitHasBlocked
	
def cunningDodge(unit):
    unitHasDodged = False
    if (random.randint(1, 20)  <= (unit.cun//3)):
        unitHasDodged = True
    return unitHasDodged

def cunningAttack(unit):
    unitCunAtk = False
    if (random.randint(1, 20)  <= (unit.cun//3)):
        unitCunAtk = True
    return unitCunAtk
        
def combatTurn(tpr, attacker, defender):
    attackInTurn = {}
    if defender.curhp > 0 and attacker.curhp > 0:
        for i in range(tpr):
            if attacker.unitclass is 'wizard':
                unitDeath, spellInfo  = spells.castSpell(attacker, defender, 0)
                initialString = stringparse.castStringParse(attacker, defender, spellInfo)
            else:
                unitDeath, damageInfo = meleeAttack(attacker, defender)
                initialString = stringparse.meleeStringParse(defender, attacker, damageInfo)
            attackInTurn[i] = initialString
            if unitDeath[0] is True:
                break
    return unitDeath, attackInTurn
            
def fight():
    combatdisplay.drawEnemyApproachesWindow()
    time.sleep(2)
    combatdisplay.drawInitialCombatWindow(classes.player, classes.monster)
    time.sleep(2)
    tpr, initiator, defender =  decideTurn(classes.player, classes.monster)
    while classes.player.curhp > 0 and classes.monster.curhp > 0:
        unitDeath, attackInTurn = combatTurn(tpr, initiator, defender)
        combatdisplay.drawInCombatWindow(classes.player, classes.monster, attackInTurn)
        time.sleep(1.5)
        if unitDeath[0] is True:
            time.sleep(1)
            combatdisplay.drawDeathWindow(classes.player, classes.monster, unitDeath)
            time.sleep(2.5)
            break
        unitDeath, attackInTurn = combatTurn(1, defender, initiator)
        combatdisplay.drawInCombatWindow(classes.player, classes.monster, attackInTurn)
        time.sleep(1.5)
        if unitDeath[0] is True:
            time.sleep(1)
            combatdisplay.drawDeathWindow(classes.player, classes.monster, unitDeath)
            time.sleep(2.5) 
            break
        time.sleep(1)
    return unitDeath
