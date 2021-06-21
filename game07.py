import pygame,sys
from pygame.locals import *
import time
import random

def rcolor():
    return (random.randint(50,255),random.randint(50,200),random.randint(20,180))
def rvict():
    return (random.randint(-5,5),random.randint(-5,5))

class dLeaf():
    def __init__(self, winid, stepx=10, color=(255,255,255), lwidth=1):
        self.win = winid
        self.winh, self.winw = winid.get_height(), winid.get_width()
        self.stepx = stepx
        self.stepy = self.winh//int(self.winw/stepx)
        self.x, self.y = 0, self.stepy
        self.color = color
        self.width = lwidth # 0 for block
        self.loop = 0
        self.slp = 1

    def nextLine(self):
        if self.slp > 0:
            #pygame.draw.line(self.win,
            #              self.color,
            #              (self.x,0),
            #              (self.winw,self.y),
            #              self.width)
            #pygame.draw.line(self.win,
            #              self.color,
            #              (self.winw - self.x,self.winh),
            #              (0,self.winh - self.y),
            #              self.width)'''
            pygame.draw.line(self.win,
                         self.color,
                         (self.winw - self.x,0),
                         (0, self.y),
                         self.width)
            pygame.draw.line(self.win,
                         self.color,
                         (self.x, self.winh),
                         (self.winw, self.winh - self.y),
                         self.width)
            
            self.x += self.stepx
            self.y += self.stepy
            if self.x > self.winw or self.y > self.winh:
                self.slp = -30
            return 0 # nothing todo
        else:
            self.slp += 1
            if self.slp > 0: # 重启一屏幕
                self.x, self.y = 0, self.stepy
                self.color = rcolor()
                return 1 #'next screen'
            else:
                return 0 # nothing todo 
            

blue = 0,34,64
pygame.init()
psize = (900,600)
screen = pygame.display.set_mode(psize)
pygame.display.set_caption('Drawing Lines')

screen.fill(blue) #尽快进行第一板显示，缩短黑屏时间
pygame.display.update()

start = time.perf_counter()
spd = 0.03 # 速度，越小越快
eli = spd # 不变速了，random.random() * spd

lf = dLeaf(screen, 10, rcolor(), 2) # 

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                screen.fill(blue)
    now = time.perf_counter()
    if (now - start) > eli:
        start = now
        eli = spd
        if lf.nextLine():
            screen.fill(blue)
        pygame.display.update()

