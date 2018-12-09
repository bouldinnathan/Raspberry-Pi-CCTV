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


root=tkinter.Tk()

helv36 = tkFont.Font(family='Helvetica', size=24, weight='bold')
helv12 = tkFont.Font(family='Helvetica', size=12, weight='bold')
width = root.winfo_screenwidth()    
root.title("About Screen")

about='''
This projected was made in collaboration between
UAB Project lab and Adult Vocational Rehab Services
Application Programmer:
Nathan Bouldin
Mentors:
Michael Papp, M.Sc.Eng., C.P.M.,
Dr. Timothy Wick
Desland Robinson'''


info = tkinter.Label(root, text=about,font=helv36)
info.grid(row=0, column=0,columnspan=3)

root.after(10000, func=lambda: root.destroy())
root.mainloop()

