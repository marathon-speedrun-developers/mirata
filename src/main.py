#Mirata v.1 by tbcr
#coded in Python 2.9
#released under GNU GPL,
#a copy of which is in
#the same folder as this

import os
import time
import subprocess
from urlgrabber.grabber import URLGrabber
from urlgrabber.progress import text_progress_meter
url = "http://174.109.47.119/files/alephone.snap"


os.system('clear')
print("MIRATA, the AlephOne Linux setup tool")
print("Version .1 by tbcr")
print("-----------------------------------------")
print("")
time.sleep(3)

print("Before we begin, please select your distro")
print("------------------------------------------")
print("1)Fedora")
print("2)Ubuntu")
print("3)Arch")
print("4)Gentoo")
print("5)openSUSE")
print ("6)Sabayon(Equo)")
print("")
option = input("Selection: ")

def distro_install_cmd(option):
    switcher = {
        1:  import
    }



print('Part 1: Downloading Snap')
g = URLGrabber(reget='simple')
local_file=g.urlgrab(url, filename='alephone.snap')
print("DONE!")

#print('Part 2: Detecting snapd Installation')

print('Part 3: Setting up Snap')
