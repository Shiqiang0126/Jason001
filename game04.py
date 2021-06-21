import pygame,sys
from pygame.locals import *
import time
import random

class dBall():
    def __init__(self, wsize, bsize=pass, bcolor=pass):
        self.pos_x, self.pos_y = psize[0]//2, psize[1]//2
        pass

    def paint(self):
        color = 200,200,0
        width = 0
        pos = pos_x, pos_y, 10, 10
        screen.fill(blue)
        pygame.draw.rect(screen, color, pos, width)

white = 255,200,200
blue = 10,10,200
pygame.init()

psize = (800,600)
screen = pygame.display.set_mode(psize)
pygame.display.set_caption('Drawing Rectangles')

screen.fill(blue) #尽快进行第一板显示，缩短黑屏时间
pygame.display.update()

pos_x, pos_y = psize[0]//2,psize[1]//2
vel_x, vel_y = 2, 1

start = time.perf_counter()
spd = 0.02 #速度，越小越快
fls = 600
flsstart = start
eli = random.random() * spd
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                screen.fill(blue)
    now = time.perf_counter()
    if (now - flsstart) > fls:
        screen.fill(blue)
        flsstart = now
    elif (now - start) > eli:
        start = now
        eli = random.random() * spd
        pos_x += vel_x
        pos_y += vel_y
        if pos_x > psize[0]-10 or pos_x < 0:
            vel_x = -vel_x
            pos_x += vel_x
        if pos_y > psize[1]-10 or pos_y < 0:
            vel_y = -vel_y
            pos_y += vel_y
        color = 200,200,0
        width = 0
        pos = pos_x, pos_y, 10, 10
        screen.fill(blue)
        pygame.draw.rect(screen, color, pos, width)
        pygame.display.update()

