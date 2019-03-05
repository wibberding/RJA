# Import the pygame library and initialise the game engine
import pygame
pygame.init()

# Define some colors
BLACK = ( 0, 0, 0)
BROWN = ( 153, 76, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)

#Constants
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3

#a dictionary linking resources to colors
colors = {
	DIRT : BROWN,
	GRASS : GREEN,
	WATER : BLUE,
	COAL : BLACK
}

# Open a new window
size = (1024, 640)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First Game")

TILESIZE = 64
MAPWIDTH = 16
MAPHEIGHT = 10
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))
# Draw Inital Screen
	#ten tiles high and 16 tiles wide


tilemap = [
	[GRASS, COAL, DIRT, WATER, WATER, WATER, DIRT, DIRT, WATER, WATER, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
	[GRASS, COAL, DIRT, WATER, WATER, WATER, DIRT, DIRT, WATER, WATER, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
	[GRASS, COAL, DIRT, WATER, WATER, WATER, DIRT, DIRT, WATER, WATER, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
	[GRASS, COAL, DIRT, WATER, WATER, WATER, DIRT, DIRT, WATER, WATER, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
	[GRASS, COAL, DIRT, WATER, WATER, WATER, DIRT, DIRT, WATER, WATER, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
	[GRASS, COAL, DIRT, WATER, WATER, WATER, DIRT, DIRT, WATER, WATER, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
	[GRASS, COAL, DIRT, WATER, WATER, WATER, DIRT, DIRT, WATER, WATER, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
	[GRASS, COAL, DIRT, WATER, WATER, WATER, DIRT, DIRT, WATER, WATER, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
	[GRASS, COAL, DIRT, WATER, WATER, WATER, DIRT, DIRT, WATER, WATER, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
	[GRASS, COAL, DIRT, WATER, WATER, WATER, DIRT, DIRT, WATER, WATER, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS]
	
]

# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
 
     # --- Game logic should go here
 
     # --- Drawing code should go here
     # First, draw background map. 
    for row in range(MAPHEIGHT):
    	#loop through each column in the row
    	for column in range(MAPWIDTH):
    		#draw resources on map
    		pygame.draw.rect(DISPLAYSURF, colors[tilemap[row][column], (column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE) 

     #Then you can draw different shapes and lines or add text to your background stage.
 
 
     # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
     # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
