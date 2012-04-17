import combat
import equipment
import classes
import time

classes.chooseClass()                           #chooses player class
classes.chooseMonsterClass()                    #chooses monster class
kill_count = 0
unitDeath = combat.fight()          #initiates fight

while 'player' not in unitDeath:
    kill_count += 1
    classes.chooseMonsterClass()        #rerolls monster
    unitDeath = combat.fight()          #fights again

if kill_count is 1:
	print('You have died. You killed %s monster.' % kill_count)
else:
	print('You have died. You killed %s monsters.' % kill_count)
time.sleep(10)
