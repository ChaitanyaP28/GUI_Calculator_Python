#Simple Calculator
from tkinter import *
root=Tk()
root.title("Simple Calculator")

e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def clear():
    e.delete(0,END)

def add():
    f_n=e.get()
    global f_num
    global oper
    oper="add"
    f_num=int(f_n)
    e.delete(0,END)

def sub():
    f_n=e.get()
    global f_num
    global oper
    oper="Sub"
    f_num=int(f_n)
    e.delete(0,END)

def multi():
    f_n=e.get()
    global f_num
    global oper
    oper="multi"
    f_num=int(f_n)
    e.delete(0,END)

def div():
    f_n=e.get()
    global f_num
    global oper
    oper="div"
    f_num=int(f_n)
    e.delete(0,END)

def equl():
    s_sum=int(e.get())
    e.delete(0,END)
    if oper=="add":
        e.insert(0,f_num+s_sum)
    elif oper=="sub":
        e.insert(0,f_num-s_sum)
    elif oper=="multi":
        e.insert(0,f_num*s_sum)
    elif oper=="div":
        e.insert(0,f_num/s_sum)
        
#Button
btn1=Button(root,text="1",padx=40,pady=20,command=lambda:click(1))
btn2=Button(root,text="2",padx=40,pady=20,command=lambda:click(2))
btn3=Button(root,text="3",padx=40,pady=20,command=lambda:click(3))
btn4=Button(root,text="4",padx=40,pady=20,command=lambda:click(4))
btn5=Button(root,text="5",padx=40,pady=20,command=lambda:click(5))
btn6=Button(root,text="6",padx=40,pady=20,command=lambda:click(6))
btn7=Button(root,text="7",padx=40,pady=20,command=lambda:click(7))
btn8=Button(root,text="8",padx=40,pady=20,command=lambda:click(8))
btn9=Button(root,text="9",padx=40,pady=20,command=lambda:click(9))
btn0=Button(root,text="0",padx=40,pady=20,command=lambda:click(0))

btnadd=Button(root,text="+",padx=39,pady=20,command=add)
btnsub=Button(root,text="-",padx=41,pady=20,command=sub)
btnmult=Button(root,text="*",padx=40,pady=20,command=multi)
btndiv=Button(root,text="/",padx=41,pady=20,command=div)

btnequl=Button(root,text="=",padx=90,pady=20,command=equl)
btnclear=Button(root,text="Clear",padx=79,pady=20,command=clear)

btn1.grid(row=3,column=0)
btn2.grid(row=3,column=1)
btn3.grid(row=3,column=2)
btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)
btn7.grid(row=1,column=0)
btn8.grid(row=1,column=1)
btn9.grid(row=1,column=2)
btn0.grid(row=4,column=0)

btnadd.grid(row=5,column=0)
btnsub.grid(row=6,column=0)
btnmult.grid(row=6,column=1)
btndiv.grid(row=6,column=2)
btnequl.grid(row=5,column=1,columnspan=2)
btnclear.grid(row=4,column=1,columnspan=2)


root.mainloop()
