import random
import time
import classes
import copy
import os
from combatdisplay import personalBar
from constants import *

current_dungeon_map = {}

#create room in center
#randomly place a corridor on edge of room
#have corridor lead to another room
#have room check for availability. if available create room
#repeat 

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
		self.CURRENTMAP = [[Floor for x in range(BOARD_WIDTH)] for y in range(BOARD_HEIGHT)]
		self.displayMap = copy.deepcopy(self.CURRENTMAP)
					
	def draw(self):
		os.system("cls")
		for creature in classes.creatures:
			if self.CURRENTMAP[classes.creatures[creature].yPos][classes.creatures[creature].xPos].passable is 'impassable':
				pass
			else:
				self.displayMap[classes.creatures[creature].yPos][classes.creatures[creature].xPos] = classes.creatures[creature]
		drawMap = ''
		pb1, pb2 = personalBar()
		print('')
		print('')
		print('')
		for yVal in range(len(self.displayMap)):
			for xVal in range(len(self.displayMap[yVal])):
				drawMap += str(self.displayMap[yVal][xVal].display)
			print('  ' + drawMap + '  ')
			drawMap = ''
		print('')
		print('  ' + pb1)
		print('  ' + pb2)
		self.displayMap = copy.deepcopy(self.CURRENTMAP)


def createMap():
	global current_dungeon_map
	dlvl = len(current_dungeon_map) + 1
	current_dungeon_map[dlvl] = Map()

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






	
