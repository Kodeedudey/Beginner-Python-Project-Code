def invalid():
    print("Answer not valid")
def game():
    Answer = input("You saw a bear in woods, what would you do?\nA) Give bear a hug\nB) Run as fast as you can\n>? ")
    if Answer == ("A"):
           print("The bear attacked on you!")
           Answer2 = input("The bear is still there, what will you do now?\nA) Lay down and die\nB) Or fight back\n>? ")
           if Answer2 == ("A"):
               print("Sorry, you bled out and died")
           elif Answer2 == ("B"):
               print("You fought back\n But failed and died")
    elif Answer == ("B"):
           Answer3 = input("Bear is coming after you, but you find a tree. what would you do?\nA) Climb the tree\nB) Hide behind it\n>? ")
           if Answer3 == ("A"):
               print("Cograts, you're safe. The bear went away!")
               print("You walked home and slept")
           elif Answer3 == ("B"):
               Answer4 = input("Your foot slept and you feel down in a village, what would you do?\nA) Do business with Villager\nB) Head home\n>? ")
               if Answer4 == ("A"):
                   Answer5 = input("Only one merchant is there in the village, will you trade with him?\nA) Yes\nB) No")
                   if Answer5 == ("A"):
                       print("You bought a steel sword for two gold coins")
                       print("You headed home")
                   elif Answer5 == ("B"):
                       print("You didn't trade and went home")
                   else:
                       invalid()
               elif Answer4 == ("A"):
                   print("You headed home")
               else:
                   invalid()
           else:
               invalid()
    else:
        invalid()
game()
