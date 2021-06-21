n=int(input())
for i in range(1,n+1,2):
    print(('{: ^'+str(n)+'}').format(chr(ord('A')+(i-1)//2)*i))

