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
import math
win=tk.Tk()
l1=tk.Label(win,text='This is a program to factor\n quadratic functions of the form\n ax^2 + bx + c.')
a1=tk.Label(win,text='ax^2 ')
b1=tk.Label(win,text='x')
b2=tk.Entry(win,width=10)
c2=tk.Entry(win,width=10)
buttonvar1=StringVar()
buttonvar2=StringVar()
resultvar1=StringVar()
resultvar2=StringVar()
finalvar=StringVar()
final=tk.Entry(win,width=20,textvariable=finalvar)

cs1a=['+']
cs1b=['-']
cs2a=['+']
cs2b=['-']
signMenu1=tk.OptionMenu(win,buttonvar1,cs1a,cs1b)
signMenu2=tk.OptionMenu(win,buttonvar2,cs2a,cs2b)

def factor():
    sign1=buttonvar1.get()
    sign2=buttonvar2.get()
    print(sign2)
    print(sign1)

    b=int(b2.get())
    if sign1=="('-',)":
        b=b*-1
    
    c=int(c2.get())
    if sign2=="('-',)":
        c=c*-1
    print(b)
    print(c)
    x1=(((-1 * b) + math.sqrt(b**2 - (4 * 1 * c)))/2)
    x2=(((-1 * b) - math.sqrt(b**2 - (4 * 1 * c)))/2)


    if x1<0:
        resultvar1.set("(x + "+str(abs(x1))+')')
    if x2<0:
        resultvar2.set('(x + '+str(abs(x2))+')')
    if x1==0:
        resultvar1.set('(x)')
    if x2==0:
        resultvar2.set('(x)')
    if x1>0:
        resultvar1.set('(x - '+str(abs(x1))+')')
    if x2>0:
        resultvar1.set('(x - '+str(abs(x2))+')')


    finalvar.set(str(resultvar1.get())+str(resultvar2.get()))

mainButton=tk.Button(win,text='Press this to factor',command=factor)


l1.grid(row=1,column=1)
a1.grid(row=2,column=1,sticky=E)
signMenu1.grid(row=2,column=2)
b2.grid(row=2,column=3)
b1.grid(row=2,column=4)
signMenu2.grid(row=2,column=5)
c2.grid(row=2,column=6)
mainButton.grid(row=3,column=3)
final.grid(row=4,column=3)


win.mainloop()