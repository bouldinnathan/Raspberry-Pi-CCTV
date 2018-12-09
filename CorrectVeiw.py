#!/usr/bin/python3


#>>>>>>>>>>>>>>>>>>>>Read Me<<<<<<<<<<<<<<<<<<<<<<
#If you mistakenly opened this click the "x" in the
#top right corner and do not save any changes. 
#>>>>>>>>>>>>>>>>>>>>Read Me<<<<<<<<<<<<<<<<<<<<<<<<

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


#“For libray cv2 Copyright (c) 2018 Open Source Computer Vision Library.  All rights reserved.
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

#NOTE: The axis are all messed up
import tkinter as Tkinter
import tkinter
from tkinter import font as tkFont
import PIL
from PIL import Image
import cv2
import numpy
from math import floor
import os

displayImgMultiplier=.50 #edit to fit screen
location='/home/pi/currentPic.png'
img0=cv2.imread(location,1)

keyPress=-1
img1=img0
x,y,_=img0.shape
zoomFactor=1
shiftX=0
shiftY=0
colorShift=-1
rotateBy90=0
#cv2.namedWindow("camera", cv2.WINDOW_KEEPRATIO | cv2.WINDOW_FULLSCREEN)
#cv2.namedWindow("camera", cv2.WND_PROP_FULLSCREEN)
#cv2.namedWindow("camera", cv2.WINDOW_FULLSCREEN)
cv2.namedWindow("camera",cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("camera",cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

def threshToRGB(img1):
    #img1 = cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)#this is a better threshold but it is slow
    _,img1 = cv2.threshold(img1,127,255,cv2.THRESH_BINARY);## slider on the 127(half way piont) now 100
    img1=cv2.cvtColor(img1,cv2.COLOR_GRAY2RGB);
    return img1
def invThreshToRGB(img1):
    _,img1 = cv2.threshold(img1,127,255,cv2.THRESH_BINARY_INV);## slider on the 127(half way piont) now 100
    img1=cv2.cvtColor(img1,cv2.COLOR_GRAY2RGB);
    return img1

while 1:
    #if x>y:#this bunches up the whole page to fit on the screen
    #    temp=x
    #    x=y
    #    y=temp
    
    if keyPress==1114039 or keyPress==1114041 or keyPress==1114037 or keyPress==1114033 or keyPress==1114035 or keyPress==1114032:#########
        colorShift=-1
        
    if keyPress==1114026 or keyPress==65450:# this is *
        rotateBy90=rotateBy90+1
        
    if keyPress==1114038:#this is 6
        print (colorShift)
        shiftX=shiftX+floor((9*5)*5/2)
        x,y,_=img0.shape
        imgTobeCheck = img0[shiftY+0:shiftY+x-(x/50)*zoomFactor,shiftX+0:shiftX+y-(y/50)*zoomFactor]#temp image that wants to be a real boy
        xCheck,yCheck,_=imgTobeCheck.shape#this is done because it is easier to check that the aspect ratio is close to correct then to find a moving boarder with respect to shift(X/Y) 
        if yCheck!=0 and xCheck/yCheck > (x/y)-((x/y)*.05) and xCheck/yCheck < (x/y)*1.05:#the (x/y)Check must not be 0 and if it is then the if statment fails and the if statment will not divid by zero
            img1=imgTobeCheck #fuzzy logic says close enough!!!
        else:
            shiftX=shiftX-floor((9*5)*5/2)#fuzzy logic says No
    elif keyPress==1114036:#this is 4
        shiftX=shiftX-floor((9*5)*5/2)
        x,y,_=img0.shape
        if shiftX < 0:
            shiftX=0
        img1 = img0[shiftY+0:shiftY+x-(x/50)*zoomFactor,shiftX+0:shiftX+y-(y/50)*zoomFactor]
    elif keyPress==1114040:#this is 8
        shiftY=shiftY-floor((16*5)*5/2)
        x,y,_=img0.shape
        if shiftY < 0:
            shiftY=0
        img1 = img0[shiftY+0:shiftY+x-(x/50)*zoomFactor,shiftX+0:shiftX+y-(y/50)*zoomFactor]
    elif keyPress==1114034:#this is 2
        shiftY=shiftY+floor((16*5)*5/2)
        x,y,_=img0.shape
        imgTobeCheck = img0[shiftY+0:shiftY+x-(x/50)*zoomFactor,shiftX+0:shiftX+y-(y/50)*zoomFactor]#temp image that wants to be a real boy
        xCheck,yCheck,_=imgTobeCheck.shape#this is done because it is easier to check that the aspect ratio is close to correct then to find a moving boarder with respect to shift(X/Y) 
        if yCheck!=0 and xCheck/yCheck > (x/y)-((x/y)*.05) and xCheck/yCheck < (x/y)*1.05:#the (x/y)Check must not be 0 and if it is then the if statment fails and the if statment will not divid by zero
            img1=imgTobeCheck #fuzzy logic says close enough!!!
        else:
            shiftY=shiftY-(16*5)*5#fuzzy logic says No
        
    else:
        i=1+1

    if keyPress==1114027:#this is +
        x,y,_=img0.shape
        
        zoomFactor=zoomFactor+1
        imgTobeCheck = img0[shiftY+0:shiftY+x-(x/50)*zoomFactor,shiftX+0:shiftX+y-(y/50)*zoomFactor]
        xCheck,yCheck,_=imgTobeCheck.shape
        if xCheck>50 and yCheck>50:
            img1=imgTobeCheck
        else:
            zoomFactor=zoomFactor-1
        #print (img1.shape)
    elif keyPress==1114029:#this is -
        zoomFactor=zoomFactor-1
        x,y,_=img0.shape
        img1 = img0[shiftY+0:shiftY+x-(x/50)*zoomFactor,shiftX+0:shiftX+y-(y/50)*zoomFactor]
    else:
        i=1+1

    if keyPress==1114039 or colorShift==7:#this is 7
        img1 = img0[shiftY+0:shiftY+x-(x/50)*zoomFactor,shiftX+0:shiftX+y-(y/50)*zoomFactor]
        img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
        img1=threshToRGB(img1)
        colorShift=7
    elif keyPress==1114041 or colorShift==9:#this is 9
        img1 = img0[shiftY+0:shiftY+x-(x/50)*zoomFactor,shiftX+0:shiftX+y-(y/50)*zoomFactor]#with the inverter a clean image is needed
        img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
        img1=invThreshToRGB(img1)
        #ret,img1 = cv2.threshold(img1,127,255,cv2.THRESH_BINARY_INV)
        #img1=cv2.cvtColor(img1,cv2.COLOR_GRAY2RGB)
        colorShift=9
    elif keyPress==1114037 or colorShift==5:#this is 5
        x,y,_=img0.shape
        img1 = img0[shiftY+0:shiftY+x-(x/50)*zoomFactor,shiftX+0:shiftX+y-(y/50)*zoomFactor]
        colorShift=5
    elif keyPress==1114033 or colorShift==1:#this is 1
        img1 = img0[shiftY+0:shiftY+x-(x/50)*zoomFactor,shiftX+0:shiftX+y-(y/50)*zoomFactor]
        img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
        img1=threshToRGB(img1)
        #_,img1 = cv2.threshold(img1,127,255,cv2.THRESH_BINARY);## slider on the 127(half way piont) now 100
        #img1=cv2.cvtColor(img1,cv2.COLOR_GRAY2RGB);
        img1[numpy.where((img1==[255,255,255]).all(axis=2))] = [0,255,255];
        colorShift=1
    elif keyPress==1114035 or colorShift==3:#this is 3
        img1 = img0[shiftY+0:shiftY+x-(x/50)*zoomFactor,shiftX+0:shiftX+y-(y/50)*zoomFactor]#with the inverter a clean image is needed
        img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
        img1=invThreshToRGB(img1)
        #ret,img1 = cv2.threshold(img1,127,255,cv2.THRESH_BINARY_INV);## slider on the 127(half way piont) now 100
        #img1=cv2.cvtColor(img1,cv2.COLOR_GRAY2RGB);
        img1[numpy.where((img1==[255,255,255]).all(axis=2))] = [0,255,255];
        colorShift=3
    elif keyPress==1114032 or colorShift==0:#this is 0
        img1 = img0[shiftY+0:shiftY+x-(x/50)*zoomFactor,shiftX+0:shiftX+y-(y/50)*zoomFactor]
        img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
        img1=threshToRGB(img1)
        #ret,img1 = cv2.threshold(img1,127,255,cv2.THRESH_BINARY)## slider on the 127(half way piont) now 100
        #img1=cv2.cvtColor(img1,cv2.COLOR_GRAY2RGB);#this one works for some reason?!?
        img1[numpy.where((img1==[0,0,0]).all(axis=2))] = [0,255,255]
        img1[numpy.where((img1==[255,255,255]).all(axis=2))] = [255,0,0]
        colorShift=0
    #>>>>>>>>>this does not work...opencv error<<<<<<<<<<<<<<<
    #elif keyPress==1114030:#this is .
    #    img0=cv2.imread(location,0)#I KNOW!!!
    #    img1 = img0[shiftY+0:shiftY+x-(x/50)*zoomFactor,shiftX+0:shiftX+y-(y/50)*zoomFactor];
    #    x,y=img1.shape# will have to change back to the true values
    #    ret,imgInvThreshold = cv2.threshold(img1,127,255,cv2.THRESH_BINARY_INV)
    #    ret,imgThreshold = cv2.threshold(img1,127,255,cv2.THRESH_BINARY)
    #    imgThreshold=cv2.cvtColor(imgThreshold, cv2.COLOR_GRAY2RGB)
    #    imgInvThreshold=cv2.cvtColor(imgInvThreshold, cv2.COLOR_GRAY2RGB)
    #    color0 = numpy.repeat([0,255,255], x*y).reshape((x,y,3))
    #    color1 = numpy.repeat([255,0,0], x*y).reshape((x,y,3))
    #    img1=numpy.bitwise_and(color0,imgInvThreshold)
    #    img0=cv2.imread(location,1)
    #    x,y,_=img0.shape# true values
    #    img1.astype('uint8')#forcing it into binary
    #    print(img1)
    #    print(img1.shape)
    #>>>>>>>>>this does not work...<<<<<<<<<<<<<<<
    else:
        i=1+1
        
    if keyPress==1113997:    # "Enter" with numlock on for change
        print ("Quit")
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        cv2.waitKey(1)
        cv2.waitKey(1)
        cv2.waitKey(1)
        #sys.exit()
        os.system('python3 /home/pi/Desktop/Start\ Here.py')
        quit()


    #img1=numpy.rot90(img1,rotateBy90)
    #rotateBy90=0

    #<<<<<<<<<<rotates but places black bars>>>>>>>>>
    #if rotateBy90:
    #    yofimg2,xofimg2=img1.shape[:2]
    #    center=(floor(yofimg2/2),floor(xofimg2/2))
    #    temp=cv2.getRotationMatrix2D(center,rotateBy90*90,1)
    #    img1=cv2.warpAffine(img1,temp,(yofimg2,xofimg2))
    #    rotateBy90=0
    #<<<<<<<<<<rotates but places black bars>>>>>>>>>

    img2 = cv2.resize(img1,(floor(y*displayImgMultiplier),floor(x*displayImgMultiplier)))#(1920, 1080),interpolation = cv2.INTER_NEAREST)
    #print(str(floor(y*displayImgMultiplier))+' '+str(floor(x*displayImgMultiplier)))

    #<<<<<<<<<<rotates but places black bars>>>>>>>>>
    #yofimg2,xofimg2=img2.shape[:2]
    #center=(floor(yofimg2/2),floor(xofimg2/2))
    #temp=cv2.getRotationMatrix2D(center,rotateBy90*90,1)
    #img2=cv2.warpAffine(img2,temp,(yofimg2,xofimg2))
    #<<<<<<<<<<rotates but places black bars>>>>>>>>>
    
    print(rotateBy90)

    #<<<<<<<this works but the rotate is hard coded>>>>>>
    #img2 =img2.transpose((1,0,2))
    #img2=numpy.fliplr(img2)
    #<<<<<<<this works but the rotate is hard coded>>>>>>
    if rotateBy90:
        img1=numpy.rot90(img1,rotateBy90)
        img0=numpy.rot90(img0,rotateBy90)
        rotateBy90=0
    if colorShift==1 or colorShift==3 or colorShift==0:
        magicify=(255,255,255)
    else:
        magicify=(0,255,255)

    cv2.putText(img2,'X'+str(int(zoomFactor/5.875)+1),(10,50),cv2.FONT_HERSHEY_SIMPLEX,2,magicify,4)
    cv2.imshow("camera",img2)#opencv is coded in C and is wrapped in python so is will show the image with less than a Sec or more delay.
    keyPress=cv2.waitKey(1)#A 1ms delay is DEMANDED by the coding Gods for cv2.imshow to bless us with sub Sec latency. Praise Them. But no really this has to be in the loop.  

    

