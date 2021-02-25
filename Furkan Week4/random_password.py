'''
Developer: Furkan Sürücü
Purpose of Software: Reinforcement of learned python code and self-improvement
What does program do?: As a user, I want to use a program which can generate random password and display the result on user interface.
So that I can generate my password for any application.
'''

import random, string
import tkinter as tk
def password_creater():
    length = 10 #password length
    uppers = string.ascii_uppercase #return all uppercase letter
    digits = string.digits #return all digits
    special_symbols = '!@#$%^&*():;,.-_*<>'
    chars = string.ascii_letters + string.digits + special_symbols # combining all ascii leters, digits and symbols
    pas = ''.join(random.choice(uppers) for i in range(2))
    sw = ''.join(random.choice(digits) for i in range(2))
    ord = ''.join(random.choice(special_symbols) for i in range(2))
    # contain at least 2 upper case letter, 2 digits and 2 special symbols.
    password = pas + sw + ord +''.join(random.choice(chars) for i in range(length-6))
    new_password = ''.join(random.sample(password,len(password))) #shuffle and return  a list than converting string
    label.config(text=new_password)
    return new_password



window= tk.Tk()
window.title("Password  Generator")
window.geometry("600x300")

frame = tk.Frame(window)
frame.grid()

label_text = tk.Label(frame, text="Password is: ",font="arial 17")
label_text.grid(padx = 120, pady = 10)

label = tk.Label(frame, text ="Click the button to generate a password",font="arial 14" )
label.grid(padx = 120, pady = 20)


button = tk.Button(frame,text="Hit to Generate",width= 70, height=7,command=password_creater)
button.grid(padx =120 , pady = 50)

window.mainloop()






