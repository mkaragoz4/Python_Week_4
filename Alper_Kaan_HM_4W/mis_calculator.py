### All Rights Reserved ###
'''
Developer: Alper Kaan
Date: 25.02.2021
Purpose of Software: mis_calculator
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
As a user, I want to use a program which can calculate basic mathematical operations. So that I can add, subtract,
multiply or divide my inputs.

Acceptance Criteria:

The calculator must support the Addition, Subtraction, Multiplication and Division operations.
Define four functions in four files for each of them, with two float numbers as parameters.
To calculate the answer, use math.ceil() and get the next integer value greater than the result Create a menu using
the print command with the respective options and take an input choice from the user. Using if/elif statements for
cases and call the appropriate functions. Use try/except blocks to verify input entries and warn the user for incorrect inputs.
Ask user if calculate numbers again. To implement this, take the input from user Y or N.
'''
import math

def addition(x,y):
    return x+y

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x, y):
   return math.ceil(x / y)

answer = "Y"
while (answer == "Y"):
   
    choice = input("Operation to perform:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\nEnter choice: ")
    
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {addition(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {subtraction(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiplication(num1, num2)}")

        elif choice == '4':
            print(f"{num1} / {num2} = {division(num1, num2)}")
    except ValueError:
        print("please enter a number")
    except ZeroDivisionError:
        print(f"Second number = 0\n{num1} can't be divided by zero\nPlease enter a different number")

    answer = input("Do you want to do a new calculation? Y/N:\n").upper()
    while (answer != "N" or answer != "Y" ):
        if answer == "N":
            break
        elif answer == "Y":
            answer == "Y"
            break
        else:
            answer= input("You made an invalid choice.\nPlease press N to exit\nY to continue\nAnswer: ").upper()
            
print("!!! THANK YOU !!!")

### All Rights Reserved ###

#Copyright (c) ${mis_calculator.2021} ${Alper_Kaan}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.