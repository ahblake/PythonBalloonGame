
import pygame
from random import randint

class Balloon:
    
    def __init__(self, margin, screenSizeX, screenSizeY):
        self.images = ["images/red.jpg", "images/yellow.jpg", "images/blue.jpg", "images/green.jpg"]
        #self.sounds = ["sounds/pop1.wav", "sounds/pop2.wav", "sounds/pop3.wav", "sounds/pop4.wav"]
        self.ballonTypes = len(self.images)
        self.randImg = randint(0, 3)
        self.img = pygame.image.load(self.images[self.randImg])
        self.velocity = randint(2, 7)
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.screenSizeX = screenSizeX
        self.screenSizeY = screenSizeY
        self.margin = margin
        self.x = randint(margin, (self.screenSizeX - self.width - self.margin))
        self.y = self.screenSizeY + self.height - 250
        self.flyAwayFlag = False
        self.poppedFlag = False
        
    def move(self):
        self.y -= self.velocity
        self.checkFlyAway()
        
    def popIt(self):
        #self.img = ("images/popped.jpg") # This does nothing. The balloon gets removed from the list before it gets blitted and displayed.
        pygame.mixer.Sound("sounds/pop.wav").play()
        self.poppedFlag = True
        
    def checkFlyAway(self):
        if self.y <= -self.height:
            self.flyAwayFlag = True
        
        