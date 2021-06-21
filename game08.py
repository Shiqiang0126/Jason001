import pygame,sys
from pygame.locals import *
import time
import random
import math

def rcolor():
    return random.randint(0,255),random.randint(0,255),random.randint(0,255)
def rpos(screen):
    pass
def rarcpos(screen): #不好玩，经常‘超届’，而且不好看
    h = random.randint(30,screen.get_height()//8)
    x = random.randint(0,screen.get_width()-h)
    y = random.randint(0,screen.get_height()-h)
    return x,y,h*2,h*2
def rwidth():
    return random.randint(2,10)
def rangle():
    s = random.randint(1,359)
    e = random.randint(s+45,s+180)
    return math.radians(s),math.radians(e)
    

def rcircle(size):
    r,g,b = rcolor()
    rpos = (random.randint(0,size[0]),random.randint(0,size[1]))
    rradius = random.randint(10,size[1] // 4) # 半径不大于四分之一窗口高度
    rwidth = random.randint(2,10) #线宽度在2-10之间
    pygame.draw.circle(screen, (r,g,b), rpos, rradius, rwidth)

def rarc(screen):
    pygame.draw.arc(screen,
                    rcolor(),
                    rarcpos(screen),
                    *rangle(),
                    rwidth())
                    
    
white = 255,200,200
blue = 0,34,64
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
        #rcircle(psize) #随机圆圈
        rarc(screen)
        pygame.display.update()

