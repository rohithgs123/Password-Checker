from password_strength import PasswordStats
import tkinter as tk
import math
from tkinter import messagebox
window=tk.Tk()
window.title("Password Checker")
window.geometry("800x800")
label2=tk.Label(window,text="")
label2.place(x=200,y=275)
def checkFunc():
    if enterInfo.get()=="":
        messagebox.showinfo("Error Field must be filled in")
    else:
        result=PasswordStats(enterInfo.get())
        final=result.strength()
        label2["text"]=str(math.ceil(final*100)) + " %"
        if final >= 0.66:
            w.create_rectangle(105,50,300,100,fill="#27cf54",outline="white")
        elif final > 0.10 and final < 0.40:
            w.create_rectangle(105,50,300,100,fill="#f0f007",outline="white")
        elif final <= 0.10:
            w.create_rectangle(105,50,300,100,fill="#de3c3c",outline="white")
            
heading=tk.Label(window,text="Password Checker",font=("helvetica",15,"bold"))
heading.pack(ipadx=12,ipady=12)
labelText=tk.Label(window,text="Enter You Password",font=("helvetica",15,"bold"))
labelText.pack(ipadx=5,ipady=5)
enterInfo=tk.Entry(window)
enterInfo.pack(ipadx=30,ipady=5)
buttonType=tk.Button(window,text="Submit",command=checkFunc)
buttonType.pack(ipadx=5,ipady=5)
w=tk.Canvas(window,height=100,width=600)
w.pack()



