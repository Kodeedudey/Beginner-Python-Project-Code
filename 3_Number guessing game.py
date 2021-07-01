import random
print("Welcome to the number guessing game\n")
print("You have to guess a random number between 10 to 40\n")
print("There will be 5 attempts in total\n")
print("If the guessed number is low, guess a higher number\n")
print("If the guessed number is high, guess a lower number\n")
print("Let's start the Game\n")

n=random.randint(10,40)

for i in range(1,6):
    print("\nGuess the number: ")
    x=int(input())
    if(x==n):
        print("\nYou guessed the right number ",n," in ",i," steps")
        break
    elif(x>n):
        print("\nGuess is high")
    else:
        print("\nGuess is low")

else:
    print("\nGame Over")
    print("\nThe magice number was ",n)
