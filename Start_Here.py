#!/usr/bin/env python3
#Title: Bug EYE 1.0
#Version 1.0.0
#Created By: Nathan Ray Bouldin
#Copyright (c) 2018, Nathan Ray Bouldin

#>>>>>>>>>>>>>>>>>>>>Read Me<<<<<<<<<<<<<<<<<<<<<<
#If you mistakenly opened this click the "x" in the
#top right corner and do not save any changes. 
#>>>>>>>>>>>>>>>>>>>>Read Me<<<<<<<<<<<<<<<<<<<<<<<<

#Thank you to Abid Rahman K for his answer at https://stackoverflow.com/questions/11433604/opencv-setting-all-pixels-of-specific-bgr-value-to-another-bgr-value
#The code was used and modified at 264,265,269, and 275, licenses at https://creativecommons.org/licenses/by-sa/3.0/

#The Python Imaging Library (PIL) is
#    Copyright © 1997-2011 by Secret Labs AB
#    Copyright © 1995-2011 by Fredrik Lundh
#Pillow is the friendly PIL fork. It is
#    Copyright © 2010-2018 by Alex Clark and contributors
#Like PIL, Pillow is licensed under the open source PIL Software License:
#By obtaining, using, and/or copying this software and/or its associated documentation, you agree that you have read, understood, and will comply with the following terms and conditions:
#Permission to use, copy, modify, and distribute this software and its associated documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appears in all copies, and that both that copyright notice and this permission notice appear in supporting documentation, and that the name of Secret Labs AB or the author not be used in advertising or publicity pertaining to distribution of the software without specific, written prior permission.
#SECRET LABS AB AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL SECRET LABS AB OR THE AUTHOR BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

#Copyright (c) 2005, NumPy Developers
#All rights reserved.
#Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
#Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
#Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
#Neither the name of the NumPy Developers nor the names of any contributors may be used to endorse or promote products derived from this software without specific prior written permission.
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


#“For libray cv2 Copyright (c) 2018, Open Source Computer Vision Library.  All rights reserved.
#
#This software is provided by the copyright holders and contributors “as is” and any express or
#implied warranties, including, but not limited to, the implied warranties of merchantability and 
#fitness for a particular purpose are disclaimed. In no event shall copyright holders or contributors
# be liable for any direct, indirect, incidental, special, exemplary, or consequential damages 
#(including, but not limited to, procurement of substitute goods or services; loss of use, data, or
# profits; or business interruption) however caused and on any theory of liability, whether in contract,
# strict liability, or tort (including negligence or otherwise) arising in any way out of the use of this 
#software, even if advised of the possibility of such damage. This software is provided by the copyright
# holders and contributors “as is” and any express or implied warranties, including, but not limited to,
# the implied warranties of merchantability and fitness for a particular purpose are disclaimed. In no 
#event shall copyright holders or contributors be liable for any direct, indirect, incidental, special,
# exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or
# services; loss of use, data, or profits; or business interruption) however caused and on any theory of
# liability, whether in contract, strict liability, or tort (including negligence or otherwise) arising 
#in any way out of the use of this software, even if advised of the possibility of such damage.  Neither
# the copyright holders nor the contributors endorse or promote this product.”



#the "#!/usr/bin/python3" is a shebang do not delete
#change fps for new speed
#original speed 10 fps
#cv2.imshow("camera",img1)#there is no buffer that has to be filled up
#all prints must go!!!!!!!!!!!!!!!!!!
import tkinter as Tkinter
import tkinter
from tkinter import font as tkFont
import PIL
from PIL import Image
#from PIL import ImageTk
import cv2
import threading
import numpy
from multiprocessing import Pipe
import os
import gc #garbage collector
from time import time
from time import sleep
import sys
import subprocess
from math import floor

##python 2.7
#import Tkinter
#import tkFont
#import PIL
#from PIL import Image
#from PIL import ImageTk
#import cv2
#import threading
#import numpy
#from multiprocessing import Pipe
#import os
#import gc #garbage collector
#from time import time
#import sys

#/////lock file (there can only be one)\\\\\\\\
location='/home/pi/lock.txt'
working_dirctory=''
read_data=0
try:
    f=open(location,'r')
    read_data = f.read(1)
    f.close()
    print('read lock file: '+str(read_data))
except IOError:
    g=open(location,'w')
    g.write('1')
    g.close()
    print('made lock file')
if(read_data):
    exit()
#/////lock file (there can only be one)\\\\\\\\

def quit_(cam,root):
    osOutput = subprocess.getoutput(["sudo rm "+location])#this allows the program to be started back up
    osOutput=os.system("sudo shutdown -h now")
    print ('error '+str(osOutput))
    print ("Quiting")
    cv2.destroyAllWindows()
    cam.release()
    print("Camera Released")
    root.destroy()
    print("Main Window Closed")
    #cameraControl.destroy()
    #print("Secondary Window Closed")
    #osOutput = subprocess.getoutput(["sudo rm "+location])#this allows the program to be started back up
    #osOutput=os.system("sudo rm "+location)#this allows the program to be started back up
    sleep(2)
    cv2.waitKey(1)
    cv2.waitKey(1)
    cv2.waitKey(1)
    cv2.waitKey(1)
    #sys.exit()
    # osOutput=os.system("sudo shutdown -h now")
    print(osOutput)
    print("shutdown computer")
    sleep(2)
    quit()
def vSave():
    global needToSave
    needToSave=1
def original():
    global blackWhite
    global whiteBlack
    global yellowBlue
    global blackYellow
    global yellowBlack
    global isChanged
    blackWhite=False
    whiteBlack=False
    yellowBlue=False
    blackYellow=False
    yellowBlack=False
def blackWhiteF():
    global blackWhite
    global whiteBlack
    global yellowBlue
    global blackYellow
    global yellowBlack
    
    blackWhite=True
    whiteBlack=False
    yellowBlue=False
    blackYellow=False
    yellowBlack=False
def whiteBlackF():
    global blackWhite
    global whiteBlack
    global yellowBlue
    global blackYellow
    global yellowBlack
    
    blackWhite=False
    whiteBlack=True
    yellowBlue=False
    blackYellow=False
    yellowBlack=False
def yellowBlueF():
    global blackWhite
    global whiteBlack
    global yellowBlue
    global blackYellow
    global yellowBlack
    blackWhite=False
    whiteBlack=False
    yellowBlue=True
    blackYellow=False
    yellowBlack=False
def yellowBlackF():
    global blackWhite
    global whiteBlack
    global yellowBlue
    global blackYellow
    global yellowBlack
    blackWhite=False
    whiteBlack=False
    yellowBlue=False
    blackYellow=False
    yellowBlack=True
def blackYellowF():
    global blackWhite
    global whiteBlack
    global yellowBlue
    global blackYellow
    global yellowBlack
    blackWhite=False
    whiteBlack=False
    yellowBlue=False
    blackYellow=True
    yellowBlack=False
def pauseFocusF():
    global autofocus
    print('Autofocus: '+str(autofocus))
    if autofocus:
        os.system('v4l2-ctl -d 0 -c focus_auto='+str(int(autofocus)))
        autofocus=0
    else:
        os.system('v4l2-ctl -d 0 -c focus_auto='+str(int(autofocus)))
        autofocus=1
def plusFocusF():
    global varFocus
    global autofocus
    varFocus=varFocus+5
    if varFocus >255:
        varFocus=255
    os.system('v4l2-ctl -d 0 -c focus_auto='+str(0))
    os.system('v4l2-ctl -d 0 -c focus_absolute='+str(varFocus))#side effect: it turns autofocus off
    autofocus=0#the next time Pause focus is clicked it will unpuase
def minusFocusF():
    global varFocus
    global autofocus
    varFocus=varFocus-5
    if varFocus <0:
        varFocus=0
    os.system('v4l2-ctl -d 0 -c focus_auto='+str(0))
    os.system('v4l2-ctl -d 0 -c focus_absolute='+str(varFocus))#side effect: it turns autofocus off
    autofocus=0#the next time Pause focus is clicked it will unpuase

def slideFocusF(var):
    global varFocus
    global autofocus
    
    varFocus=var
    os.system('v4l2-ctl -d 0 -c focus_auto='+str(0))
    os.system('v4l2-ctl -d 0 -c focus_absolute='+str(varFocus))#side effect: it turns autofocus off
    autofocus=0#the next time Pause focus is clicked it will unpuase
    

def cleanImg(img0,img1):
    averageImg=(numpy.float32(img0)+numpy.float32(img1))/2
    averageImg=cv2.cvtColor(averageImg,cv2.COLOR_BGR2RGB);
    return numpy.uint8(averageImg)

def changeImg(img1):
    global blackWhite
    global whiteBlack
    global yellowBlue
    global blackYellow
    global yellowBlack
    global isChanged
    if blackWhite or whiteBlack or yellowBlue or blackYellow or yellowBlack:
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        isChanged=1
    if blackWhite:
        ret,img1 = cv2.threshold(img1,127,255,cv2.THRESH_BINARY)## slider on the 127(half way piont) now 100
    elif whiteBlack:
        ret,img1 = cv2.threshold(img1,127,255,cv2.THRESH_BINARY_INV)## slider on the 127(half way piont) now 100
    elif yellowBlue:
        ret,img1 = cv2.threshold(img1,127,255,cv2.THRESH_BINARY)## slider on the 127(half way piont) now 100
        img1=cv2.cvtColor(img1,cv2.COLOR_GRAY2RGB);#this one works for some reason?!?
        img1[numpy.where((img1==[0,0,0]).all(axis=2))] = [0,255,255]
        img1[numpy.where((img1==[255,255,255]).all(axis=2))] = [255,0,0]
    elif yellowBlack:
        ret,img1 = cv2.threshold(img1,127,255,cv2.THRESH_BINARY);## slider on the 127(half way piont) now 100
        img1=cv2.cvtColor(img1,cv2.COLOR_GRAY2BGR);
        img1[numpy.where((img1==[255,255,255]).all(axis=2))] = [0,255,255];
        #sleep(.02)#idk cv2.cvtColor just will not work with out this commented out line and if it stop working uncomment and run
    
    elif blackYellow:
        ret,img1 = cv2.threshold(img1,127,255,cv2.THRESH_BINARY_INV);## slider on the 127(half way piont) now 100
        img1=cv2.cvtColor(img1,cv2.COLOR_GRAY2BGR);
        img1[numpy.where((img1==[255,255,255]).all(axis=2))] = [0,255,255];
        #print "black and yellow" #idk cv2.cvtColor just will not work with out this commented out line and if it stop working uncomment and run
    return img1


def save(cam):
    cam.release()
    
    CV_CAP_PROP_FRAME_WIDTH=3
    CV_CAP_PROP_FRAME_HEIGHT=4
    width=5168
    height=2907

    cam=cv2.VideoCapture(0)
    cam.set(CV_CAP_PROP_FRAME_WIDTH,width)
    cam.set(CV_CAP_PROP_FRAME_HEIGHT,height)
    _, img0=cam.read()
    _, img1=cam.read()
    img0 = cv2.cvtColor(img0, cv2.COLOR_BGR2RGB)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    averageImg=cleanImg(img0,img1)
    #averageImg=cv2.cvtColor(averageImg,cv2.COLOR_BGR2RGB);
    img1=changeImg(averageImg)
    #img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB);#########error grey cant be converted from bgr to rgb
    cv2.imwrite('/home/pi/currentPic.png', img1)####change name to time stamp#######
    cam.release()
    #<<<<<<<<<<<<<<used to resetup cam not needed now>>>>>>>>>>>>>>>>>
    #width=1280###############hard code resolution
    #height=720###############hard code resolution
    #cv2.setUseOptimized(1)
    #cam=cv2.VideoCapture(0)
    #cam.set(CV_CAP_PROP_FRAME_WIDTH,width)
    #cam.set(CV_CAP_PROP_FRAME_HEIGHT,height)
    #return cam
    #<<<<<<<<<<<<<<used to resetup cam not needed now>>>>>>>>>>>>>>>>>


def daemon(cam,child_conn):
    totalTime=time()#############testing
    #img0=[]
    img1=[]
    #img2=[]
    #_,_=cam.read()###############stop ghosting
    #_,_=cam.read()
    #_,_=cam.read()
    _, img1=cam.read()
    #img1 = cv2.resize(img1, (1920, 1080)) #(1920, 1080),interpolation = cv2.INTER_NEAREST)
    #img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB);# idk i just look like a smurf and I fixed it
    img1=changeImg(img1)
    #img1 = Image.fromarray(img1) ####change color and it breaks
    try:
        child_conn.send(img1)
    except IOError as e:
        child_conn.close()
        print("Broken Pipe")
    totalTime=time()-totalTime##################testing
    print ("Total Thread Time "+str(totalTime))##########testing
    
    
def loop(cam,d,parent_conn):
    totalTime=time()#############testing
    global needToSave
    
    
    #d.join################testing
    #img1=queue.get()############testing
    #d=None################# testing
    
    if d is not None:
        
        img1=parent_conn.recv()
        parent_conn.close()
        d.join()
        
        parent_conn, child_conn = Pipe()
        
        if needToSave:#there can only be one thread polling the cam at a time :_(
            print ("Saving")
            save(cam);
            print ("Finished Saving")
            needToSave=0
            #os.system('python3 CorrectVeiw.py')
            #<<<<<<<<>>>>>>>>>>>
            print("Changing in 2")
            cv2.destroyAllWindows()
            root.destroy()
            print("Changing in 2")
            #cameraControl.destroy()
            cv2.waitKey(1)
            cv2.waitKey(1)
            cv2.waitKey(1)
            cv2.waitKey(1)
            #sys.exit()
            print("Changing")
            osOutput = subprocess.getoutput(["sudo rm "+location])#this allows the program to be started back up
            os.system('python3 '+working_dirctory+'CorrectVeiw.py')
            quit()
            #<<<<<<<<>>>>>>>>>>>
        
        d = threading.Thread(name='daemon', target=daemon,args=(cam,child_conn))
        d.setDaemon(True)
        d.start()
        
    else:#this can be removed
        print ("here")
        d = threading.Thread(name='daemon', target=daemon,args=(cam,queue))
        d.setDaemon(True)
        
        d.start()
        print ("thread d=None")
        d.join()
        d = threading.Thread(name='daemon', target=daemon,args=(cam,queue))
        d.setDaemon(True)
        d.start()
    

    
    
    #img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB);# idk i just look like a smurf and I fixed it

    #img1 = Image.fromarray(img1)  #############################################  
    #img1 = ImageTk.PhotoImage(img1)
    #panel.configure(image=img1)

    # this is al most working rotation££££££££££££££££££££££££££££££££££££££££  
    #y,x=img1.shape[:2]
    #center=(floor(y/2),floor(x/2))
    #temp=cv2.getRotationMatrix2D(center,270,1)
    #img1=cv2.warpAffine(img1,temp,(y,x))
        
    #cv2.imshow("camera",img1)#there is no buffer that has to be filled up
    cv2.imshow("Preview",img1)#opencv is coded in C and is wrapped in python so is will show the image with less than a Sec or more delay.
    cv2.waitKey(1)#A 1ms delay is DEMANDED by Savitar the God of Speen for cv2.imshow to bless us with sub Sec latency. Praise Him. But no really this has to be in the loop.  
    
    
    root.update_idletasks()#this over "root.update()" saved .3 sec. Also the Gui will not even show up cause this updates the whole Gui
    root.after(0, func=lambda: loop(cam,d,parent_conn))
   
    totalTime=time()-totalTime##################testing
    print ("Total Time "+str(totalTime))##########testing
    
def lifterLoop(root):
    root.lift()
    root.focus_force()
    root.after(50, func=lambda: lifterLoop(root))
    
def popup_showinfo():
    #helv36 = tkFont.Font(family='Helvetica', size=24, weight='bold')
    #def killThisWindow(popUpAbout):
    #    print(popUpAbout)
    #    popUpAbout.destroy()
    #    popUpAbout=tkinter.Toplevel(root)
    #    popUpAbout.wm_title('About this application')
    #    label1=tkinter.Label(popUpAbout, text='hi', font=helv36)
    #    label1.grid(row=0, column=0,columnspan=1)
    #    okPopButton = tkinter.Button(popUpAbout,width=10, text='OK',font=helv36,command=lambda: killThisWindow(popUpAbout))
    #    okPopButton.grid(row=1, column=0,columnspan=1)
    #    popUpAbout.mainloop()
    os.system('python3 '+working_dirctory+'about.py')
    

    
if __name__ == '__main__':
    CV_CAP_PROP_FRAME_WIDTH=3
    CV_CAP_PROP_FRAME_HEIGHT=4
    CV_CAP_PROP_FPS=5
    #width=240
    #height=200
    #width=480
    #height=400
    width=1280###############hard code resolution
    height=720##############hard code resolution
    #width=1920
    #height=1080
    #width=5168
    #height=2907
    parent_conn, child_conn = Pipe()
    needToSave=False
    blackWhite=False
    whiteBlack=False
    yellowBlue=False
    blackYellow=False
    yellowBlack=False
    autofocus=True
    varFocus=10

    cv2.setUseOptimized(1)
    cam=cv2.VideoCapture(0)
    
    cam.set(CV_CAP_PROP_FRAME_WIDTH,width)
    cam.set(CV_CAP_PROP_FRAME_HEIGHT,height)
    if height >=1080:
        fps=5#was 3
        cam.set(CV_CAP_PROP_FPS,fps); #have to set the FPS otherwise the internal buffer of the webcam will give old frames
    elif height==720:
        fps=5#was 9
        cam.set(CV_CAP_PROP_FPS,fps);
    
    d = threading.Thread(name='daemon', target=daemon,args=(cam,child_conn))
    d.setDaemon(True)
    d.start()

    root=Tkinter.Tk()

    helv36 = tkFont.Font(family='Helvetica', size=24, weight='bold')
    
    quit_button = Tkinter.Button(master=root,width=10, text='Quit',font=helv36,command=lambda: quit_(cam,root))
    quit_button.grid(row=15, column=0,columnspan=3)#gui location
    saveButton = Tkinter.Button(master=root,width=10, text='Magnify',font=helv36,command=lambda: vSave())
    saveButton.grid(row=7, column=0,columnspan=3)#gui location
    aboutButton = Tkinter.Button(master=root,width=10, text='About',font=helv36,command=lambda: popup_showinfo())
    aboutButton.grid(row=14, column=0,columnspan=3)#gui location

    

    
    blackWhiteButton = Tkinter.Button(master=root,width=10, text='Black',fg='Black',bg='white',font=helv36,command=lambda: blackWhiteF())
    blackWhiteButton.grid(row=1, column=0,columnspan=1)
    whiteBlackButton = Tkinter.Button(master=root,width=10, text='White',fg='white',bg='black',font=helv36,command=lambda: whiteBlackF())
    whiteBlackButton.grid(row=2, column=0,columnspan=1)
    originalButton = Tkinter.Button(master=root,width=10, text='Original',font=helv36,command=lambda: original())
    originalButton.grid(row=0, column=0,columnspan=3)
    yellowBlueButton = Tkinter.Button(master=root,width=10, text='Yellow',fg='Yellow',bg='blue',font=helv36,command=lambda: yellowBlueF())
    yellowBlueButton.grid(row=3, column=0,columnspan=1)
    yellowBlackButton = Tkinter.Button(master=root,width=10, text='Black',fg='Black',bg='yellow',font=helv36,command=lambda: yellowBlackF())
    yellowBlackButton.grid(row=4, column=0,columnspan=1)
    blackYellowButton = Tkinter.Button(master=root,width=10, text='Yellow',fg='Yellow',bg='black',font=helv36,command=lambda: blackYellowF())
    blackYellowButton.grid(row=5, column=0,columnspan=1)


    #default_font = tkFont.nametofont("TkDefaultFont")
    #default_font.configure(family='Helvetica', size=24, weight='bold')
    #cameraControl=Tkinter.Tk()
    #helv362 = tkFont.Font(family='Helvetica', size=24, weight='bold')
    #pauseFocus = Tkinter.Button(master=root,width=12, text='Autofocus',fg='Black',font=helv36,command=lambda: pauseFocusF())
    #pauseFocus.grid(row=0, column=3,columnspan=1)
    #minusFocus = Tkinter.Button(master=cameraControl,width=5, text='Focus -',fg='Black',font=helv362,command=lambda: minusFocusF())
    #minusFocus.grid(row=1, column=0,columnspan=1)
    #plusFocus = Tkinter.Button(master=cameraControl,width=5, text='Focus +',fg='Black',font=helv362,command=lambda: plusFocusF())
    #plusFocus.grid(row=1, column=1,columnspan=1)
    sliderFocus=Tkinter.Scale(master=root,from_=255, to=0, resolution=5, font=helv36,label='Focus', command=slideFocusF, length=300, width=50)#fake limit is set at 25 and not 255 on the focus
    sliderFocus.grid(row=8, column=0,columnspan=1,rowspan=6)
    sliderFocus.set(10)

    
    root.wm_title("Controls")
    #cameraControl.wm_title("Focus")
    
    img1=parent_conn.recv()#read frame from thread
    parent_conn.close()#cleaning up after read
    d.join()
    parent_conn, child_conn = Pipe()#point to point connection between thread and main
    d = threading.Thread(name='daemon', target=daemon,args=(cam,child_conn))#starts the thread that only reads the frames. Also starting now sets this thread to be working while main is displaying the last frame
    d.setDaemon(True)#allow main to close without it... IDK seemed like a good idea
    d.start()
    
    
    #img1 = Image.fromarray(img1)###########################################
    #img1 = ImageTk.PhotoImage(img1)

    #cv2.namedWindow("Preview", cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow("Preview",cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Preview",cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


    
    panel=None
    root.attributes("-topmost", True)

    root.after(0, func=lambda: loop(cam,d,parent_conn))
    root.after(50, func=lambda: lifterLoop(root))
    #root.after(500, func=lambda: gc.collect())
    root.wm_protocol("WM_DELETE_WINDOW",lambda: quit_(cam,root))#may not need wm_
    root.mainloop()
