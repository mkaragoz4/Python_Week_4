'''
Developer: Furkan Sürücü
Purpose of Software: Reinforcement of learned python code and self-improvement
What does program do?: As a player, I want to play a game which I can guess a number the computer chooses in the range I chose.
So that I can try to find the correct number which was selected by computer.
'''

import random, time
def number_guessing_game ():

    x = int(input("Enter a lower bound number:\n"))
    y = int(input("Enter a upper bound number:\n"))

    hidden_number = random.randint(x,y)
    count = 0
    while True:
        count +=1
        t0 = time.time() #starting time
        guess = int(input("Guess a number:"))
        if guess == hidden_number:
            elapsed_time = time.time()-t0 #elapsed time
            elapsed_time = round(elapsed_time,2)
            print("Hey! You guessed the number in",count,"try and",elapsed_time,"seconds, congratulations!")
            break
        elif guess > hidden_number:
            print("You guessed too high :(")
        elif guess < hidden_number:
            print("You guessed too small :(")
number_guessing_game()



