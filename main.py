import combat
import equipment
import classes
import time
import gameturn
import combatdisplay
import board
from msvcrt import getch

 
classes.chooseClass()
classes.chooseMonsterClass()
board.createMap()
board.current_dungeon_map[1].draw()

while gameturn.playerDeath is False:
    input = getch()
    if 'w' in str(input): 
        classes.creatures['player'].move(0, -1) 
        gameturn.doGameTurn()
    elif 's' in str(input):
        classes.creatures['player'].move(0, 1)
        gameturn.doGameTurn()
    elif 'a' in str(input):
        classes.creatures['player'].move(-1, 0)
        gameturn.doGameTurn()
    elif 'd' in str(input):
        classes.creatures['player'].move(1, 0)
        gameturn.doGameTurn()
    elif 'xff' in str(input):
        classes.creatures['player'].move(1, 0)
        gameturn.doGameTurn() 