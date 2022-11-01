from tkinter import *

root=Tk()
root.title("Simple Calculator")
root.geometry("570x450")
root.resizable(False,False)
root.configure(bg="#17161b")

eq=""

def show(value):
  global eq
  eq=eq+value
  l_result.config(text=eq)

def clear():
  global eq
  eq=" "
  l_result.config(text=eq)


def cal():
    global eq
    result=""
    if(eq!=""):
        try:
            result=eval(eq)
        except:
            result="error"
            eq=""
    l_result.config(text=result)

l_result=Label(root,width=24,height=2,text="",font=("chalkboard",30))
l_result.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

Button(root,text="C",width=5,height=1,font=("chalkboard",30,"bold"),fg="#fff",bg="#3697f5",command=lambda:clear()).place(x=10,y=110)
Button(root,text="/", width=5, height=1,font=("chalkboard",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda:show("/")).place(x=150,y=110)
Button(root,text="%", width=5, height=1,font=("chalkboard",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda:show("%")).place(x=290,y=110)
Button(root,text="", width=5, height=1,font=("chalkboard",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda:show("")).place(x=430,y=110)

Button(root,text="7", width=5, height=1,font=("chalkboard",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda:show("7")).place(x=10,y=170)
Button(root,text="8", width=5, height=1,font=("chalkboard",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda:show("8")).place(x=150,y=170)
Button(root,text="9", width=5, height=1,font=("chalkboard",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda:show("9")).place(x=290,y=170)
Button(root,text="-", width=5, height=1,font=("chalkboard",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda:show("-")).place(x=430,y=170)

Button(root,text="4", width=5, height=1,font=("chalkboard",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda:show("4")).place(x=10,y=230)
Button(root,text="5", width=5, height=1,font=("chalkboard",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda:show("5")).place(x=150,y=230)
Button(root,text="6", width=5, height=1,font=("chalkboard",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda:show("6")).place(x=290,y=230)
Button(root,text="+", width=5, height=1,font=("chalkboard",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda:show("+")).place(x=430,y=230)

Button(root,text="1", width=5, height=1,font=("chalkboard",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda:show("1")).place(x=10,y=290)
Button(root,text="2", width=5, height=1,font=("chalkboard",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda:show("2")).place(x=150,y=290)
Button(root,text="3", width=5, height=1,font=("chalkboard",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda:show("3")).place(x=290,y=290)

Button(root,text="0", width=12, height=1,font=("chalkboard",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda:show("0")).place(x=10,y=350)
Button(root,text=".", width=5, height=1,font=("chalkboard",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda:show(".")).place(x=290,y=350)
Button(root,text="=", width=5, height=2,font=("chalkboard",30,"bold"),fg="#fff",bg="#fe9037",command=lambda:cal()).place(x=430,y=300)

root.mainloop()
