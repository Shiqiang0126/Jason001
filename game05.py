import pygame,sys
from pygame.locals import *
import time
import random

def rcolor():
    return (random.randint(50,255),random.randint(50,200),random.randint(20,180))
def rvict():
    return (random.randint(-5,5),random.randint(-5,5))

class dBall():
    def __init__(self, winid, bsize=10, bcolor=(255,255,255), v=(2,1), bwidth = 0):
        self.winh, self.winw = winid.get_height(), winid.get_width()
        self.posx, self.posy = self.winh//2, self.winw//2
        self.size = bsize
        self.color = bcolor
        self.width = bwidth # 0 for block
        self.win = winid
        self.loop = 0
        self.setStep(*v)
        pos = (self.posx, self.posy, self.size, self.size)
        pygame.draw.rect(self.win, self.color, pos, self.width)

    def nextStep(self):
        self.posx += self.vx
        self.posy += self.vy
        if self.posx > self.winw - self.size or self.posx < 0:
            self.loop += 1
            self.vx = -self.vx
            self.posx += self.vx
        if self.posy > self.winh - self.size or self.posy < 0:
            self.loop += 1
            self.vy = -self.vy 
            self.posy += self.vy
        if self.loop > 3:
            self.loop = 0
            self.color = rcolor()
            self.setStep(*rvict())
        pos = self.posx, self.posy, self.size, self.size
        pygame.draw.rect(self.win, self.color, pos, self.width)

    def setStep(self, vel_x, vel_y):
        self.vx = vel_x if vel_x != 0 else 1 
        self.vy = vel_y if vel_y != 0 else 1

    def setPos(self, posx, posy):
        if posx > self.winw - self.size:
            self.posx = self.winw - self.size
        else:
            self.posx = posx
        if posy > self.winh - self.size:
            self.posy = self.winh - self.size
        else:
            self.posy = posy
        
blue = 0,34,64
pygame.init()
psize = (800,600)
screen = pygame.display.set_mode(psize)
pygame.display.set_caption('Drawing Rectangles')

screen.fill(blue) #尽快进行第一板显示，缩短黑屏时间
pygame.display.update()

start = time.perf_counter()
spd = 0.03 #速度，越小越快
eli = random.random() * spd

B = [ dBall(screen,
            10,
            rcolor(),
            rvict()) for i in range(20) ]
for b in B:
    b.setPos(random.randint(0,b.winw),random.randint(0,b.winh))

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
        eli = random.random() * spd
        
        screen.fill(blue) 
        for b in B:
            b.nextStep()
        pygame.display.update()

