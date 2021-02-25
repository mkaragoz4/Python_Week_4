#===================4 Random Password======================================
# Developer: Cemil Tepecik
# Date:25.02.2021
#As a user, I want to use a program which can generate random password and display the result on user interface.
# So that I can generate my password for any application.
#Acceptance Criteria:
#Password length must be 10 characters long. It must contain at least 2 upper case letter, 2 digits and 2 special symbols.
# You must import some required modules or packages. The GUI of program must contain at least a button and a label.
# The result should be display on the password label when the user click the generate button.

#-----------import modules---------------------------------
import tkinter
import random
import string

#-----------------function: 10 char password generation---------------
def random_key10():
    key = random.sample(string.digits, 2) + \
          random.sample(string.punctuation[0:14], 2) + \
          random.sample(string.ascii_uppercase, 2) + \
          random.sample(string.printable[0:76], 4)
    print(key)
    random.shuffle(key)
    print(key)
    str = ''
    for i in key:
        str += i
    print(str)
    label.config(text=str)  # bu bolum display penceresi ile iliskilendiriyor
    return str
#---------------------function: 20 char password generation-----------
def random_key20():
    key = random.sample(string.digits, 10) + \
          random.sample(string.ascii_lowercase, 10)
    print(key)
    random.shuffle(key)
    print(key)
    str = ''
    for i in key:
        str += i
    print(str)
    label.config(text=str)  # bu bolum display penceresi ile iliskilendiriyor
    return str

#----------------generating the window----------------------
window =tkinter.Tk()
window.title("InfoTechAcademy")
window.geometry("550x450")

key_application = tkinter.Frame(window)
key_application.grid()

# label
label_txt = tkinter.Label(key_application, text="Password:", font="arial 15 bold")
label_txt.grid(padx=100, pady=20)

# label insert
label = tkinter.Label(key_application, text="Please push the botton to generate a password!", font="arial 14")
label.grid(padx=100, pady=20)

# button insert
button1 = tkinter.Button(key_application, text=" GENERATE \n (10 Character)", width=25, height=4, command=random_key10, font="arial 14")
button1.grid(padx=100, pady=20)

button2 = tkinter.Button(key_application, text=" GENERATE \n (20 Character) ", width=25, height=4, command=random_key20, font="arial 14")
button2.grid(padx=150, pady=20)
#Label(mode,text="Password Generator", font="arial 15 bold").pack()
#Label(key_application,text="InfoTechAcademy", font="arial 11 bold").pack(side=BOTTOM)

window.mainloop()
#======================END================================================================