import random
import time
import classes
import stringparse
import combatdisplay
import gameturn

def determineDeath(defender):
    if defender.curhp <= 0:
        if defender.type is 'monster':
            gameturn.monsterDeath = True
            gameturn.deathblow = True
        elif defender.type is 'player':
            gameturn.playerDeath = True
        defender.curhp = 0

