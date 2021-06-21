import pygame,sys
from pygame.locals import *
import time
import random

def rcircle(size):
    r,g,b = random.randint(0,255),random.randint(0,255),random.randint(0,255)
    rpos = (random.randint(0,size[0]),random.randint(0,size[1]))
    rradius = random.randint(10,size[1] // 4) # 半径不大于四分之一窗口高度
    rwidth = random.randint(2,10) #线宽度在2-10之间
    pygame.draw.circle(screen, (r,g,b), rpos, rradius, rwidth)
    
white = 255,200,200
blue = 10,10,200
pygame.init()

psize = (800,600)
screen = pygame.display.set_mode(psize)
pygame.display.set_caption('Drawing Circles')

screen.fill(blue) #尽快进行第一板显示，缩短黑屏时间
rcircle(psize)
pygame.display.update()

start = time.perf_counter()
spd = 0.2 #速度，越小越快
fls = 15
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
        rcircle(psize) #随机圆圈
        pygame.display.update()

