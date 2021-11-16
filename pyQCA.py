import tkinter as tk
import necessaryconditions
import os
import time
import truthtable
import parsimonioussolution
import intermediatesolution
import complexsolution
import mvnecessaryconditions
import mvtruthtable
import mvparsmonioussolution
import mvintermediatesolution
import mvcomplexsolution
def necess():
    necessaryconditions.check()
def truthab():
    truthtable.truthtable()
    print("generate truthable successfully")
def parsmoniou():
    print("the parsimonioussolution is as followed:")
    parsimonioussolution.parsimonious()
def intermedia():
    print("the intermediatesolution is as followed:")
    intermediatesolution.intermediate()
def comple():
    print("the complexsolution is as followed:")
    complexsolution.complex()
def mvnece():
    mvnecessaryconditions.nece()
def mvtruth():
    print("generate mvtruthable successfully")
    mvtruthtable.truthtable()
def mvparsmoniou():
    print("the mvparsimonioussolution is as followed:")
    mvparsmonioussolution.mvparsmonious()
def mvintermedia():
    print("the mvintermediatesolution is as followed:")
    mvintermediatesolution.mvintermediate()
def mvcomple():
    print("the mvcomplexsolution is as followed:")
    mvcomplexsolution.mvcomplex()
class APP:
    def __init__(self, master):
        root.title("pyQCA1.0")
        frame = tk.Frame(master)
        frame.pack()
        self.hi_there = tk.Button(frame, text='necessaryconditions', bg='white', fg='black',font=('微软雅黑',10),height=1,width=28,command=necess)
        self.hi_there.pack()
        frame.pack()
        self.hi_there = tk.Button(frame, text='truthable', bg='white', fg='black', font=('微软雅黑', 10),height=1,width=28,command=truthab)
        self.hi_there.pack()
        frame.pack()
        self.hi_there = tk.Button(frame, text='parsimonioussolution', bg='white', fg='black', font=('微软雅黑', 10),height=1,width=28,command=parsmoniou)
        self.hi_there.pack()
        frame.pack()
        self.hi_there = tk.Button(frame, text='intermediatesolution', bg='white', fg='black', font=('微软雅黑', 10),height=1,width=28,command=intermedia)
        self.hi_there.pack()
        frame.pack()
        self.hi_there = tk.Button(frame, text='complexsolution', bg='white', fg='black', font=('微软雅黑', 10),height=1,width=28,command=comple)
        self.hi_there.pack()
        frame.pack()
        self.hi_there = tk.Button(frame, text='mvnecessaryconditions', bg='lightgrey', fg='black', font=('微软雅黑', 10),height=1,width=28,command=mvnece)
        self.hi_there.pack()
        frame.pack()
        self.hi_there = tk.Button(frame, text='mvtruthable', bg='lightgrey', fg='black', font=('微软雅黑', 10),height=1,width=28,command=mvtruth)
        self.hi_there.pack()
        frame.pack()
        self.hi_there = tk.Button(frame, text='mvparsmonioussolution', bg='lightgrey', fg='black', font=('微软雅黑', 10),height=1,width=28,command=mvparsmoniou)
        self.hi_there.pack()
        frame.pack()
        self.hi_there = tk.Button(frame, text='mvintermediatesolution', bg='lightgrey', fg='black', font=('微软雅黑', 10),height=1,width=28,command=mvintermedia)
        self.hi_there.pack()
        frame.pack()
        self.hi_there = tk.Button(frame, text='mvcomplexsolution', bg='lightgrey', fg='black', font=('微软雅黑', 10),height=1,width=28,command=mvcomple)
        self.hi_there.pack()
root = tk.Tk()
root.wm_geometry('320x350+1000+100')
root.wm_resizable(False,False)
app = APP(root)
root.mainloop()





