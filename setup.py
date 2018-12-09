import os

print("Answer all of the questions. The setup will run unattended after that(~2hrs).")
user_input=input('Would you like to update all (y/n)?')
user_input2=input('Is the SD card at least 16GB (y/n)?')
if not(user_input2=='y'):
    print('The opencv library is a very large source and must be compiled. Exiting...')
    exit()
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
##--------------dependencies------------------
print('-------------Getting dependencies…---------------')
output=os.system('sudo apt-get install build-essential cmake pkg-config -y')
output=os.system('sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev -y')+output
output=os.system('sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev -y')+output
output=os.system('sudo apt-get install libxvidcore-dev libx264-dev -y')+output
output=os.system('sudo apt-get install libgtk2.0-dev -y')+output
output=os.system('sudo apt-get install libatlas-base-dev gfortran -y')+output
output=os.system('sudo apt-get install python2.7-dev python3-dev -y')+output
if output==0:
    print('success dependencies')
else :
    print('failed dependencies')
##--------------dependencies------------------

###-------------get Opencv------------------
print('-------------Getting opencv--------------')
output=os.system('wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.1.0.zip')
output=os.system('unzip opencv.zip')+output
output=os.system('sudo rm opencv.zip')+output
output=os.system('wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.1.0.zip')+output
output=os.system('unzip opencv_contrib.zip')+output
output=os.system('sudo rm opencv_contrib.zip')+output
if output==0:
    print('success download of opencv')
else :
    print('failed download of opencv')

#output=os.system('wget https://bootstrap.pypa.io/get-pip.py')
#output=os.system('sudo python get-pip.py')

output=os.system('pip3 install numpy')
output=os.system('mkdir /opencv-3.1.0/build')+output
output=os.system('cmake /opencv-3.1.0/build -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.1.0/modules \
    -D BUILD_EXAMPLES=ON ..')+output
if output==0:
    print('success pre-install of opencv')
else :
    print('failed pre-install of opencv')















