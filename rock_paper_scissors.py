from art import rock
from art import paper
from art import scissors
import random

print("For Rock, Enter 0")
print("For Paper, Enter 1")
print("For Scissors, print 2")
user_input = int(input("What do you want to choose? Rock, Paper of Scissors. "))
if user_input == 0:     
    print("User chose:", rock)
elif user_input == 1:     
    print("User chose:", paper)
elif user_input == 2:     
    print("User chose:", scissors)
else:     
    print("Wrong Input!!")

computer_input = random.randint(0,2)
if computer_input == 0:     
    print("Computer chose:", rock)
elif computer_input == 1:
    print("Computer chose:", paper)
elif computer_input ==2:
    print("Computer chose:", scissors)

if user_input == 0 and computer_input == 0:
    print("Game is tied.")
elif user_input == 0 and computer_input == 1:
    print("You lost.")
elif user_input == 0 and computer_input == 2:
    print("You won.")
elif user_input == 1 and computer_input == 0:
    print("You won.")
elif user_input == 1 and computer_input == 1:
    print("Game is tied.")
elif user_input == 1 and computer_input == 2:
    print("You lost.")
elif user_input == 2 and computer_input == 0:
    print("You lost.")
elif user_input == 2 and computer_input == 1:
    print("You won.")
elif user_input == 2 and computer_input == 2:
    print("Game is tied.")