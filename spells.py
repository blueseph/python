import random
import combat
import stringparse
from operator import itemgetter

spells = {
    #                          description                 type    base    scaling  cd   prior
    #                            0                           1       2        3      4    5
    'wizard': {
           'fireball':  ('casts a fireball at an enemy',  'dmg', (10, 15),   2.5,     6,  9),
      'magic missile':         ('casts a magic missile',  'dmg', (4,  8),    1.8,     0,  5),
               'heal':              ('heals the player', 'heal', (10, 15),     2,    12,  0),
    }
    }

spellCooldowns = {}        

def getSpellAvail(spell):

    ###############################
    # if cd is either not listed  #
    #  or 0, spell is available   #
    ###############################
    
    try:
        if spellCooldowns[spell] is not 0:
            return False
        else:
            return True
    except:
        return True

def useHeal(caster):

    ###############################
    #   use heal when it is most  #
    #          effecient          #
    ###############################
    
    castHeal = False
    avgHealAmt = (((spells[caster.unitclass]['heal'][2][0] + spells[caster.unitclass]['heal'][2][1]) / 2) + (caster.int * spells[caster.unitclass]['heal'][3]))
    if caster.curhp < (caster.maxhp - avgHealAmt):
        castHeal = getSpellAvail('heal')
    return castHeal

def getSpellToCast(caster):
    spellToCast = ''
    castHeal = useHeal(caster)
    if castHeal is True:
        spellToCast = 'heal'
    if castHeal is False:
        spellPriority = []

        ###############################
        # checks spell with highest   #
        # priority for cd, then casts #
        ###############################
    
        for i in spells[caster.unitclass]:
            spellPriority.append((i, spells[caster.unitclass][i][5]))
        spellPriority = sorted(spellPriority, key=itemgetter(1), reverse=True)
        for i in range(len(spellPriority)):
            if getSpellAvail(spellPriority[i][0]) is True:
                spellToCast = spellPriority[i][0]
                break
            else:
                pass
    return spellToCast

def castSpell(caster, defender, spellChoice):
    spellName       = spellChoice
    spellType       = spells[caster.unitclass][spellChoice][1]
    spellBaseMin    = spells[caster.unitclass][spellChoice][2][0]
    spellBaseMax    = spells[caster.unitclass][spellChoice][2][1]
    spellScale      = spells[caster.unitclass][spellChoice][3]
    spellCooldown   = spells[caster.unitclass][spellChoice][4]
    spellMag = int(random.randint(spellBaseMin, spellBaseMax) + (caster.int * spellScale))
    spellInfo = spellName, spellType, spellBaseMin, spellBaseMax, spellScale, spellMag
    if spellType is 'dmg':              #i want this to be automated
        defender.curhp -= spellMag
    if spellType is 'heal':
        caster.curhp += spellMag
        if caster.curhp > caster.maxhp:
            caster.curhp = caster.maxhp
    combat.determineDeath(defender)
    spellCooldowns[spellName] = spellCooldown
    return spellInfo
        

    
