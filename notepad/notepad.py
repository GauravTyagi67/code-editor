from tkinter import*
import os
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter.messagebox import showinfo#error,information,messageshow

def quitApp():#Exit window
    root.destroy()
    
def cut():#cut
    TA.event_generate(("<<Cut>>"))
    
def copy():#copy
    TA.event_generate(("<<Copy>>"))
    
def paste():#Paste
    TA.event_generate(("<<Paste>>"))

def about():#about is a show information window
    showinfo("Notepad","Notepad Created By Gaurav Tyagi")
    
def Newfile():
    global file
    root.title("Untitled-Notepad")
    file=None
    TA.delete(1.0,END)#1 is row and 0 is column work,End is work last
    
def openfile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        TA.delete(1.0,END)
        f=open(file,"r")
        TA.insert(1.0,f.read())
        f.close()
        
def savefile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",
                               filetypes=[("All Files","*.*"),
                                          ("Text Document",".txt")])
        if file=="":
            file=None   
        else:
            #save as a new file
            f=open(file,"w")
            f.write(TA.get(1.0,END))
            f.close()
            
            root.title(os.path.basename(file)+"-Notepad")
            print("File Saved")
            
    else:
        #save the file name
        f=open(file,"w")
        f.write(TA.get(1.0,END))
        f.close()
            
    
    

root=Tk()
root.geometry("500x500")
root.title("Notepad")
root.iconbitmap("notepad.ico")
TA=Text(root,font=("Arial",15))
TA.pack(expand=True,fill=BOTH)
file=None

mainmenu=Menu(root)
m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="New",command=Newfile)
m1.add_command(label="Open",command=openfile)
m1.add_command(label="Save",command=savefile)
m1.add_separator()
m1.add_command(label="Exit",command=quitApp)
mainmenu.add_cascade(label="File",menu=m1)

m2=Menu(mainmenu)
m2=Menu(mainmenu,tearoff=0)
m2.add_command(label="Cut",command=cut)
m2.add_command(label="Copy",command=copy)
m2.add_command(label="Paste",command=paste)
mainmenu.add_cascade(label="Edit",menu=m2)

m3=Menu(mainmenu)
m3=Menu(mainmenu,tearoff=0)
m3.add_command(label="About Notepad",command=about)
mainmenu.add_cascade(label="Help",menu=m3)

s=Scrollbar(TA)
s.pack(side=RIGHT,fill=Y)
s.config(command=TA.yview)
TA.config(yscrollcommand=s.set)

root.config(menu=mainmenu)
root.mainloop()
