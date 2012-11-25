import combat
import equipment
import classes
import time
import gameturn
import combatdisplay
import board
import savegame
import os
from msvcrt import getch


os.system("mode con cols=90 lines=30") 


classes.spawnPlayer()
classes.spawnMonster()
board.createMap()
savegame.current_dungeon_map[1].draw()

while gameturn.playerDeath is False:
    input = getch()

    ###############################
    #           movement          #
    ###############################

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

    ###############################
    #           inventory         #
    ###############################

    elif 'i' in str(input):
        invEscape = False
        combatdisplay.inventoryScreen()
        invArrow = 1
        arrow = 1
        while invEscape is False:
            invInput = getch()
            if 'd' in str(invInput):
                arrow += 1
                if arrow > 4:
                    arrow = 4
                combatdisplay.inventoryScreen(arrow)
            elif 'a' in str(invInput):
                arrow -= 1
                if arrow < 1:
                    arrow = 1
                combatdisplay.inventoryScreen(arrow)
            elif '\\r' in str(invInput) or 's' in str(invInput):
                invArrow = 1
                subInvEscape = False
                combatdisplay.inventoryScreen(arrow, invArrow)
                while subInvEscape is False:
                    subInvInput = getch()
                    if 's' in str(subInvInput):
                        invArrow += 2
                        if invArrow > 10:
                            invArrow -= 10
                        combatdisplay.inventoryScreen(arrow, invArrow)
                    elif 'w' in str(subInvInput):
                        invArrow -= 2
                        if invArrow < 1:
                            subInvEscape = True
                            invArrow = 0
                        combatdisplay.inventoryScreen(arrow, invArrow)
                    elif 'd' in str(subInvInput):
                        invArrow += 1
                        if invArrow > 10:
                            invArrow = 1
                        combatdisplay.inventoryScreen(arrow, invArrow)
                    elif 'a' in str(subInvInput):
                        invArrow -= 1
                        if invArrow < 1:
                            invArrow += 1
                        combatdisplay.inventoryScreen(arrow, invArrow)
                    elif '\\x1b' in str(subInvInput):
                        invArrow = 0
                        subInvEscape = True
                        combatdisplay.inventoryScreen(arrow, invArrow)
                    elif 'i' in str(subInvInput):
                        subInvEscape = True
                        invEscape = True
                        savegame.current_dungeon_map[1].draw()
            elif 'i' in str(invInput):
                invEscape = True
                savegame.current_dungeon_map[1].draw()
            elif '\\x1b' in str(invInput):
                invEscape = True 
                savegame.current_dungeon_map[1].draw()

    ###############################
    #           character         #
    ###############################

    elif 'c' in str(input):
        characterEscape = False
        combatdisplay.characterScreen()
        while characterEscape is False:
            charInput = getch()
            if 'c' in str(charInput) or '\\x1b' in str(charInput):
                characterEscape = True
                savegame.current_dungeon_map[1].draw()
        

