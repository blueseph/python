import random
import time
import classes
import stringparse
import spells

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
    stringparse.meleeStringParse(unitHasDodged, unitHasCrit, unitCunAtk, defender, attacker, unitDeath, wepTotDmg, unitHasBlocked)
    return unitDeath

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
        
def gameTurn(tpr, attacker, defender):
    if defender.curhp > 0 and attacker.curhp > 0:
        for i in range(tpr):
            if attacker.unitclass is 'wizard':
                unitDeath = spells.castSpell(attacker, defender, 0)
            else:
                unitDeath = meleeAttack(attacker, defender)
            if unitDeath[0] is True:
                break
    return unitDeath
            
def fight():
    print(' ')
    print('An enemy approaches!')
    print(' ')
    time.sleep(1)
    print('Equipment:')
    time.sleep(1)
    if classes.player.offhand is not None:
        print('You: %s (mainhand), %s (offhand), %s (%s ac)' % (classes.player.mainhandWeaponName, classes.player.offhandItemName, classes.player.armorName, classes.player.armorClass))
    elif classes.player.mainhand is '2h':
        print('You: %s (two-handed), %s (%s ac)' % (classes.player.mainhandWeaponName, classes.player.armorName, classes.player.armorClass))
    else:
        print('You: %s (mainhand), %s (%s ac)' % (classes.player.mainhandWeaponName, classes.player.armorName, classes.player.armorClass))
    time.sleep(.5)
    if classes.monster.offhand is not None:
        print('%s: %s (mainhand), %s (offhand), %s (%s ac)' % (classes.monster.clas, classes.monster.mainhandWeaponName, classes.monster.offhandItemName, classes.monster.armorName, classes.monster.armorClass))
    elif classes.monster.mainhand is '2h':
        print('%s: %s (two-handed), %s (%s ac)' % (classes.monster.unitclass, classes.monster.mainhandWeaponName, classes.monster.armorName, classes.monster.armorClass))
    else:
        print('%s: %s (mainhand), %s (%s ac)' % (classes.monster.unitclass, classes.monster.mainhandWeaponName, classes.monster.armorName, classes.monster.armorClass))
    stringparse.dispHP(classes.player.curhp, classes.player.maxhp, classes.monster.curhp, classes.monster.maxhp)
    time.sleep(1)
    tpr, initiator, defender =  decideTurn(classes.player, classes.monster)
    while classes.player.curhp > 0 and classes.monster.curhp > 0:
        unitDeath = gameTurn(tpr, initiator, defender)
        if unitDeath[0] is True:
            stringparse.dispHP(classes.player.curhp, classes.player.maxhp, classes.monster.curhp, classes.monster.maxhp)
            break
        time.sleep(.5)
        unitDeath = gameTurn(1, defender, initiator)
        stringparse.dispHP(classes.player.curhp, classes.player.maxhp, classes.monster.curhp, classes.monster.maxhp)
    return unitDeath
