#mtfacfib.py @shiqiang oct28 2019, with windows10/pythone3.7/vscode
#比较单线程、多线程下，计算三种运算的耗时差别

import threading
from time import sleep,ctime

loops=(4,2)

class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.name=name
        self.func=func
        self.args=args
    def getResult(self):
        return self.res
    def run(self):
        print (self.name,' staring at:', ctime())
        self.res=self.func(*self.args) # p1.x must write: apply(self.func,self,args)
        print (self.name,' finished at:',ctime())

def fib(x):
    sleep(0.005)
    if x < 2:return 1
    return (fib(x-2)+fib(x-1))
def fac(x):
    sleep(0.1)
    if x < 2:return 1
    return (x * fac(x-1))
def isum(x):
    sleep(0.1)
    if x <2: return 1
    return (x+isum(x-1))

funcs=[fib,fac,isum]
n=14

def main():
    nfuncs=range(len(funcs))
    print ('... SINGLE THREAD ...')
    for i in nfuncs:
        print ('>>>>>>> staring ',funcs[i].__name__,' at:',ctime())
        print (funcs[i](n))
        print ('======= finished ',funcs[i].__name__,' at',ctime())

    print ('::: MULTIPLE THREADS :::')
    threads=[]
    for i in nfuncs:
        t=MyThread(funcs[i],(n,),funcs[i].__name__) #(n,) 是什么意思?
        threads.append(t)
    for i in nfuncs:
        threads[i].start() #不论什么方式产生的线程类，运行方式都是一样的
    for i in nfuncs:
        threads[i].join()
        print ('Thread ',i,' ', funcs[i].__name__, ' result: ',threads[i].getResult())
    



if __name__ == '__main__':
    main()