"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
"""

import tkinter as tk
from tkinter import *

win=tk.Tk()
win.geometry('600x400')
wordlist=['Adjective','Adjective','Noun','Noun','Plural Noun','Game','Plural Noun','Verb Ending in Ing','Verb Ending in Ing','Plural Noun','Verb Ending in Ing','Noun','Plant','Part of the Body','A place','Verb Ending in Ing','Adjective','Number','Plural Noun']
wordtype=StringVar()
output=StringVar()
l1=tk.Label(win,text='Enter the next word')
e1=tk.Entry(win,width=20)
wtype=tk.Label(win,textvariable=wordtype)
l2=tk.Label(win,textvariable=output)
wordlist2=[]
wordtype.set(wordlist[0])
count=0

def wordEntry():
    global count
    word=e1.get()
    word=str(word)
    wordlist2.append(word)
    e1.delete(0,END)
    
    count=count+1
    wordtype.set(wordlist[count])
    print(wordlist2)
    length=len(wordlist2)
    if length==18:
        displayMadLib()

def displayMadLib():
    output.set('A vacation is when you take a trip to some'+wordlist2[0]+' place with your'+wordlist2[1]+'family. Usually you go to some place\n that is near a/an '+wordlist2[2]+' or up on a/an '+wordlist2[3]+'.\n A good vacation place is one where you can ride '+wordlist2[4]+'\n or play '+wordlist2[5]+' or go hunting for '+wordlist2[6]+' . I like\n to spend my time '+wordlist2[7]+' or '+wordlist2[8]+'.\n When parents go on a vacation, they spend their time eating\n three '+wordlist2[9]+' a day, and fathers play golf, and mothers\n sit around '+wordlist2[10]+'. Last summer, my little brother\n fell in a/an '+wordlist2[11]+' and got poison '+wordlist2[12]+' all\n over his'+wordlist2[13]+'. My family is going to go to (the)\n '+wordlist2[14]+', and I will practice '+wordlist2[15]+'. Parents\n need vacations more than kids because parents are always very\n '+wordlist2[16]+' and because they have to work'+wordlist2[17]+'\n hours every day all year making enough '+wordlist2[18]+' to pay\n for the vacation.')



button1=tk.Button(win,text='Press to commit the word',command=wordEntry)



l1.grid(row=2,column=1)
e1.grid(row=2,column=2)
wtype.grid(row=1,column=2)
button1.grid(row=3,column=2)
win.mainloop()
    