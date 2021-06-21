
while True:
    gs=input('> ')
    if gs.upper()=='QUIT':
        print('Bye')
        break
    elif gs.upper()=='HELP' or gs=='?':
        print('Enter int/float for pow, help/? for help, quit for quit, other for echo')
    elif gs.isdecimal():
        print( '{}**2={}'.format(gs,int(gs)**2))
    else:
        try:
            print( '{}**2={}'.format(gs,float(gs)**2))
        except:
            if gs!='': print('{}'.format(gs))

        
