#Mirata v0.5 by tbcr
#This application was written in python 2.7 and is released under the GNU Public License v3
#A copy of this license can be found in the LICENSE document.
#This application downloads both snap images of the alephone source port (https://github.com/Aleph-One-Marathon/alephone)
#and free-to-download scenario files that are property of Bungie LLC.
import os
import time
import getpass
USER = getpass.getuser()
from urlgrabber.grabber import URLGrabber
from urlgrabber.progress import text_progress_meter
url = "http://174.109.47.119/files/alephone.snap"
BASEDIR="/home/" + USER  + "/mirata/"
SNAP="/home/" + USER  + "/mirata/snap/"
SCEN="/home/" + USER  + "/mirata/scenarios/"
PLUG="/home/" + USER  + "/mirata/plugins/"
M1 = "http://github.com/Aleph-One-Marathon/alephone/releases/download/release-20150620/Marathon-20150620-Data.zip"
FILE_M1 = "m1.zip"
M2 = "http://github.com/Aleph-One-Marathon/alephone/releases/download/release-20150620/Marathon2-20150620-Data.zip"
FILE_M2 = "m2.zip"
MINF = "https://github.com/Aleph-One-Marathon/alephone/releases/download/release-20150620/MarathonInfinity-20150620-Data.zip"
FILE_MINF = "minf.zip"
cmd='nothing'

def distpkg(pick):
    #Determining package manager command from input of 'option'
    if pick == 1:
        act = 'rpm -qa |grep snapd | wc -l'
    elif pick == 2:
        act = 'apt list snapd | grep snapd | wc -l'
    elif pick == 3:
        act = 'pacman -Qs snapd | grep snapd | wc -l'
    elif pick == 4:
        act = 'emerge -p snapd | grep snapd | wc -l'
    elif pick == 5:
        act = 'equo search --installed | wc -l'
    else:
        print("INVALID OPTION")
        exit(0)
    return act

def tril_down():
    cont = 1
    count =0
    
    while cont == 1 and count < 3:
    
        print("Please Select a Scenario")
        print("------------------------")
        print("1)Marathon") 
        print("2)Marathon 2: Durandal")
        print("3)Marathon Infinity")
        print("0)Skip")
        
        sel = input("Selection: ")
        
        if sel == 0:
            break
        else:
            if sel == 1:
                act_url = M1
                act_file = FILE_M1
                time.sleep(1) 
            elif sel == 2:
                act_url = M2
                act_file = FILE_M2
                time.sleep(1) 
            elif sel == 3:
                act_url = MINF
                act_file = FILE_MINF
                time.sleep(1) 
            
            g = URLGrabber(reget='simple')
            local_file=g.urlgrab(act_url, filename= SCEN + act_file,  progress_obj=text_progress_meter())
            print("done")
            
        print("Would you like to download more scenarios")
        print("1)Yes")
        print("2)No")
        cont = input("Selection: ")
        
        count += 1
        print(count)
        
        
    
    
def exist_dir(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)
     

    
def snap_cmd(ot):
    if ot == 1:
        return 'sudo dnf -y install snapd'
    elif ot == 2:
        return 'sudo apt -y install snapd'
    elif ot == 3:
        return 'yes | sudo pacman -S snapd'
    elif ot == 4:
        return 'sudo emerge snapd'
    elif ot == 5:
        return 'sudo equo install snapd'
        
        

    
def snap_inst(coop):
        print('snapd needs to be installed...attempting now')
        os.system(coop)
        os.system('sudo snap install --devmode ' + SNAP + 'alephone.snap')


os.system('clear')
print("mirata, the AlephOne Linux setup tool")
print("Version .5 by tbcr")
print("-----------------------------------------")
print("")
time.sleep(3)

#Displays options then gets option of choice
print("Before we begin, please select your distro")
print("------------------------------------------")
print("1)Fedora")
print("2)Ubuntu")
print("3)Arch")
print("4)Gentoo")
print("5)Sabayon(Equo)")
print("")
option = input("Selection: ")

cmd = distpkg(option)

os.system('clear')

print("Creating needed irectories in ~/")
exist_dir(BASEDIR)
exist_dir(SNAP)
exist_dir(PLUG)
exist_dir(SCEN)
    
time.sleep(3)

print('Part 1: Downloading Snap')
g = URLGrabber(reget='simple')
local_file=g.urlgrab(url, filename= SNAP +'alephone.snap',  progress_obj=text_progress_meter())
print("DONE!")

print('Part 2: Detecting snapd Installation')

inst = os.system(cmd)
com = snap_cmd(option)


print('Part 3: Setting up Snap')
if inst == 0:
    snap_inst(com)
    print('DONE')
elif inst > 0:
    print('Snapd is already installed')

time.sleep(1)
os.system('clear')

print('Part 4: Scenarios')
print('-----------------')

print('Would you like to download the trilogy?')
print('-----------------------------------------------------------')
print('1)yes')
print('2)no')
scen_tril = input('Selection: ')

if scen_tril == 1:
    tril_down()

print("Setup completed, files can be found in ~/mirata")
print("Start alephone with 'sudo snap run alephone'")










