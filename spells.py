import random
import combat
import stringparse

spells = {
    #   name                    description       type    base   int scaling
    #   0                        1                 2       4      5
    'wizard': [
    ['fireball', 'casts a fireball at an enemy',  'dmg', (10,15), .6],
    [    'heal',             'heals the player', 'heal',   (6-8), .2],
    ]
    }

def castSpell(caster, defender, spellChoice):
    spellName       = spells[caster.unitclass][spellChoice][0]
    spellType       = spells[caster.unitclass][spellChoice][2]
    spellBaseMin    = spells[caster.unitclass][spellChoice][3][0]
    spellBaseMax    = spells[caster.unitclass][spellChoice][3][1]
    spellScale      = spells[caster.unitclass][spellChoice][4]
    spellMag = int(random.randint(spellBaseMin, spellBaseMax) + (caster.int * spellScale))
    spellInfo = spellName, spellType, spellBaseMin, spellBaseMax, spellScale, spellMag
    if spellType is 'dmg':              #i want this to be automated
        defender.curhp -= spellMag
    if spellType is 'heal':
        attacker.curhp += spellMag
    unitDeath = combat.determineDeath(defender)
    stringparse.castStringParse(caster, defender, spellInfo, unitDeath)
    return unitDeath
