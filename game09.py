import math
import pygame,sys
from pygame.locals import *
import random
import time

pygame.init()
screen = pygame.display.set_mode((600,500))
myfont = pygame.font.Font(None, 60)

color = 200, 80, 60
width = 4
x,y = 300,250
radius = 200
position = x - radius, y - radius, radius * 2, radius * 2

pieco = [False, False, False, False]
keys = pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4
ltag = (x+radius,y),(x,y-radius),(x-radius,y),(x,y+radius)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            for i in range(4):
                if event.key == keys[i]:
                    pieco[i] = True

    screen.fill((0,10,50))

    screen.blit( myfont.render('1', True, color),
                (x + radius/2 - 20, y - radius/2))
    screen.blit( myfont.render('2', True, color),
                (x - radius/2, y - radius/2))
    screen.blit( myfont.render('3', True, color),
                (x - radius/2, y + radius/2 - 20))
    screen.blit( myfont.render('4', True, color),
                (x + radius/2 - 20, y + radius/2 - 20))

    for i in range(4):
        if pieco[i]:
            pygame.draw.arc(screen,
                            color,
                            position,
                            math.radians(90 * i),
                            math.radians(90 *(i+1)),
                            width)
            pygame.draw.line(screen,
                             color,
                             (x,y),
                             ltag[i],
                             width)
            pygame.draw.line(screen,
                             color,
                             (x,y),
                             ltag[(i+1)%4],
                             width)
    if pieco[0] and pieco[1] and pieco[2] and pieco[3]:
            color = 0,255,0
    pygame.display.update()
