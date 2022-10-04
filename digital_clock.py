from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime


def quit(*args):
    root.destroy()

def clock_time():
    time= datetime.datetime.now()
    if "01" == (time.strftime("%m")):
    	month= "January"
    elif "02" == (time.strftime("%m")):
    	month= "February"
    elif "03" == (time.strftime("%m")):
    	month= "March"
    elif "04" == (time.strftime("%m")):
    	month= "April"
    elif "05" == (time.strftime("%m")):
    	month= "May"
    elif "06" == (time.strftime("%m")):
    	month= "June"
    elif "07" == (time.strftime("%m")):
    	month= "July"
    elif "08" == (time.strftime("%m")):
    	month= "August"
    elif "09" == (time.strftime("%m")):
    	month= "September"
    elif "10" == (time.strftime("%m")):
    	month= "October"
    elif "11" == (time.strftime("%m")):
    	month= "November"
    elif "12" == (time.strftime("%m")):
    	month= "December"

    if 12 < (int(time.strftime("%H"))):
    	hour = str((int(time.strftime("%H"))) - 12)
    	ss = "PM"
    else:
    	hour = str(int(time.strftime("%H")))
    	ss = "AM"

    time= (time.strftime("  "+hour+" : %M : %S "+ss+"\n"+month+" %d %Y"))
    timetxt.set(time)
    root.after(1000,clock_time)


root =Tk()
root.configure(bg= "black")
root.bind("x",quit)
root.geometry("400x200")
root.title("Digital Clock")
root.after(1000,clock_time)

fnt = font.Font(family = "Bahnschrift Light",size=30, weight ="bold")
timetxt = StringVar()
lbl = ttk.Label(root,textvariable=timetxt, font = fnt, foreground= "white",background= "black")
lbl.place(relx=0.5,rely=0.5, anchor=CENTER)


root.mainloop()
root.mainloop()