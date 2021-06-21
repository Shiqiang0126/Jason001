#maxfact.py @shiqiang 2019

def showMaxFactor(num):
    count= num//2
    while count>1:
        if num % count ==0:
            print('largest factor of %d is %d' % (num,count))
            break
        count -= 1
    else:
        print ("%d is prime" % num)

for eachNum in range(10,20):
    showMaxFactor(eachNum)

    
