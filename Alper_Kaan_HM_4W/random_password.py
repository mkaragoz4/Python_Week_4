### All Rights Reserved ###
'''
Developer: Alper Kaan
Date: 25.02.2021
Purpose of Software: random_password
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
As a user, I want to use a program which can generate random password and display the result on user interface.
So that I can generate my password for any application.

Acceptance Criteria:
Password length must be 10 characters long. It must contain at least 2 upper case letter, 2 digits and 2 special symbols.
You must import some required modules or packages. The GUI of program must contain at least a button and a label.
The result should be display on the password label when the user click the generate button.
'''
import random
import string

def new_func():
    password = set()
    while(True):
        for i in range(2):
            a= random.choice(string.ascii_uppercase)
            b= random.choice(string.digits)
            c= random.choice(string.punctuation)
            password.add(a)
            password.add(b)
            password.add(c)
        for i in range(4):
            d= random.choice(string.ascii_lowercase)
            password.add(d)
            password.add(a)
        if len(password) == 10:
            break
        else:
            password=set()
    return password

password = new_func()


password = ''.join(password)
print(f"Your Password : {password}")

'''
ALTERNATIVE
#importing Libraries
from tkinter import *
import random, string
import pyperclip

###initialize window
root =Tk()
root.geometry("350x350")
#root.resizable(0,0)
root.title("InfoTechAcademy - RANDOM PASSWORD GENERATOR")

#heading
heading = Label(root, text = 'PASSWORD GENERATOR' , font ='arial 15 bold').pack()

Label(root, text ='InfoTechAcamedy', font ='arial 13 bold').pack(side = BOTTOM)

#####define function
pass_str = StringVar()
def Generator():
    password = ''
    for x in range (0,6):
        password = random.choice(string.ascii_uppercase)+random.choice(string.ascii_uppercase)+random.choice(string.digits)+random.choice(string.digits)+random.choice(string.punctuation)+random.choice(string.punctuation)
    for y in range(4):
        password = password+random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)

###button
Button(root, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 5)
Entry(root , textvariable = pass_str).pack()

########function to copy
def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)

# loop to run program
root.mainloop()
'''

### All Rights Reserved ###

#Copyright (c) ${Random_password.2021} ${Alper_Kaan}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

