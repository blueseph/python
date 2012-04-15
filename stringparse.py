import time

def meleeStringParse(dodge, crit, cunatk, defender, attacker, death, dmg, block):
    hasCrit = crit[0]
    deathString = ''
    unitHasDied = False
    if attacker.type is 'berserker' or attacker.type is 'rogue' or attacker.type is'warrior':
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
        if death[0] is True and dodge is False:
            deathString = ('The damage is fatal!')
            deathStringTwo = ('You have slain the %s!' % defender.type)
        if dmg <= 0:
            initialString = ('You attack. The attack does no damage.')
        if dodge is True:
            initialString = ('You attack. The %s dodges!' % defender.type)
    elif attacker.type is not 'berserker' or 'rogue' or 'warrior':
        if hasCrit is True or cunatk is True:
            initialString = ('The %s strikes' % attacker.type)
        else:
            initialString = ('The %s attacks.' % attacker.type)
        if hasCrit is True:
            initialString = initialString + (' critically!')
        if cunatk is True and hasCrit is True:
            initialString = initialString + (' It finds a weakspot!')
        elif cunatk is True and hasCrit is False:
            initialString = initialString + ('. It find a weakspot!')
        if block is True:
            initialString = initialString + (' You block some damage!')
        initialString = initialString + (' The %s did %s damage.' % (attacker.type, dmg))
        if death[0] is True and dodge is False:
            deathString = ('The damage is fatal!')
            deathStringTwo = ('You have been slain.')
        if dmg <= 0:
            initialString = ('The %s attacks. The attack does no damage.' % attacker.type)
        elif dodge is True:
            initialString = ('The %s attacks. You dodge!' % attacker.type)

    if death[0] is True:
        print(initialString)
        time.sleep(1.5)
        print(deathString)
        time.sleep(1.5)
        print(deathStringTwo)
        time.sleep(2.5)
    else:
        print(initialString)
        time.sleep(1)

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

