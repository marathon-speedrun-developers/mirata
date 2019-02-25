#Mirata v0.6 - The Linux setup utility for AlephOne
#by Brandon Clark and Chance Callahan

#    This file is part of mirata.

#    mirata is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    mirata is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with mirata.  If not, see <https://www.gnu.org/licenses/>.

#    This application downloads both snap images of the alephone source port (https://github.com/Aleph-One-Marathon/alephone)
#    and free-to-download scenario files that are property of Bungie LLC.
import os
import time
import subprocess
import argparse
import sys

from whichcraft import which
from subprocess import call

snap_bugout = False
target_os = ""
refactor_override = False
live_dangerously = False
nerf_snapd = False

url = "https://mirata.chancecallahan.com/a1/dangerzone/current/alephone.snap"


act_os = 60
sup_os = ['Ubuntu', 'Fedora', 'Arch', 'Gentoo', 'openSUSE', 'Sabayon']

def get_args():
    global refactor_override
    global target_os
    global snap_bugout
    global live_dangerously
    global nerf_snapd
    parser = argparse.ArgumentParser()
    parser.add_argument("--override-snap-bugout", dest="snap_bugout", help="Overrides sanity check for snapcraft.", action="store_true", default=False)
    parser.add_argument("--target-os", dest="target_os", help="Select target OS, see --eligible-targets", action="store")
    parser.add_argument("--eligible-targets", help="Eligible Target Platforms: Ubuntu, Fedora, Arch, Gentoo, openSUSE, Sabayon")
    parser.add_argument("--refactor-override", dest="refactor_override", help="No one in their sane mind would use this flag right now.", action="store_true", default=False)
    parser.add_argument("--live-dangerously", dest="live_dangerously", help="Just used for debug purposes. It won't exist in the final release.", action="store_true", default=False)
    parser.add_argument("--nerf-snapd", dest="nerf_snapd", help="Nerfs snapd detection for debug purposes.", action="store_true", default=False)
    args = parser.parse_args()
#    print parser.parse_args()
    refactor_override = args.refactor_override
    live_dangerously = args.live_dangerously
    snap_bugout = args.snap_bugout
    target_os = args.target_os
    nerf_snapd = args.nerf_snapd
    #    refactor_override = 
    print(refactor_override, live_dangerously, snap_bugout, target_os, nerf_snapd)
    refactor_safety()

    # This subroutine basically keeps some idiot from running the program in it's current state. Like us.

def refactor_safety():
    if refactor_override == True:
        print("Bless your heart, you stupid fool. Running as normal, and may God have mercy on your computer.")
        # At some point, we should add the call to the subrouting that runs this mess.
        os_preprocessing()
    else:
        print(refactor_override)
        print(nerf_snapd)
        print("Just... don't even bother trying to run this code right now. You'll need to perform an exorcism if you do, and you probably can't afford both a technomancer and whatever the hourly rate right now the Catholic Church is charging.")

def os_preprocessing():
    global act_os
    if target_os == "Ubuntu":
        act_os=0
        os_pp_debug()
    elif target_os == "Fedora":
        act_os=1
    elif target_os == "Arch":
        act_os=2
    elif target_os == "Gentoo":
        act_os=3
    elif target_os == "openSUSE":
        act_os=4
    elif target_os == "Sabayon":
        act_os=5
    else:
        os_pp_debug()


def os_pp_debug():
    print(act_os)
    print(target_os)
    time.sleep(5)	
    title_banner()

def title_banner():
    os.system('clear')
    print("mirata, the Linux setup tool for AlephOne")
    print("This program comes with ABSOLUTELY NO WARRANTY.")
    print("This is free software, and you are welcome to redistribute it under certain conditions.")
    print( '-' * 20 )
    time.sleep(3)
    check_for_snap_nerf()

def check_for_snap_nerf():
    if nerf_snapd == True:
        print("Acting as if snapd is not installed.")
        os_select()
    else:
        check_for_snap()

def check_for_snap():
    # Checks if snap is in the system PATH
    if nerf_snapd == True:
        os_routing()
    elif which('snap') is not None:
        snap_dl()
    else:
        print("Hmm. I don't see snapd installed. Let's get that fixed.")
        os_routing()

def os_select():
    global act_os
    if act_os == 60:
        print("Before we begin, please select your distro")
        print("------------------------------------------")
        print("1)Ubuntu")
        print("2)Fedora")
        print("3)Arch")
        print("4)Gentoo")
        print("5)openSUSE")
        print("6)Sabayon(Equo)")
        print("")
        act_os = int(input("Selection: "))
        act_os = act_os - 1
    else:
        print("I see you have selected " + sup_os[act_os] + " as your install target during runtime. Continuing unattended.")
    check_for_snap()

def snap_dl():
    print('Downloading the snap file...')
    call(["wget", url])
    installmirata()


def bugout_nosnap():
    #Checks if we are overriding the bugout
    if snap_bugout is True:
        snap_dl()
    else:
        print("I can't seem to find snap on this system. Either add it to your path, or use --override-snap-bugout to bypass this sanity check")

def installmirata():
    if live_dangerously == True:
        print("Installing Aleph One using snap. Stand by.")
        call(["snap", "install", "alephone.snap", "--dangerous", "--devmode"])
    else:
        print("Use --live-dangerously")

def os_routing():
    global act_os
    if act_os == 0:
        ubu_install()
    elif act_os == 1:
        fed_install()
 #   elif act_os == 2:
 #       arch_install()
 #   elif act_os == 3:
 #       needs_more_gentoo()
 #   elif act_os == 4:
 #       suse_install()
 #   elif act_os == 5:
 #       saba_install()
    else:
        print("Failure in the OS Routing Subroutine.")

def ubu_install():
    if act_os == 0:
        print("I'm going to install snapd from your distribution's package manager.")
        print("There shouldn't be any issues with the automated installation, but if you")
        print("want to be extra cautious/paranoid, just install it the old fashioned way.")
        print("")
        print("")
        print("I'm going to wait ten seconds for you to make up your mind, then I'll start.")
        print("Hit Ctrl+C to stop this script.")
        time.sleep(10)
        print("Hold your noses, here we go!")
        call(["sudo", "apt", "install", "snapd", "-y"])
        print("snapd has been installed. Resuming installation.")
        snap_dl()
    else:
        print("Failure in the snapd installation for Ubuntu subroutine.")


def fed_install():
    if act_os == 1:
        print("I'm going to install snapd from your distribution's package manager.")
        print("There shouldn't be any issues with the automated installation, but if you")
        print("want to be extra cautious/paranoid, just install it the old fashioned way.")
        print("")
        print("")
        print("I'm going to wait ten seconds for you to make up your mind, then I'll start.")
        print("Hit Ctrl+C to stop this script.")
        time.sleep(10)
        print("Hold your noses, here we go!")
        call(["sudo", "dnf", "install", "snapd", "-y"])
        print("")
        print("")
        print("")
        print("")
        print("snapd has been installed. Resuming installation.")
        print("")
        print("")
        snap_dl()
    else:
        print(act_os)
        print("Failure in the snapd installation for Fedora subroutine.")

def suse_install():
    if act_os == 4:
        suse_ver = input("Enter your version of openSUSE Leap here (15.0 or 42.3 supported):")
        print("I'm going to install snapd from your distribution's package manager.")
        print("There shouldn't be any issues with the automated installation, but if you")
        print("want to be extra cautious/paranoid, just install it the old fashioned way.")
        print("")
        print("")
        print("I'm going to wait ten seconds for you to make up your mind, then I'll start.")
        print("Hit Ctrl+C to stop this script.")
        time.sleep(10)
        print("Hold your noses, here we go!")
        call(["sudo", "zephyr", "addrepo", "--refresh", "https://download.opensuse.org/repositories/system:/snappy/openSUSE_Leap_"+suse_ver+" snappy"])
    else:
        print(act_os)
        print("Failure in the snapd installation for openSUSE subroutine.")


def main():
    get_args()

if __name__ == '__main__':
    main()
