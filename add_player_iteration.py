import pygame, sys
from pygame.locals import *

#constants representing the different resources
DIRT = "dirt"
GRASS = "grass"
WATER = "water"
COAL = "coal"

#a dictionary linking resources to colors
textures = 	{
				DIRT : pygame.image.load('images/dirt.png'),
				GRASS : pygame.image.load('images/grass.png'),
				WATER : pygame.image.load('images/water.png'),
				COAL : pygame.image.load('images/coal.png')
			}

#a list representing our tilemap
tilemap = 	[
				[GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS, COAL, DIRT, DIRT ],
				[WATER, WATER, GRASS, GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS],
				[GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS,COAL, GRASS, WATER],
				[DIRT, GRASS, COAL, GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS],
				[GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS,GRASS, WATER, DIRT ],
				[GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS, COAL, DIRT, DIRT ],
				[WATER, WATER, GRASS, GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS],
				[GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS,COAL, GRASS, WATER],
				[DIRT, GRASS, COAL, GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS],
				[GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS,GRASS, WATER, DIRT ]
			]

#useful game dimensions
TILESIZE = 64
MAPWIDTH = 16
MAPHEIGHT = 10



#set up the display
pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

#1 the player image
PLAYER = pygame.image.load('images/player.png').convert_alpha()
#the position of the player [x,y]
playerPos = [0,0]

while True:

	#get all the user events
	for event in pygame.event.get():
		#2 See game events in the console
		print(event)
		#if the user wants to quit
		if event.type == QUIT:
			#end the game and close the window
			pygame.quit()
			sys.exit()
		#3 if a key is pressed
		elif event.type == KEYDOWN:
			#if the right arrow is pressed
			if (event.key == K_RIGHT) and playerPos[0] < MAPWIDTH -1:
				#change the player's x position
				playerPos[0] += 1
			#if the left arrow is pressed
			elif (event.key == K_LEFT) and playerPos[0] > 0:
				#change the player's x position
				playerPos[0] -= 1
			#if the down arrow is pressed
			elif (event.key == K_DOWN) and playerPos[1] < MAPHEIGHT -1:
				#change the player's x position
				playerPos[1] += 1
			#if the up arrow is pressed
			elif (event.key == K_UP) and playerPos[1] > 0:
				#change the player's x position
				playerPos[1] -= 1

	#loop through each row
	for row in range(MAPHEIGHT):
		#loop through each column in the row
		for column in range(MAPWIDTH):
			#draw the resource at that position in the tilemap, using the correct image
			DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE))

	#4 display the player at the correct position
	DISPLAYSURF.blit(PLAYER,(playerPos[0]*TILESIZE, playerPos[1]*TILESIZE))


	#update the display
	pygame.display.update()
