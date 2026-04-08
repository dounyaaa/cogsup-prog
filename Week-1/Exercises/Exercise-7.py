"""
Have a look at the script called 'human-guess-a-number.py' (in the same folder as this one).

Your task is to invert it: You should think of a number between 1 and 100, and the computer 
should be programmed to keep guessing at it until it finds the number you are thinking of.

At every step, add comments reflecting the logic of what the particular line of code is (supposed 
to be) doing. 
"""


from random import randint

lower_step = 1
higher_step= 101

def check_answer(ind):
    return (ind.lowercase()== "right" or ind.lowercase()== "higher" or ind.lowercase()=="lower")


def ask_indication(prompt):
    """ Asks user for an integer input. If valid, the string input is returned as an integer. """
    ind = input(prompt) # Ask the user for their indication
    while not check_answer(ind): # Repeat until the user inputs a valid indication
        print('Please, enter higher, lower or right')
        ind = input(prompt)  
    return ind

def choose_number(ind, previous):
    if (ind == "lower"):
        higher_step=previous
        



target = randint(1, 100) # Computer selects a random number between 1 and 100 inclusive
print("Think of a number between 1 and 100, I'll try to guess it. Write lower if my guess is to high and higher if my guess it too low. If I'm right, say right/")
ind = output_integer("Your guess (1-100)? ")

while guess != target: # Repeat until the user guesses.
    print("Your guess is too low!") if guess < target else print("Your guess is too high!\n")
    guess = input_integer("New guess? ")

print("You win! The number was indeed " + str(target))