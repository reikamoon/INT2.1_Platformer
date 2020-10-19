# Import Pygame
import pygame
import random
# Import pygame.locals for easier access to key coordinates.
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

#DEFINITIONS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Initalize pygame
pygame.init()
pygame.display.set_caption('INT2.1 Game')

#Initialize Screen
screen = pygame.display.set_mode((544, 416))

# Run until the User Quits
running = True
while running:
    #Did the user click the close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Set Up BG
    screen.fill(WHITE)

    #Draw a circle
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    #Update Screen
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
