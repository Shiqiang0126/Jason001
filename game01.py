import pygame,sys
from pygame.locals import *
import time

white = 255,200,200
blue = 50,50,200
pygame.init()
screen = pygame.display.set_mode((600,500))
myfont = pygame.font.Font(None,60)
textImage = myfont.render('Hello Pygame', True, white)

screen.fill(blue)
screen.blit(textImage,(100, 100))
pygame.display.update()
    
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill(blue)
    screen.blit(textImage,(100, 100))
    pygame.display.update()

'''time.sleep(4)
sys.exit()'''
    
