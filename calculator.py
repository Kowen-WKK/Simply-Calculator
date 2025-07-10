import math
from tkinter import *

window = Tk()                                         
window.title("Calculator")                            #the title of the window

displaybar = Entry(window, width=35, borderwidth=5)   #make an entry with 
displaybar.grid(row=0, column=0, columnspan=4)        #the location of the entry
displaybar.delete(0, END)                             #clear the entry
displaybar.focus()                                    #when the program startred, it will be able to enter number from keyboard 

# define button function

def click(number):
    current = displaybar.get()             #value
    displaybar.delete(0, END)              #clear the entry
    displaybar.insert(0, str(current) + str(number))  #merge the number together

def add():
    first_number = displaybar.get()        #getting the value from the entry and store it into a valuable
    global f_num                           #global variable
    global math                            #global variable
    math = "addition"                      #passing parameters
    f_num = int(first_number)              #passing parameters
    displaybar.delete(0, END)              #clear the entry
    

def subtract():
    first_number = displaybar.get()        #getting the value from the entry and store it into a valuable
    global f_num                           #global variable
    global math                            #global variable
    math = "subtraction"                   #passing parameters
    f_num = int(first_number)              #passing parameters
    displaybar.delete(0, END)              #clear the entry

def multiply():
    first_number = displaybar.get()        #getting the value from the entry and store it into a valuable
    global f_num                           #global variable 
    global math                            #global variable 
    math = "multiplication"                #passing parameters
    f_num = int(first_number)              #passing parameters
    displaybar.delete(0, END)              #clear the entry
    
def divide():
    first_number = displaybar.get()        #getting the value from the entry and store it into a valuable
    global f_num                           #global variable 
    global math                            #global variable 
    math = "division"                      #passing parameters
    f_num = int(first_number)              #passing parameters
    displaybar.delete(0, END)              #clear the entry

def equal():
    second_number = displaybar.get()       #getting the value from the entry and store it into a valuable
    displaybar.delete(0, END)              #clear the entry

    if math == "addition":             # condition
        displaybar.insert(0, f_num + int(second_number))   #doing calculation

    if math == "subtraction":          # condition
        displaybar.insert(0, f_num - int(second_number))   #doing calculation
    
    if math == "multiplication":       # condition
        displaybar.insert(0, f_num * int(second_number))   #doing calculation

    if math == "division":             # condition
        displaybar.insert(0, f_num / int(second_number))   #doing calculation

def clear():
    displaybar.delete(0, END)              #clear the entry

# Define buttons

# Valuable_name = type  (where it shows, what it shows,     what to do     , x-size , y-size) 
button_1 = Button(window, text="1", command = lambda: click(1), padx=40, pady=20)
button_2 = Button(window, text="2", command = lambda: click(2), padx=40, pady=20)
button_3 = Button(window, text="3", command = lambda: click(3), padx=40, pady=20)
button_4 = Button(window, text="4", command = lambda: click(4), padx=40, pady=20)
button_5 = Button(window, text="5", command = lambda: click(5), padx=40, pady=20)
button_6 = Button(window, text="6", command = lambda: click(6), padx=40, pady=20)
button_7 = Button(window, text="7", command = lambda: click(7), padx=40, pady=20)
button_8 = Button(window, text="8", command = lambda: click(8), padx=40, pady=20)
button_9 = Button(window, text="9", command = lambda: click(9), padx=40, pady=20)
button_0 = Button(window, text="0", command = lambda: click(0), padx=40, pady=20)
button_add = Button(window, text="+", command = lambda: add(), padx=40, pady=20)
button_subtract = Button(window, text="-", command = lambda: subtract(), padx=40, pady=20)
button_multiply = Button(window, text="*", command = lambda: multiply(), padx=40, pady=20)
button_divide = Button(window, text="/", command = lambda: divide(), padx=40, pady=20)
button_equal = Button(window, text="=", command = lambda: equal(), padx=40, pady=20)
button_clear = Button(window, text="C", command = lambda: clear(), padx=40, pady=20)

# Put the buttons on the screen
# Setting location
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_equal.grid(row=4, column=2)
button_clear.grid(row=4, column=1)

# running the code
window.mainloop() 
