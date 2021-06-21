import time

a=time.time()
print(len(str(2**1000000)))
print('{:.2f}\'s'.format(time.time()-a))
