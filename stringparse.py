import time

def meleeStringParse(dodge, crit, cunatk, defender, attacker, death, dmg, block):
    hasCrit = crit[0]
    deathString = ''
    if attacker.type is 'player':
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
        if dmg <= 0:
            initialString = ('You attack. The attack does no damage.')
        if dodge is True:
            initialString = ('You attack. The %s dodges!' % defender.type)
    elif attacker.type is 'monster':
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
        if dmg <= 0:
            initialString = ('The %s attacks. The attack does no damage.' % attacker.type)
        elif dodge is True:
            initialString = ('The %s attacks. You dodge!' % attacker.type)
    print(initialString)
    time.sleep(.5)
    determineDeath(defender, death)

def castStringParse(caster, defender, spellInfo, death):
    if caster.type is 'player':
        initialString = ('You cast %s.' % spellInfo[0])
        if 'dmg' in spellInfo[1]:
            initialString += (' It does %s damage.' % spellInfo[5])
            if death[0] is True:
                deathString = ('The damage is fatal!')
                deathStringTwo = ('You have slain the %s!' % defender.type)
        elif 'heal' in spellInfo[1]:
            initialString += ('It restores %s hitpoints.' % spellInfo[5])
    elif caster.type is 'monster':
        initialString = ('The %s casts %s.' % (attacker.type, spellInfo[0]))
        if 'dmg' in spellInfo[1]:
            initialString += (' It does %s damage.' % spellInfo[5])
            if death[0] is True:
                deathString = ('The damage is fatal!')
                deathStringTwo = ('You have slain the %s!' % defender.type)
        elif 'heal' in spellInfo[1]:
            initialString += ('It restores %s hitpoints.' % spellInfo[5])
    print(initialString)
    determineDeath(defender, death)

def determineDeath(defender, death):
    if death[0] is True:
        time.sleep(1.5)
        print('The damage is fatal!')
        time.sleep(1.5)
        if defender.type is 'player':
            print('You have been slain!')
        elif defender.type is 'monster':
            print('The %s has been slain!' % defender.unitclass)
        time.sleep(2.0)

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

