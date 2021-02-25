import random
import time


def rand_find(a, b):
    lst = [i for i in range(a, b + 1)]
    chosen = random.sample(lst, 1)
    return chosen[0]


def control_selection(c, p):
    global t0
    global t1
    global count
    global final
    if count==0:
        t0 = time.time()
    if c - p < 0:
        count += 1
        return print("\nthe guess is too high!")
    elif c - p > 0:
        count += 1
        return print("\nthe guess is too low!")
    else:
        count += 1
        t1 = time.time()
        final = 1
        return print("\n"+str(c) + " is correct answer")


count = 0
final = 0
r1 = int(input("Please enter the starting range as an integer: "))
r2 = int(input("Please enter the finish range as an integer: "))

com_chosen = rand_find(r1, r2)

while True:
    player_input = int(input("Please chose your guess: "))
    control_selection(com_chosen, player_input)

    if final == 1:
        print("Congratulations!")
        print("Total selection: ", count)
        print("Total time: ", int(t1 - t0)," second")
        break
    else:
        print("Your selection is false, Please try again!")
print("The game finished!")
