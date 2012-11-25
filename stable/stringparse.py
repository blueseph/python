import time

def meleeStringParse(attacker, defender, critRoll, apRoll, wepTotDmg, blockRoll):
    if attacker.type is 'player':
        if critRoll is True or apRoll is True:
            initialString = ('You attack')
        else:
            initialString = ('You attack.')
        if critRoll[1] is True:
            initialString = initialString + (' critically!')
        if apRoll is True and critRoll[1] is True:
            initialString = initialString + (' You find a weakspot!')
        elif apRoll is True and critRoll[1] is False:
            initialString = initialString + ('. You find a weakspot!')
        if blockRoll is True:
            initialString = initialString + (' It blocks some damage!')
        initialString = initialString + (' You did %s damage.' % wepTotDmg)
        if wepTotDmg <= 0:
            initialString = ('You attack. The attack does no damage.')
    elif attacker.type is 'monster':
        if critRoll[1] is True or apRoll is True:
            initialString = ('The %s strikes' % attacker.type)
        else:
            initialString = ('The %s attacks.' % attacker.type)
        if critRoll[1] is True:
            initialString = initialString + (' critically!')
        if apRoll is True and critRoll[1] is True:
            initialString = initialString + (' It finds a weakspot!')
        elif apRoll is True and critRoll[1] is False:
            initialString = initialString + ('. It find a weakspot!')
        if blockRoll is True:
            initialString = initialString + (' You block some damage!')
        initialString = initialString + (' The %s did %s damage.' % (attacker.type, wepTotDmg))
        if wepTotDmg <= 0:
            initialString = ('The %s attacks. The attack does no damage.' % attacker.type)
    time.sleep(.5)
    return initialString

def castStringParse(caster, defender, spell, spellmag):
    if caster.type is 'player':
        initialString = ('You cast %s.' % spell.name)
        if spell.type is 'dmg':
            initialString += (' It does %s damage.' % spellmag)
        elif spell.type is 'heal':
            initialString += (' It restores %s hitpoints.' % spellmag)
    elif caster.type is 'monster':
        initialString = ('The %s casts %s.' % (attacker.type, spell.name))
        if spell.type is 'dmg':
            initialString += (' It does %s damage.' % spellmag)
        elif spell.type is 'heal':
            initialString += ('It restores %s hitpoints.' % spellmag)
    return initialString

