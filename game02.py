import pygame,sys
from pygame.locals import *
import time
import random

white = 255,200,200
blue = 10,10,200
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption('Drawing Circles')
#myfont = pygame.font.Font(None,60)
#textImage = myfont.render('Hello Pygame', True, white)

#screen.fill(blue)
#screen.blit(textImage,(100, 100))
#pygame.display.update()

r,g,b = random.randint(0,255),random.randint(0,255),random.randint(0,255)
color,position,radius,width = (r,g,b),(300,250),100,10

screen.fill(blue)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == pygame.K_UP:
                radius += 5
            elif event.key == pygame.K_DOWN:
                radius -= 5
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_LEFT:
                r,g,b = random.randint(0,255),random.randint(0,255),random.randint(0,255)
                color = (r,g,b)
            elif event.key == pygame.K_RIGHT:
                r,g,b = random.randint(0,255),random.randint(0,255),random.randint(0,255)
                color = (r,g,b)
                
    
    pygame.draw.circle(screen, color, position, radius, width)
    pygame.display.update()

