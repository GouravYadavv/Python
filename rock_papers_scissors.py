import random
user_wins=0
computer_wins=0
options=["rock","papers","scissors"]
while True:
    user_input=input("Choose between rocks, papers and scissors:").lower()
    if user_input=="q" :
        break
    elif user_input not in options:
        continue

    computer_picks=random.randrange(0,2)
    computer_input=options[computer_picks]

    print("computer choose:",computer_input)

    if user_input=="papers" and computer_input=="rock":
        print("You won")
        user_wins+=1
        continue

    elif user_input=="rock" and computer_input=="scissors":
        print("You won")
        user_wins+=1
        continue

    elif user_input=="scissors" and computer_input=="paper":
        print("You won")
        user_wins+=1
        continue

    else:
        print("computer wins!")
        computer_wins+=1

print("you won",user_wins,"time.")
print("computer won",computer_wins,"time.")
print("Good Bye!!")
            