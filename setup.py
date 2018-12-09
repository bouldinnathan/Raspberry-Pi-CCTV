import os


print("starting update")
output=os.system('sudo apt-get update -y')
if output==0:
    print('good update')
else :
    print('failed update')
    
output=os.system('sudo apt-get upgrade -y')
if output==0:
    print('good update')
else :
    print('failed update')
    
