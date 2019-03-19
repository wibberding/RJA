#1 the player image
PLAYER = pygame.image.load('images/player.png').convert_alpha()
#the position of the player [x,y]
playerPos = [0,0]

#2 See game events in the console
		print(event)

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

#4 display the player at the correct position
DISPLAYSURF.blit(PLAYER,(playerPos[0]*TILESIZE, playerPos[1]*TILESIZE))
