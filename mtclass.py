#mtclass.py @shiqiang oct28 2019, with windows10/pythone3.7/vscode

import threading
from time import sleep,ctime

loops=(4,2)

class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.name=name
        self.func=func
        self.args=args
    def run(self):
        self.func(*self.args) # p1.x must write: apply(self.func,self,args)

def loop(nloop,nsec):
    print ('start loop ',nloop,' at:',ctime())
    sleep(nsec)
    print ('loop ',nloop,' done at:',ctime())

def main():
    print ('start at >>>>>> :',ctime())
    threads=[]
    nloops=range(len(loops))

    for i in nloops:
        t=MyThread(loop,(i,loops[i]),loop.__name__)
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    
    print ('end at:-------',ctime())

if __name__ == '__main__':
    main()