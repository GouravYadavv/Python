import cryptography
def view():
    with open("password.txt",'r') as f:
        for line in f.readlines():
            print(line.rstrip())

def change():
    id=input("enter the user name:")
    password=input("enter the password name:")
    with open("password.txt",'a') as f:
        f.write(id + "|" + password + "\n")
    
pwd=input("Enter the master password")

while True:
    mode=input("What you want to do? Choose either view() or change()")
    if mode=="view":
        view()
    elif mode=="change":
        change()
        
    elif mode=="q":
        break
    else:
        print("invalid input")
        continue