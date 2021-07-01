import random, os, sys 
computerscore = 0
userscore = 0
numgames = int(input("Welcome to rock, paper, scissors.\nHow many games would you like to play?\n"))
userinput = ""
computerchoice = ""
userwin = False
draw = False
choice = ""
clear = lambda: os.system("cls")

for x in range(0, numgames):
    generatednum = random.randint(1,3)
    if generatednum == 1:
        computerchoice = "rock"
    elif generatednum == 2:
        computerchoice = "paper"
    elif generatednum == 3:
        computerchoice = "scissors"

    userinput = input("Select rock, paper, or scissors\n")

    if userinput == "rock" and computerchoice == "scissors":
        print("You selected",userinput,"and the computer selected",computerchoice,"You won this round!")
        userscore += 1
    elif userinput == "rock" and computerchoice == "paper":
        print("You selected",userinput,"and the computer selected",computerchoice,"You lost this round!")
        computerscore += 1
    if userinput == "paper" and computerchoice == "rock":
        print("You selected",userinput,"and the computer selected",computerchoice,"You won this round!")
        userscore += 1
    elif userinput == "paper" and computerchoice == "scissors":
        print("You selected",userinput,"and the computer selected",computerchoice,". You lost this round!")
        computerscore += 1
    if userinput == "scissors" and computerchoice == "paper":
        print("You selected",userinput,"and the computer selected",computerchoice,"You won this round!")
        userscore += 1
    elif userinput == "scissors" and computerchoice == "rock":
        print("You selected",userinput,"and the computer selected",computerchoice,"You lost this round!")
        computerscore += 1

if userscore > computerscore:
    userwin = True
elif userscore == computerscore:
    draw = True

if userwin == True:
    print("Congratulations, you won!\nYour score:",userscore,"\nComputer's score:",computerscore)
elif draw == True:
    print("You drew!\nYour score:",userscore,"\nComputer's score:",computerscore)
elif userwin == False:
    print("I'm sorry, but you lost.\nYour score:",userscore,"\nComputer's score:",computerscore)

choice = str(input("Would you like to play again? y/n\n"))
if choice == "y":
    clear()
    os.system("rockpaperscissors.py")
