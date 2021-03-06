import pygame, sys
from pygame.locals import *

#Functions
#Check for a wall
def can_move(x,y):
	if tilemap[y][x] < 10:
		return True
	else:
		return False

#See if goal is reached
def goal_reached(x,y):
	x_goal = 15
	y_goal = 0

	if x_goal == x and y_goal == y:
		return True
	else:
		return False

#ENEMY 1 Enemy code
enemyClock = 0
enemyDirection = 1
#Starting position of the enemy [x,y]
enemyPos = [10,0]

def move_enemy():
	global enemyClock
	global enemyPos
	global enemyDirection
	#move
	if enemyClock == 5:
		enemyPos[1] = enemyPos[1] + enemyDirection
		#check for boundaries
		if enemyPos[1] == 9:
			enemyDirection = -1
		if enemyPos[1] == 0:
			enemyDirection = 1
	#Tick clock
	enemyClock += 1
	#reset when it reaches 5
	if enemyClock > 5:
		enemyClock = 0

def enemy_touched(playerPos, enemyPos):
	if playerPos[0] == enemyPos[0] and playerPos[1] == enemyPos[1]:
		return True
	else:
		return False


#constants representing the different resources
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
GOAL = 4

#Wall objects numbered above 10
WALL = 20

#a dictionary linking resources to colors
textures = 	{
				DIRT : pygame.image.load('images/dirt.png'),
				GRASS : pygame.image.load('images/grass.png'),
				WATER : pygame.image.load('images/water.png'),
				COAL : pygame.image.load('images/coal.png'),
				WALL : pygame.image.load('images/wall.png'),
				GOAL : pygame.image.load('images/goal.png')
			}

#a list representing our tilemap
tilemap = 	[
				[GRASS, COAL, DIRT, WALL, COAL, DIRT, GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS, COAL, DIRT, GOAL ],
				[WATER, WATER, GRASS, GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS],
				[GRASS, COAL, DIRT, WALL, COAL, DIRT, GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS,COAL, GRASS, WATER],
				[DIRT, GRASS, COAL, WALL, COAL, DIRT, GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS, COAL, DIRT, GRASS],
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

#ENEMY 2 Enemy Code
ENEMY = pygame.image.load('images/enemy.png').convert_alpha()
clock = pygame.time.Clock()

while True:

	#Check to see if the player has reached the goal
	print(playerPos)
	if goal_reached(playerPos[0], playerPos[1]):
		print("You Won!")
		pygame.quit()

	#ENEMY 3 Check to see if the enemy and player are in the same square
	if enemy_touched(playerPos, enemyPos):
		print("you lost!")
		pygame.quit()

	#Move enemies
	move_enemy()

	#get all the user events
	for event in pygame.event.get():
		#2 See game events in the console
		# print(event)
		#if the user wants to quit
		if event.type == QUIT:
			#end the game and close the window
			pygame.quit()
			sys.exit()
		#3 if a key is pressed
		elif event.type == KEYDOWN:
			
			#if the right arrow is pressed
			if (event.key == K_RIGHT) and playerPos[0] < MAPWIDTH -1:
				#check for wall
				x = playerPos[0] + 1
				y = playerPos[1]
				if can_move(x,y):
					#change the player's x position
					playerPos[0] += 1

			#if the left arrow is pressed
			elif (event.key == K_LEFT) and playerPos[0] > 0:
				#check for wall
				x = playerPos[0] - 1
				y = playerPos[1]
				if can_move(x,y):
					#change the player's x position
					playerPos[0] -= 1

			#if the down arrow is pressed
			elif (event.key == K_DOWN) and playerPos[1] < MAPHEIGHT -1:
				#check for wall
				x = playerPos[0]
				y = playerPos[1] +1
				if can_move(x,y):
					#change the player's x position
					playerPos[1] += 1

			#if the up arrow is pressed
			elif (event.key == K_UP) and playerPos[1] > 0:
				#check for wall
				x = playerPos[0]
				y = playerPos[1] -1
				if can_move(x,y):
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

	#ENEMY 4 Display the enemy at the correct position
	DISPLAYSURF.blit(ENEMY,(enemyPos[0]*TILESIZE, enemyPos[1]*TILESIZE))

	#update the display
	pygame.display.update()
	#ENEMY 5
	clock.tick(30)
