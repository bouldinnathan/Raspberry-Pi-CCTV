#!/usr/bin/env python3

import tkinter
from tkinter import font as tkFont
import os

def quit_():
    osOutput=os.system("sudo shutdown -h now")
    
def restart_():
    osOutput=os.system("sudo reboot")
    
def dev_(root):
    #root.wm_state('iconic')#minimized without a button
    root.destroy()#minimized with a button
def loop(root):
    root.deiconify()
    root.attributes("-zoomed", 1)#this is backup it the resizable(False,False) fails
    root.lower()
    root.update_idletasks()
    root.after(100, func=lambda: loop(root))

root=tkinter.Tk()

helv36 = tkFont.Font(family='Helvetica', size=24, weight='bold')
width = root.winfo_screenwidth()    
root.title("Splash Screen")

info = tkinter.Label(root, text="Please wait while aplication is loading...",font=helv36)
info.grid(row=0, column=0,columnspan=3)
quit_button = tkinter.Button(master=root,width=15, text='Shutdown',font=helv36,command=lambda: quit_())
quit_button.grid(row=8, column=0,columnspan=3, padx=int((width/2)*.6))#gui location
restart_button = tkinter.Button(master=root,width=15, text='Restart',font=helv36,command=lambda: restart_())
restart_button.grid(row=7, column=0,columnspan=3)#gui location
#dev_button = tkinter.Button(master=root,width=15, text='Developer Mode',font=helv36,command=lambda: dev_(root))
#dev_button.grid(row=6, column=0,columnspan=3)#gui location

#root.attributes("-fullscreen",True)
#root.attributes('-topmost', 0)#does not work

root.attributes("-zoomed", 1)
#root.resizable(False, False)

#root.attributes("-zoomed", 1)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
geom_string = "%dx%d+0+0" % (width, height)
root.wm_geometry(geom_string)

#root.overrideredirect(1)#makes boarderless

root.after(100, func=lambda: loop(root))
root.wm_protocol("WM_DELETE_WINDOW",lambda: 1+1)#highjack the x button
root.mainloop()

