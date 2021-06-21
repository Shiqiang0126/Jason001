#userpw.py @shiqiang 2019
''' password and account login/setup'''

db={}

def newuser():
    prompt="New login account disired:"
    while True:
        name = input(prompt)
        if name in db:
            prompt='Name already has, try another:'
            continue
        else:
            break
    while True:
        pwd=input("New passwd:")
        pwd2=input("passwd again:")
        if pwd == pwd2:
            db[name]=pwd        
            print('passwd ok,account setup done!')
            break
        else:
            print('passwd bed! enter again...')
            continue

def olduser():
    name=input("login account:")
    pwd=input("passwd:")
    passwd=db.get(name)
    if passwd==pwd:
        print("wellcome back,the door is opened....")
    else:
        print("login fail,go home guy...")
        
def showmenu():
    prompt="""
(N)ew User login
(E)xisting User login
(Q)uit system
Enter your choice:"""
    done=False
    while not done:
        chosen=False
        while not chosen:
            try:
                choice=input(prompt).strip()[0].lower()
            except(EOFError,KeyboardInterrupt):
                choice='q'
            print("\nYou picked:[%s]"%choice)
            if choice not in 'neq':
                print("Invalid option,try again guy...")
            else:
                chosen=True

        if choice=='q':
            print("Byebye,see you next time guy...")
            done=True
        if choice=='n': newuser()
        if choice=='e': olduser()

if __name__=='__main__':
    showmenu()
    

        
        


    
