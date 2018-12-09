import os

print("Answer all of the questions. The setup will run unattended after that(~2hrs).")
user_input=input('Would you like to update all (y/n)?')
user_input2=input('Is the SD card at least 16GB (y/n)?')
if not(user_input2=='y'):
    print('The opencv library is a very large source and must be compiled. Exiting...')
    exit()
#--------------update all----------------------
if user_input=='y':
    print("starting update")
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

print('Getting dependencies…')
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














