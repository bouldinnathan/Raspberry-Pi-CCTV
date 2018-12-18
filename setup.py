#!/usr/bin/env python3
import os
import time

print("Answer all of the questions. The setup will run unattended after that(~2hrs).")
user_input=input('Would you like to update all (y/n)?')[0]
user_input2=input('Is the SD card at least 16GB (y/n)?')[0]
if not(user_input2=='y'):
    print('The opencv library is a very large source and must be compiled. Exiting...')
    exit()
user_input3=input('Would you like the full install(y/n)?')[0]
user_input4=input('Would you like the autostart on (y/n)?')[0] 
#--------------update all----------------------
if user_input=='y':
    print("-------------starting update-----------------")
    output=os.system('sudo apt-get update -y')
    
    if output==0:
        print('success update')
    else :
        print('failed update')
        
    output=os.system('sudo apt-get upgrade -y')
    if output==0:
        print('success update')
    else :
        print('failed update')
    output=os.system('sudo apt-get dist-upgrade -y')
    if output==0:
        print('success update')
    else :
        print('failed update')
#--------------update all----------------------
##--------------dependencies-------------------
print('-------------Getting dependencies…---------------')
output=os.system('sudo apt-get install build-essential cmake pkg-config -y')
output=os.system('sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev -y')+output
output=os.system('sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev -y')+output
output=os.system('sudo apt-get install libxvidcore-dev libx264-dev -y')+output
output=os.system('sudo apt-get install libgtk2.0-dev -y')+output
output=os.system('sudo apt-get install libatlas-base-dev gfortran -y')+output
output=os.system('sudo apt-get install python2.7-dev python3-dev -y')+output

#output=os.system('sudo apt-get install build-essential cmake cmake-curses-gui \
#                               pkg-config libpng12-0 libpng12-dev libpng++-dev \
#                               libpng3 libpnglite-dev zlib1g-dbg zlib1g zlib1g-dev \
#                               pngtools libtiff4-dev libtiff4 libtiffxx0c2 libtiff-tools libeigen3-dev;sudo apt-get install libjpeg8 libjpeg8-dev libjpeg8-dbg libjpeg-progs \
#                               ffmpeg libavcodec-dev libavcodec53 libavformat53 \
#                               libavformat-dev libxine1-ffmpeg libxine-dev libxine1-bin \
#                               libunicap2 libunicap2-dev swig libv4l-0 libv4l-dev \
#                               python-numpy libpython2.6 python-dev python2.6-dev libgtk2.0-dev')+output

if output==0:
    print('success dependencies')
else :
    print('failed dependencies')
##--------------dependencies------------------

###-------------get Opencv------------------
if (user_input3=='y'):
    print('-------------Getting opencv--------------')
    output=os.system('wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.0.0.zip')
    output=os.system('unzip opencv.zip')+output
    output=os.system('sudo rm opencv.zip')+output
    output=os.system('wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.0.0.zip')+output
    output=os.system('unzip opencv_contrib.zip')+output
    output=os.system('sudo rm opencv_contrib.zip')+output
    if output==0:
        print('success download of opencv')
    else :
        print('failed download of opencv')

    #output=os.system('wget https://bootstrap.pypa.io/get-pip.py')
    #output=os.system('sudo python get-pip.py')

    output=os.system('pip3 install numpy')
    output=os.system('cd opencv-3.0.0; mkdir build;cd build')+output
    output1=os.system('cd opencv-3.0.0/build/;cmake -D CMAKE_BUILD_TYPE=RELEASE \
        -D CMAKE_INSTALL_PREFIX=/usr/local \
        -D INSTALL_PYTHON_EXAMPLES=ON \
        -D ENABLE_PRECOMPILED_HEADERS=OFF \
        -D WITH_FFMPEG=OFF\
        -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.0.0/modules \
        -D BUILD_EXAMPLES=ON ..')

    if output==0:
        print('success pre-install of opencv')
    else :
        print('failed pre-install of opencv')
        
    if output1==1:
        print('success pre-install of opencv')
    else :
        print('Errors but should be fine...')


    output=os.system('cd opencv-3.0.0/build/;make;sudo make install')
    if output==0:
        print('success make/install of opencv')
    else :
        print('failed make/install of opencv')

        
    output=os.system('sudo rm -r opencv-3.0.0;sudo rm -r opencv_contrib-3.0.0;sudo rm -r build')
    if output==0:
        print('success removing files')
    else :
        print('failed removing files')
####-------------autostart------------------
if (user_input4=='y'):
    cwd = os.getcwd()
    #f= open("/etc/rc.local","w+")
    f= open("/home/pi/.config/lxsession/LXDE-pi/autostart","w")
    text='''@lxpanel --profile LXDE-pi\n@pcmanfm --desktop --profile LXDE-pi\n@xscreensaver -no-splash'''
    text=text+'''\n@sleep 10 \n@sudo python3 '''+str(cwd)+'''/DesktopCover.py & \n@sudo python3 '''+str(cwd)+'''/Start_Here.py &\n'''
    text=text+'''@sudo rm /home/pi/lock.txt'''
    #output=os.system('sudo nano /etc/xdg/lxsession/LXDE-pi/autostart')
    print(text)
    user_input5=input('text'+'Is this correct (y/n)?')[0]
    if (user_input5=='y'):
        f.write(text)
        f.flush()
        f.close()
        #adding absolute 
        f= open(str(cwd)+"/Start_Here.py","r")
        text=f.read()
        text=text.replace('''working_dirctory=''''','working_dirctory='+"'"+str(cwd)+'/'+"'")
        f.close()
        f= open(str(cwd)+"/Start_Here.py","w")
        f.write(text)
        f.flush()
        f.close()
        #adding absolute
        f= open(str(cwd)+"/CorrectVeiw.py","r")
        text=f.read()
        f.close()
        text=text.replace('''working_dirctory=''''','working_dirctory='+"'"+str(cwd)+'/'+"'")
        f= open(str(cwd)+"/CorrectVeiw.py","w")
        f.write(text)
        f.flush()
        f.close()
        
        
time.sleep(5)
os.system('sudo reboot')

        
    










