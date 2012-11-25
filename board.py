import random
import time
import copy
import os
import savegame
import gameturn
import levelingstats
from constants import *

def getEquipBar(unit):
    if unit.offhand is not None:
        equipBar = ('%s (mainhand) %s (offhand) | %s (%s ac)' % (unit.mainhandWeaponName, unit.offhandItemName, unit.armorName, unit.armorClass))
    elif unit.mainhand is '2h':
         equipBar = ('%s (two-handed) | %s (%s ac)' % (unit.mainhandWeaponName, unit.armorName, unit.armorClass))
    else:
         equipBar = ('%s (mainhand) |  %s (%s ac)' % (unit.mainhandWeaponName, unit.armorName, unit.armorClass))
    return equipBar

def bottomMenu():
    fl = '      Character    |   Inventory   |   Abilities   |    Spells    |   Menu'
    sl = '         [c]       |      [i]      |      [z]      |      [Z]     |   [m]'
    return fl, sl

def getHPBar(unit):
    if unit.curhp < 0:
        unit.curhp = 0
    HPBarString = ('[' + ('-----' * round((unit.curhp / unit.maxhp) * 10) + ('     ' * (10 - round((unit.curhp / unit.maxhp) * 10)) + ']' )))
    return HPBarString

class Tile:
	def __init__(self, passable, display, tile):
		self.passable = passable
		self.display = display
		self.tile = tile

Empty = Tile(False, ' ', 'empty')
Floor = Tile(True, '.', 'floor')
Wall = Tile(False, '#', 'wall')
ClosedDoor = Tile(False, '|', 'closeddoor')
OpenDoor = Tile(True, '-', 'opendoor')

class Map:
	def __init__(self):
		self.CURRENTMAP = [[Tile(True, '.', 'floor') for x in range(BOARD_WIDTH)] for y in range(BOARD_HEIGHT)]
		self.displayMap = copy.deepcopy(self.CURRENTMAP)
		#y,x
					
	def draw(self, combat=' '):
		os.system("cls")
		for creature in savegame.creatures:
			if self.CURRENTMAP[savegame.creatures[creature].yPos][savegame.creatures[creature].xPos].passable is 'impassable':
				pass
			else:
				self.displayMap[savegame.creatures[creature].yPos][savegame.creatures[creature].xPos] = savegame.creatures[creature]
		drawMap = ''
		fl, sl = bottomMenu()
		print('')
		print('')
		for yVal in range(len(self.displayMap)):
			for xVal in range(len(self.displayMap[yVal])):
				drawMap += str(self.displayMap[yVal][xVal].display)
			print('  ' + drawMap + '  ')
			drawMap = ''
		print('')
		print('     %s' % combat)
		print('')
		print('    HP: %s/%s  %s  |  XP: %s [%s/%s]' % (savegame.creatures['player'].curhp, savegame.creatures['player'].maxhp, getHPBar(savegame.creatures['player']), savegame.creatures['player'].curlvl, savegame.creatures['player'].curXP, levelingstats.xpToLevel[savegame.creatures['player'].curlvl + 1]))
		print(' ')
		print('  ' + fl)
		print('  ' + sl)
		self.displayMap = copy.deepcopy(self.CURRENTMAP)


def createMap():
	dlvl = len(savegame.current_dungeon_map) + 1
	savegame.current_dungeon_map[dlvl] = Map()

#	def addRoom(self):
#		xRand = random.randint(BOARD_WIDTH)
#		yRand = random.randint(BOARD_HEIGHT)
#		xValue = random.randint(3, 5)
#		yValue = random.randint(2, 5)
#		while currentMap[random.randint(yRand)][random.randint(xRand)].tile is not 'empty':
#			xRand = random.randint(BOARD_WIDTH)
#			yRand = random.randint(BOARD_HEIGHT)
#		currentMap = [[Floor 
#			for yVal in range(yRand + yValue + 1)]
#				for xVal in range(y)
#		for yVal in range(yValue + 1):
#			currentMap[yVal][
#				xVal for xVal in range(xValue + 1)]






	
