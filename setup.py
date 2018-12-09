import os

print("Answer all of the questions. The setup will run unattended after that(~2hrs).")
user_input=input('Would you like to update all (y/n)?')
user_input2=input('Is the SD card at least 16GB (y/n)?')
if not(user_input2=='y' or user_input2=='yes'):
    print('The opencv library is a very large source and must be compiled. Exiting...')
    exit()
user_input3=input('Would you like the full install(y/n)?')    
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
if user_input3!='y'or user_input3!='yes':
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
output=os.system('cd opencv-3.1.0; mkdir build;cd build')+output
output1=os.system('cd opencv-3.1.0/build/;cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.1.0/modules \
    -D BUILD_EXAMPLES=ON ..')

if output==0:
    print('success pre-install of opencv')
else :
    print('failed pre-install of opencv')
    
if output1==1:
    print('Errors but should be fine...')
else :
    print('failed pre-install of opencv')


output=os.system('cd opencv-3.1.0/build/;make -j4')
if output==0:
    print('success make of opencv')
else :
    print('failed make of opencv')















