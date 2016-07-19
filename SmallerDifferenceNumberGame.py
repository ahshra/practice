
# This is a difference between random numbers decision-making game. It enables the winner 
# tell the loser what to do based on whose difference is smaller.


from random import randint
from time import sleep

def get_user_guess():
  user_guess1 = int(raw_input('What\'s Player One\'s guess? '))
  return user_guess1

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  
  print "WELCOME! Whoever's guessed number has the smallest diffence between that number and a randomly \
generated number by this program wins! Then the loser has to do what the winner says! \
The max value for the guesses is between 0 and %d." % (max_val) 
  
  sleep(1)
  user_guess1 = get_user_guess()
  if user_guess1 > max_val:
      print "Guess invalid. Must be between 0 and the max number."
      return
  else:
    print "Generating..."
    sleep(2)
    print "The first random number is %d and Player One's guess was %d. " % (first_roll, user_guess1)
    difference_user1 = abs(first_roll - user_guess1)
    print "The difference between Player One\'s guess and the randomly generated number is %d. " % (difference_user1)
    sleep(2)
    user_guess2 = int(raw_input('What\'s Player Two\'s guess? '))
    print "The second random number is %d and Player Two\'s guess was %d. " % (second_roll, user_guess2)
    difference_user2 = abs(second_roll - user_guess2)
    print "The difference between Player Two's guess and the randomly generated number is %d. " % (difference_user2)
    sleep(1)
  if  difference_user2 < difference_user1:
    print "Player Two has the smaller difference and he wins!"
  elif difference_user1 < difference_user2:
    print "Player One has the smaller difference and she wins!"
  elif difference_user1 == difference_user2:
  	print "Tie game. Try again!"

roll_dice(6)