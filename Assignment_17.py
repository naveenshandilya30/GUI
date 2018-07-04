#Question 1


from tkinter import *

r =Tk()
frame=Frame(r)
frame.pack()
rb=Button(frame,text='Hello world',fg='blue')
rb.pack(side=LEFT)
bb=Button(frame,text='exit',fg='red',command=quit)
bb.pack(side=LEFT)
r.mainloop()



#Question 2

import tkinter as tk

def Hello():
   print("Hello World")
r= tk.Tk()
r.title("Program")
button1= tk.Button(r,text="Hello World",width=20,fg="green",command=Hello)
button1.pack(side=tk.TOP)
button2= tk.Button(r,text="QUIT",width=20,fg="red",command=quit)
button2.pack(side=tk.TOP)
r.mainloop()



#Question 3..

from tkinter import *

root =Tk()
frame=Frame(root,bg='red')
frame.pack()
def click():
    lb2.config(text="Bye")
bb=Button(frame,text='Exit',fg='blue',command=quit )
bb.pack(side=RIGHT)
db=Button(frame,text='Press',fg='blue',command=click)
db.pack(side=LEFT)
lb1=Label(root,text='Hi')
lb1.pack()
lb2=Label(root,text='Hello')
lb2.pack()
root.mainloop()




#Question 4

from tkinter import *

root = Tk()
frame=Frame(root,bg='white')
frame.pack()
Label(frame, text="First Name").grid(row=0)
Label(frame, text="Last Name").grid(row=1)
e1 = Entry(frame)
e2 = Entry(frame)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
def cal():
  a = e1.get()
  b = e2.get()
  c=a + ' ' + b
  lb1 = Label(frame, text=c)
  lb1.grid(row=2, column=1)
  lb1.config(text=a+b)
lb1 = Label(frame,text='')
lb1.grid(row=2, column=1)
db = Button(frame, text='Press', fg='green',width=10, command=cal)
db.grid(row=3,column=1)
bb = Button(frame, text='Exit', fg='green',width=10, command=quit)
bb.grid(row=4,column=1)
mainloop()
