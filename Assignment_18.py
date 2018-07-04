#Question 1

import tkinter as tk
from tkinter import *
nav=tk.Tk()
nav.title("info")
dict={'Name':' Naveen','Mobile Number': 8628912069}
scrollbar=Scrollbar(nav)
scrollbar.pack(side=LEFT,fill=Y)
mylist=Listbox(nav,yscrollcommand= scrollbar.set)
for key in dict.__iter__():
        mylist.insert(END,key)
mylist.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=mylist.yview)
def naveen():
    nav.quit()
b=Button(nav,text="Enter",fg='green',width=20,command=naveen)
b.pack()
nav.mainloop()


#Question 2

def naveen():
    dict.update({" age":20})
    print(dict)
button1=Button(nav,text='Insert',fg='blue',width=20,command=naveen)
button1.pack()
nav.mainloop()