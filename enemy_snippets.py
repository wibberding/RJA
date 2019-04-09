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

#ENEMY 2 Enemy Code
ENEMY = pygame.image.load('images/enemy.png').convert_alpha()
clock = pygame.time.Clock()

	#ENEMY 3 Check to see if the enemy and player are in the same square
	if enemy_touched(playerPos, enemyPos):
		print("you lost!")
		pygame.quit()

	#Move enemies
	move_enemy()

	#ENEMY 4 Display the enemy at the correct position
	DISPLAYSURF.blit(ENEMY,(enemyPos[0]*TILESIZE, enemyPos[1]*TILESIZE))

	#ENEMY 5
	clock.tick(30)
