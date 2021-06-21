#!/usr/bin/env python ?

'big.py make a text file  -- create a text file'

import os
ls = os.linesep

#get filename

while True:
    fname = input("Pls enter filename:")
    if os.path.exists(fname):
        print("Error:'%s' already exitsts" % fname)
    else:
        break

#get file content  text lines
all=[]
print("\nEnter lines('.' by itself to quit).\n")
while True:
    entry = input(">")
    if entry =='.':
        break
    else:
        all.append(entry)


fobj= open(fname,'w')
fobj.writelines( '%s\n' % x for x in all )  #(['%s%s' % (x,ls) for x in all])
fobj.close()
print( 'DONE!' )
