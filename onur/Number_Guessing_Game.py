import time
from random import randint


A=int(input("Enter first number: "))
B=int(input("Enter stop number : "))
rand_number=randint(A,B)
count=1
current_time=time.time()
print("********************************************")
print("\t\tLets game begin!")
print("********************************************")

while True:
    guess=int(input("Make your attempt : "))
    range_to_num=(abs(guess-rand_number))/float(B-A)
    if rand_number==guess:
        stop_time=time.time()
        print("********************************************")
        print("********************************************")
        print("Congrutulations, you knew it :",guess)
        print("You tried", count,"times")
        print("your total time is :", round(stop_time-current_time,2)," seconds")
        print("********************************************")
        break
    elif guess>rand_number and range_to_num<=0.1:
        print("You are little bit high")
    elif guess>rand_number and range_to_num<=0.2:
        print("You are very high")
    elif guess>rand_number:
        print("You are very very high")
    elif guess < rand_number and range_to_num <= 0.1:
        print("You are little bit low")
    elif guess < rand_number and range_to_num <= 0.2:
        print("You are very low")
    else :
        print("You are very very low")

    count+=1





