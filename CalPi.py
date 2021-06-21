#CalPi.py @shiqiang oct.2019 masOS python2.7

from random import random
from time import time

def calpi( L ):
    dots = L**2 #total dot gona drop
    hits=0.0
    start=time()
    while dots > 0:
        x,y=random(),random()
        if pow(x**2+y**2,0.5) <= 1.0: #hits in 1/4 circle
            hits=hits+1
        dots -= 1
    pi=4*(hits/(L**2))
    print('running time:{:.5f}'.format(time()-start))
    print('L = {}'.format(L))
    print('pai = {}'.format(pi))

calpi(1000)
#calpi(10000)
