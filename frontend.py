#Frontend

from tkinter import *
import tkinter.messagebox
from backend import *

root=Tk()
root.title("Lexical Analyzer")
root.geometry("1350x750+0+0")
root.config(bg="black")   

Input=StringVar()
txtInput=StringVar()
  
#Fuctions
def iExit():
        iExit=tkinter.messagebox.askyesno("Lexical Analyzer", "Are you sure???")
        if iExit>0:
                root.destroy()
        return

def clcdata():
        txtInput.delete(0,END)

def adddata():
        inp = txtInput.get()
        ans=parsefn(inp)
        lbl.config(text = "Result : "+ans)

#Frames
MainFrame=Frame(root, bg="black")
MainFrame.grid()

TFrame=Frame(MainFrame, bd=5, padx=54, pady=8, bg="black", relief=RIDGE)
TFrame.pack(side=TOP)

TFrame=Label(TFrame, font=('Arial', 51, 'bold'), text="Lexical Analyzer", bg="black", fg="orange")
TFrame.grid() 

BFrame=Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="black", relief=RIDGE)
BFrame.pack(side=BOTTOM)

DFrame=Frame(MainFrame, bd=2, width=1300, height=400, padx=20, pady=20, bg="black", relief=RIDGE)
DFrame.pack(side=BOTTOM)

DFrameL=LabelFrame(DFrame, bd=2, width=1000, height=600, padx=20, bg="black", relief=RIDGE, font=('Arial', 20, 'bold'), text="Input Info\n", fg="white")
DFrameL.pack(side=LEFT)

DFrameR=LabelFrame(DFrame, bd=2, width=450, height=300, padx=31, pady=3, bg="black", relief=RIDGE, font=('Arial', 20, 'bold'), text="Output\n", fg="white")
DFrameR.pack(side=RIGHT)

#Labels & Entry Box
lblInput=Label(DFrameL, font=('Arial', 18, 'bold'), text="Your Info :", padx=2, pady=2, bg="black", fg="orange")
lblInput.grid(row=0, column=0, sticky=W)
txtInput=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Input, width=39, bg="black", fg="white")
txtInput.grid(row=0, column=1)

#output label
lbl = Label(DFrameR, text = "")
lbl.pack()

#Buttons
btnadd=Button(BFrame, text="Evaluate", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=adddata)
btnadd.grid(row=0, column=0)
btnadd.pack()

if __name__=='__main__':
	root=Tk()
	root.mainloop()
