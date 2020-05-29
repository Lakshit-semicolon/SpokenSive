from tkinter import *
from speak import *
from speech import *
import os
from PIL import Image

root = Tk()
# Icon
root.wm_iconbitmap('c:/Users/asus/Desktop/lakshit/Python programs/Hand/notepad.ico')
# Width  x  Height
root.geometry("644x800")

# Fix window size
root.minsize(479,180)
root.maxsize(479,180)

# Title
root.title("SpokenCiv - your cursive partner")

#func
def createe(text):
    try:
        
        # print('Text: ' + text)
        os.system('python C:/Users/asus/Desktop/speechsy-master/get_hand.py -t "' + text + '" -s 4 -c 0,0,200' )
        img = Image.open('images/0.png')
        img.show()
    except:
        pass

# Display 
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold") 
screen.pack(fill=X)
             

# Function
def click(event):
    global scvalue
    text = event.widget.cget("text")
    
    if text == "voice":
        text=rect() 
        female("You can see the value on the screen      "+ text)
        scvalue.set(scvalue.get() + text)
        screen.update()
    elif text == "All Clear":
        scvalue.set("")
        screen.update()
        female("I have cleared the screen")
    elif text == "OFF":
        female("Bye Bye , hope to meet you soon")
        sys.exit()
    elif text == "Output":
        female("It is getting converted and will show on your screen in a while.")
        createe(scvalue.get())
        pass
    elif text == "DEL": #scvalue=text
         try:
            fullstring = scvalue.get()
            newstring=fullstring[:-1]
            # we are replacing the last string item[-1] with blank or ""
            # String slicing method
            
            scvalue.set(newstring)

            # print(newstring)
            screen.update()
            female("Done")
         except Exception as e:
            print(e) 
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()




# Frame
mFrame = Frame(root)
mFrame.pack(side=TOP, fill=X)


vframe=Frame(mFrame,relief=GROOVE)
vframe.pack(side=TOP)
b=Button(vframe,text="voice",width=20,height=3)
b.grid(row=0,column=0)
b.bind("<Button-1>",click)
b=Button(vframe,text="All Clear",width=20,height=3)
b.grid(row=0,column=1)
b.bind("<Button-1>",click)
b=Button(vframe,text="OFF",width=20,height=3)
b.grid(row=0,column=2,padx=1)
b.bind("<Button-1>",click)

topFrame = Frame(root)
topFrame.pack(side=TOP, fill=X)
cframe=Frame(topFrame,relief=GROOVE)
cframe.pack(side=LEFT,padx=80)
b=Button(cframe,text="Output",width=20,height=3)
b.pack()
b.bind("<Button-1>",click)

opframe=Frame(topFrame,relief=GROOVE)
opframe.pack(side=TOP,fill=X,padx=4)
b=Button(opframe,text="DEL",width=20,height=3)
b.grid(row=0,column=0)
b.bind("<Button-1>",click)


root.mainloop()