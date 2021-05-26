from tkinter import *
import random
from tkinter import messagebox as msg

a = random.randrange(1, 10)
b = random.randrange(1, 10)
o = random.choice('+-')

def compute():
    global two
    result = two.get()
    tmp = int(result)
    o_tmp = 0
    if(o=='+'):
        o_tmp=a+b
    else:
        if(a>=b):
            o_tmp=a-b
        else:
            o_tmp=b-a
    if(tmp==o_tmp):
        msg.showinfo('결과', 'You got it!!')
    else:
        msg.showinfo('결과', 'Wrong!!')

top=Tk()
top.title("Ed")

c = ""
if(a>=b):
    c = str(a)+o+str(b)
else:
    c=str(b)+o+str(a)

lb1 = Label(top, text="문제 : ")
lb1.grid(row=0, column=0)
one = Entry(top)
one.insert(0, c)
one.grid(row=0, column=1)

lb2 = Label(top, text="정답 : ")
lb2.grid(row=1, column=0)
two = Entry(top)
two.grid(row=1, column=1) 

button = Button(top, text='Enter', command=compute)
button.grid(row=2, column=0, columnspan=2)

top.mainloop()
