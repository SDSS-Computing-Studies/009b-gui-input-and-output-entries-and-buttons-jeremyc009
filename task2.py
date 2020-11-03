"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""
import tkinter as tk
from tkinter import *

win=tk.Tk()
l1=tk.Label(win,text='This is a program to factor\n quadratic functions of the form\n ax^2 + bx + c.')
a1=tk.Label(win,text='ax^2 ')
b1=tk.Label(win,text='x ')
b2=tk.Entry(win,width=10)
c2=tk.Entry(win,width=10)
buttonvar1=StringVar()
buttonvar2=StringVar()

cs1a=['+']
cs1b=['-']
cs2a=['+']
cs2b=['-']
signMenu1=tk.OptionMenu(win,buttonvar1,cs1a,cs1b)
signMenu2=tk.OptionMenu(win,buttonvar2,cs2a,cs2b)






l1.grid(row=1,column=1)
a1.grid(row=2,column=1,sticky=E)
signMenu1.grid(row=2,column=2)
b2.grid(row=2,column=3)
b1.grid(row=2,column=4)
signMenu2.grid(row=2,column=5)
c2.grid(row=2,column=6)



win.mainloop()