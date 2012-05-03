import time

def meleeStringParse(defender, attacker, damageInfo):
    if attacker.type is 'player':
        if damageInfo[1][1] is True or damageInfo[2] is True:
            initialString = ('You attack')
        else:
            initialString = ('You attack.')
        if damageInfo[1][1] is True:
            initialString = initialString + (' critically!')
        if damageInfo[2] is True and damageInfo[1][1] is True:
            initialString = initialString + (' You find a weakspot!')
        elif damageInfo[2] is True and damageInfo[1][1] is False:
            initialString = initialString + ('. You find a weakspot!')
        if damageInfo[4] is True:
            initialString = initialString + (' It blocks some damage!')
        initialString = initialString + (' You did %s damage.' % damageInfo[3])
        if damageInfo[3] <= 0:
            initialString = ('You attack. The attack does no damage.')
        if damageInfo[0] is True:
            initialString = ('You attack. The %s dodges!' % defender.type)
    elif attacker.type is 'monster':
        if damageInfo[1][1] is True or damageInfo[2] is True:
            initialString = ('The %s strikes' % attacker.type)
        else:
            initialString = ('The %s attacks.' % attacker.type)
        if damageInfo[1][1] is True:
            initialString = initialString + (' critically!')
        if damageInfo[2] is True and damageInfo[1][1] is True:
            initialString = initialString + (' It finds a weakspot!')
        elif damageInfo[2] is True and damageInfo[1][1] is False:
            initialString = initialString + ('. It find a weakspot!')
        if damageInfo[4] is True:
            initialString = initialString + (' You block some damage!')
        initialString = initialString + (' The %s did %s damage.' % (attacker.type, damageInfo[3]))
        if damageInfo[3] <= 0:
            initialString = ('The %s attacks. The attack does no damage.' % attacker.type)
        elif damageInfo[0] is True:
            initialString = ('The %s attacks. You dodge!' % attacker.type)
    time.sleep(.5)
    return initialString

def castStringParse(caster, defender, spellInfo):
    if caster.type is 'player':
        initialString = ('You cast %s.' % spellInfo[0])
        if 'dmg' in spellInfo[1]:
            initialString += (' It does %s damage.' % spellInfo[5])
        elif 'heal' in spellInfo[1]:
            initialString += (' It restores %s hitpoints.' % spellInfo[5])
    elif caster.type is 'monster':
        initialString = ('The %s casts %s.' % (attacker.type, spellInfo[0]))
        if 'dmg' in spellInfo[1]:
            initialString += (' It does %s damage.' % spellInfo[5])
        elif 'heal' in spellInfo[1]:
            initialString += ('It restores %s hitpoints.' % spellInfo[5])
    return initialString

def dispHP(playerhp, playermaxhp, orchp, orcmaxhp):
    if playerhp < 0:
        playerhp = 0
    if orchp < 0:
        orchp = 0
    print(' ')
    time.sleep(1)
    print('         You: (%s/%s HP)       Him: (%s/%s HP)' % (playerhp, playermaxhp, orchp, orcmaxhp) )
    time.sleep(1.5)
    print(' ')

