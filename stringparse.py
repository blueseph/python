import time

def StringParse(dodge, crit, cunatk, defender, attacker, death, dmg, offhand, block):
    hasCrit = crit[0]
    deathString = ''
    unitHasDied = False
    if defender is 'player':
        if hasCrit is True or cunatk is True:
            initialString = ('The %s strikes' % attacker)
        else:
            initialString = ('The %s attacks.' % attacker)
        if hasCrit is True:
            initialString = initialString + (' critically!')
        if cunatk is True and hasCrit is True:
            initialString = initialString + (' It finds a weakspot!')
        elif cunatk is True and hasCrit is False:
            initialString = initialString + ('. It find a weakspot!')
        if block is True:
            initialString = initialString + (' You block some damage!')
        initialString = initialString + (' The %s did %s damage.' % (attacker, dmg))
        if death is True and dodge is False:
            deathString = ('The damage is fatal!')
            deathStringTwo = ('You have been slain.')
        if dmg <= 0:
            initialString = ('The %s attacks. The attack does no damage.' % attacker)
        elif dodge is True:
            initialString = ('The %s attacks. You dodge!' % attacker)
    else:
        if hasCrit is True or cunatk is True:
            initialString = ('You attack')
        else:
            initialString = ('You attack.')
        if hasCrit is True:
            initialString = initialString + (' critically!')
        if cunatk is True and hasCrit is True:
            initialString = initialString + (' You find a weakspot!')
        elif cunatk is True and hasCrit is False:
            initialString = initialString + ('. You find a weakspot!')
        if block is True:
            initialString = initialString + (' It blocks some damage!')
        initialString = initialString + (' You did %s damage.' % dmg)
        if death is True and dodge is False:
            deathString = ('The damage is fatal!')
            deathStringTwo = ('You have slain the %s!' % defender)
        if dmg <= 0:
            initialString = ('You attack. The attack does no damage.')
        if dodge is True:
            initialString = ('You attack. The %s dodges!' % defender)

    if 'The' in deathString:
        unitHasDied = True
        print(initialString)
        time.sleep(1)
        print(deathString)
        time.sleep(2)
        print(deathStringTwo)
        time.sleep(1)
    else:
        print(initialString)
        time.sleep(1)
    return unitHasDied

def dispHP(playerhp, playermaxhp, orchp, orcmaxhp, sleeptime):
    time.sleep(sleeptime)
    print(' ')
    print('         You: (%s/%s HP)       Him: (%s/%s HP)' % (playerhp, playermaxhp, orchp, orcmaxhp) )
    print(' ')

