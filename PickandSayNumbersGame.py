#This is a numbers game. The user picks a number 1 through 10. 
#The computer also picks a number. The user also 'says' another number 1 through 10 
#and the computer 'says' a number. If the sum of the picked numbers equals the numbers the 
#user said or the computer said then the user or computer wins. Ties are possible. 

from random import randint
from time import sleep
options = [1,2,3,4,5,6,7,8,9,10]

LOSE_MESSAGE = "What the computer said is equal to what the user chose and the computer \
chose! The computer wins!"
WIN_MESSAGE = "What the user said is equal to what the user chose and the computer chose! The user \
wins!"

def decide_winner(user_choice, user_say, computer_choice, computer_say):    
    print "Computer choosing and saying..."
    sleep(1)
    print "The user's choice is %s, the computer's choice is %s" % (user_choice, computer_choice)
    print "The user said %s, the computer said %s" % (user_say, computer_say)
    if int(user_choice) + int(computer_choice) == int(computer_say):
        print LOSE_MESSAGE
    elif int(user_choice) + int(computer_choice) == int(user_say):
        print WIN_MESSAGE
    else:
        print "No one won. Try again!"

def play_numbers():
    print "Choose a number 1 though 5. Then 'say' a number 1 through 10. \
    The computer will then choose and 'say' a number." 
    user_choice = raw_input("What does the user choose? ")
    user_say = raw_input("What does the user say? ")
    sleep(1)
    computer_choice = options[randint(0, 5)]
    computer_say = options[randint(0, 10)-1]
    decide_winner(user_choice, user_say, computer_choice, computer_say)
play_numbers()