### All Rights Reserved ###
'''
Developer: Alper Kaan
Date: 25.02.2021
Purpose of Software: NumberGuessingGame
'''
#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
'''
---PROJECT---
As a player, I want to play a game which I can guess a number the computer chooses in the range I chose.
So that I can try to find the correct number which was selected by computer.

Acceptance Criteria:
Computer must randomly pick an integer from user selected a range, i.e., from A to B, where A and B belong to Integer.
Your program should prompt the user for guesses if the user guesses incorrectly, it should print whether the guess is too high or too low.
If the user guesses correctly, the program should print total time and total number of guesses.
You must import some required modules or packages You can assume that the user will enter valid input.
'''
import random
import time

start = time.time()
xnum = random.randint(1,100)
count= 0
num= int(input("please enter a number between 1 and 100: "))
while (xnum != num):
    if num < xnum:
        print(f"Please enter a number greater than {num}: ")
        num = int(input())
        count +=1
    else:
        print(f"Please enter a number less than {num}: ")
        num = int(input())
        count +=1


end = time.time()
sure= end-start
print(f"Congratulations !!! You found the number {num} in {count} attempts in {round(sure,2)} seconds.")

### All Rights Reserved ###

#Copyright (c) ${NumberGuessingGame.2021} ${Alper_Kaan}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.