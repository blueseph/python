import combat
import equipment
import classes
import time
import gameturn
import combatdisplay
import board
import savegame
from msvcrt import getch

 
classes.spawnPlayer()
classes.spawnMonster()
board.createMap()
savegame.current_dungeon_map[1].draw()

while gameturn.playerDeath is False:
    input = getch()
    if 'w' in str(input): 
        savegame.creatures['player'].move(0, -1) 
        gameturn.doGameTurn()
    elif 's' in str(input):
        savegame.creatures['player'].move(0, 1)
        gameturn.doGameTurn()
    elif 'a' in str(input):
        savegame.creatures['player'].move(-1, 0)
        gameturn.doGameTurn()
    elif 'd' in str(input):
        savegame.creatures['player'].move(1, 0)
        gameturn.doGameTurn()
    elif '.' in str(input):
        gameturn.doGameTurn()
    elif 'xff' in str(input):
    #    savegame.creatures['player'].move(1, 0)
        gameturn.doGameTurn()
    elif 'p' in str(input): #debug
        for creature in savegame.creatures:
            print(savegame.creatures[creature].type, savegame.creatures[creature].maxhp, savegame.creatures[creature].curhp)