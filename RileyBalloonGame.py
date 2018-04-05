import pygame, sys
from pygame.locals import *
import time
import math
from balloon import Balloon
from random import randint


# Function defs
def popBalloon(balloons):
    if len(balloons) != 0:
        randPop = randint(0, len(balloons) - 1)
        balloons[randPop].popIt()


# Set it all up
pygame.mixer.pre_init(44100, -16, 1, 512) # This fixes sound delay
pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

screen_size_x = 800
screen_size_y = 600
margin = 10

DISPLAYSURF = pygame.display.set_mode((screen_size_x, screen_size_y), 0, 32)
pygame.display.set_caption("Riley's Balloons")

WHITE = (255, 255, 255)

balloons = []

soundStartFlag = 0 

# Main loop
while True: 
    DISPLAYSURF.fill(WHITE)    

    # Event handling loop
    for event in pygame.event.get(): 
        
        if event.type == KEYDOWN:   
            if event.key == K_SPACE:
                popBalloon(balloons) # This function is defined above. It will randomly pop a balloon.
                
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()


    # Did any of them pop or fly away?
    balloons = [balloon for balloon in balloons if not balloon.poppedFlag]
    balloons = [balloon for balloon in balloons if not balloon.flyAwayFlag]
    
    # Maybe a new balloon?
    randBalloon = randint(1, 40) # 40 is good
    if randBalloon == 7:
        balloons.append(Balloon(margin, screen_size_x, screen_size_y))

    # Move the ballons and draw them
    for balloon in balloons:
        balloon.move()
        DISPLAYSURF.blit(balloon.img, (balloon.x, balloon.y))
    
    # Draw it
    pygame.display.update()    
    fpsClock.tick(FPS)   
    
    # Start music
    if soundStartFlag == 0:
        pygame.mixer.init()
        #pygame.mixer.music.load('sounds/UptownFunk.mp3')
        #pygame.mixer.music.play(0)
        soundStartFlag = 1



