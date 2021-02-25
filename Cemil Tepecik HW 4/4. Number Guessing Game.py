#******************************Number Guessing Game****************************
# Developer: Cemil Tepecik
# Date:23.02.2021
#Computer must randomly pick an integer from user selected a range, i.e., from A to B, where A and B belong to Integer.
# Your program should prompt the user for guesses if the user guesses incorrectly,
# it should print whether the guess is too high or too low. If the user guesses correctly, the program should print
# total time and total number of guesses. You must import some required modules or packages You can assume that the user
# will enter valid input.
#---------------------------------INITIAL PART-----------------------------
import random
x=list(range(1,101))
import time
from math import ceil
a=random.choice(x)
tic=ceil(time.perf_counter()) #open timer
#======================================MAIN PART=================================00
guessed_number=int(input('please enter your first guess between 1 an 100\n'))
counter=1
while guessed_number!=a:
    if guessed_number==a:
        print('You found the number. Congragulations! The number is:',guessed_number)
        break
    elif guessed_number<a:
        print('Your number is too low!')
        guessed_number = int(input('please enter your guess between 1 an 100:\n'))
    else:
        print('Your number is too high!')
        guessed_number = int(input('please enter your guess between 1 an 100:\n'))
    counter += 1

toc = ceil(time.perf_counter()) #close timer
#==============================0====FINAL PART========================================000
if toc-tic<10:
    print('Congragulations! Your performance is amazing. Guessing time is ', toc - tic, ' second. You have tried',counter,'times.')
elif 10<=toc-tic<20:
    print('Good! Guessing time is ', toc - tic, ' second. You have tried',counter,'times.')
elif 20<=toc-tic<30:
    print('Your performance is bad, wash your face before playing this game man! Guessing time is ', toc - tic, ' second. You have tried',counter,'times.')
elif 30 <= toc - tic :
    print('Your performance is terrible! You can not play this game while you are asleep. Guessing time is ', toc - tic, ' second. You have tried',counter,'times.')
#===================================END===================================================================00

#===========================OUTPUT========================================0
#please enter your first guess between 1 an 100
#50
#Your number is too high!
#please enter your guess between 1 an 100:
#25
#Your number is too low!
#please enter your guess between 1 an 100:
#35
#Your number is too high!
#please enter your guess between 1 an 100:
#30
#Your number is too low!
#please enter your guess between 1 an 100:
#33
#Your number is too low!
#please enter your guess between 1 an 100:
#34
#Good! Guessing time is  16  second. You have tried 6 times.