import time

def StringParse(dodge, crit, cunatk, defender, attacker, death, dmg):
    deathString = ''
    if defender == 'player':
        initialString = ('The %s attacks.' % attacker)
        if crit == True:
            initialString = initialString + (' It hits critically!')
        if cunatk == True:
            initialString = initialString + (' The attack finds a weakspot!')
        initialString = initialString + (' The %s did %s damage.' %s (attacker, dmg))
        if death == True and dodge == False:
            deathString = ('The damage is fatal!')
            deathStringTwo = (' You have been slain.')
        elif dodge == True:
            initialString = ('The %s attacks. You dodge!' % attacker)
    else:
        initialString = ('You attack')
        if crit == True:
            initialString = initialString + (' critically!')
        if cunatk == True:
            initialString = initialString + ('. You find a weakspot!')
        initialString = initialString + ('. You did %s damage.' % dmg)
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

        
