#mtsloop.py @shiqiang oct28 2019, with windows10/pythone3.7/vscode
#使用“类”的方式来进行多线程处理，其中定义多线程类估计是制定的格式，不必深究init和call的含义
import threading
from time import sleep,ctime

loops=(4,2)

class ThreadFunc(object):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.name=name
        self.func=func
        self.args=args
    def __call__(self):
        self.func(*self.args) # p2.x == apply(self.func,self,args)

def loop(nloop,nsec):
    print ('start loop ',nloop,' at:',ctime())
    sleep(nsec)
    print ('loop ',nloop,' done at:',ctime())

def main():
    print ('start at >>>>>> :',ctime())
    threads=[]
    nloops=range(len(loops))

    for i in nloops:
        t=threading.Thread(target=ThreadFunc(loop,(i,loops[i]),loop.__name__))
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    
    print ('end at:-------',ctime())

if __name__ == '__main__':
    main()