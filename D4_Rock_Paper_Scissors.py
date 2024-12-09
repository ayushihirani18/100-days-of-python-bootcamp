import random

print("Welcome!\n LETS PLAY THE RPS")
user = int(input("Enter 0 for rock, 1 for paper, 2 for scissors:\n"))
rps = [0,1,2]
comp = random.choice(rps)
if user == 0 :
    if comp == 0:
        print("Computer chose rock")
        print("draw")

    elif comp==1:
        print("Computer chose Paper.")
        print("You lose")
    else:
        print("Computer chose Scissors.")
        print("You win.")

elif user == 1 :
    if comp == 0:
        print("Computer chose rock")
        print("You Win")

    elif comp==1:
        print("Computer chose Paper.")
        print("Draw")
    else:
        print("Computer chose Scissors.")
        print("You lose")

else:
    
    if comp == 0:
        print("Computer chose rock")
        print("You lose")

    elif comp==1:
        print("Computer chose Paper.")
        print("You win")
    else:
        print("Computer chose Scissors.")
        print("Draw")

