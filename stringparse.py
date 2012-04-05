import time

def StringParse(dodge, crit, cunatk, defender, attacker, death, dmg):
    deathString = ''
    if defender == 'player':
        if crit == True or cunatk == True:
            initialString = ('The %s strikes' % attacker)
        else:
            initialString = ('The %s attack.' % attacker)
        if crit == True:
            initialString = initialString + (' critically!')
        if cunatk == True and crit == True:
            initialString = initialString + (' It finds a weakspot!')
        elif cunatk == True and crit == False:
            initialString = initialString + ('. It find a weakspot!')
        initialString = initialString + (' The %s did %s damage.' % (attacker, dmg))
        if death == True and dodge == False:
            deathString = ('The damage is fatal!')
            deathStringTwo = ('You have been slain.')
        elif dodge == True:
            initialString = ('The %s attacks. You dodge!' % attacker)
    else:
        if crit == True or cunatk == True:
            initialString = ('You attack')
        else:
            initialString = ('You attack.')
        if crit == True:
            initialString = initialString + (' critically!')
        if cunatk == True and crit == True:
            initialString = initialString + (' You find a weakspot!')
        elif cunatk == True and crit == False:
            initialString = initialString + ('. You find a weakspot!')
        initialString = initialString + (' You did %s damage.' % dmg)
        if death == True and dodge == False:
            deathString = ('The damage is fatal!')
            deathStringTwo = ('You have slain the %s!' % defender)
        if dodge == True:
            initialString = ('You attack. The %s dodges!' % defender)

    if 'The' in deathString:
        print(initialString)
        time.sleep(1)
        print(deathString)
        time.sleep(2)
        print(deathStringTwo)
        time.sleep(1)
    else:
        print(initialString)
        time.sleep(1)

        
