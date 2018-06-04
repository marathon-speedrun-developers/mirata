#Mirata v.1 by tbcr
#coded in Python 2.9
#released under GNU GPL,
#a copy of which is in
#the same folder as this

import os
import grabber
import time
import subprocess
from whichcraft import which
import argparse
import sys
import requests
from tqdm import tqdm

url = "http://174.109.47.119/files/alephone.snap"
active_os = 60
supported_os = ['Ubuntu', 'Fedora', 'Arch', 'Gentoo', 'openSUSE', 'Sabayon']

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--override-snap-bugout", help="Overrides sanity check for snapcraft.", action="store_true")
    parser.add_argument("--target-os", help="Select target OS, see --eligible-targets", action="store")
    parser.add_argument("--eligible-targets", help="Eligible Target Platforms: Ubuntu, Fedora, Arch, Gentoo, openSUSE, Sabayon")
    args = parser.parse_args()

def os_preprocessing(active_os, target_os):
    if target_os == "Ubuntu":
        active_os=0
    elif target_os == "Fedora":
        active_os=1
    elif target_os == "Arch":
        active_os=2
    elif target_os == "Gentoo":
        active_os=3
    elif target_os == "openSUSE":
        active_os=4
    elif target_os == "Sabayon":
        active_os=5
    else:
        print("Fatal Error in the OS Preprocessing Subroutine. Good Night.")
        sys.quit()

def title_banner():
    os.system('clear')
    print("MIRATA, the AlephOne Linux setup tool")
    print("Version .1 by tbcr")
    print("-----------------------------------------")
    print("")
    time.sleep(3)
    os_select()

def os_select(active_os, supported_os):
    if active_os == 60:
        print("Before we begin, please select your distro")
        print("------------------------------------------")
        print("1)Fedora")
        print("2)Ubuntu")
        print("3)Arch")
        print("4)Gentoo")
        print("5)openSUSE")
        print("6)Sabayon(Equo)")
        print("")
        active_os = input("Selection: ")
        active_os = active_os - 1
    else:
        print("I see you have selected " + supported_os[active_os] + " as your install target during runtime. Continuing unattended.")
    snap_dl()



def snap_dl(url):
    print('Downloading the snap file...')
    response = requests.get(url, stream=True)

    with open("alpehone.snap", wb) as handle:
        for data in tqdm(response.iter_content()):
            handle.write(data)
    

def check_for_snap():
    # Checks if snap is in the system PATH
    if which('snap') is not None:
        installmirata()
    else:
        bugout_nosnap()

def bugout_nosnap():
    #Checks if we are overriding the bugout
    if args.override-snap-bugout is True:
        installmirata()
    else:
        print("I can't seem to find snapcraft on this system. Either add it to your path, or use --override-snap-bugout to bypass this sanity check")
        #Sweet Dreams
        sys.exit()



print('Part 2: Detecting snapd Installation')



print('Part 3: Setting up Snap')
