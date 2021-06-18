#Mirata v0.7 - The Linux setup utility for AlephOne
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

#    This application downloads both appimages of the alephone source port (https://github.com/Aleph-One-Marathon/alephone)
#    and free-to-download scenario files that are property of Bungie LLC.

import sqlite3
import urllib.request as Request

from github import Github
from zipfile import ZipFile
from io import BytesIO as bio
from tkinter import *
from tkinter.ttk import *
from pathlib import Path
import sqlite3

tk = Tk()
tk.title = "Mirata v0.7"
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)

#read-only token for checking repository tags
tok = "<insert token here>"
basedir = "{}/.mirata".format(Path.home())
git_rep = "alephone/marathon"

class Tk():
    # ============================================================================== 
    # FUNCTIONS AHOY!
    # ==============================================================================

    #something...something....python 3.10 will make this less convoluted....
    #update Jun 11, 2021 - LOL NAH FAM
    def dwnldAlephone(verPick):
            try:
                ai_pick = Path("{}/appimages/ao_{}.appimage".format(basedir, verPick))
            except FileNotFoundError:
                print(verPick," is not detected, downloading....")
                urllib.request.urlretrieve("http://blah.example.com/appimages/ao_{}.appimage".format(verPick), ai_pick)
                print(verPick," downloaded to ~/.mirata/appimages/")
            else:
                print(verPick," appimage already detected in ~/.mirata/appimages/")
            finally:
                print("Moving Onward...")

    #  The first thing application should do is make sure directories are available in home directory.
    def directoryCheck():
        print("Creating required directories (if needed)")

        for dir in ["scenarios","maps","appimages","scripts","films"]:
            Path("{}/{}".format(basedir,dir)).mkdir(parents=True, exist_ok=True)
        
    def db_init():
        
        db_file = Path("{}/mirata.db".format(basedir))
        print("Checking for metadata db for launcher")
        try:
            db_file.is_file()
        except False:
            print("db not found. Creating...")
            conn = sqlite3.connect(db_file)
            curs = conn.cursor()
            curs.execute('''CREATE TABLE installed
                            (integer item_id, text name, integer version_id, integer rating, integer is_installed''')
        else:
            conn = sqlite3.connect(db_file)
            curs = conn.cursor()
        finally:
            print("Moving Onward...")

    def sceaDwld(self):
            # the following ensures we get the latest game data files.
        gh = Github(tok)
        # get_repo does NOT like getting a variable as an argument.
        repo = gh.get_repo("aleph-one-marathon/alephone")
        tag_list = repo.get_tags()
        rel = tag_list[0].name
        for scen in ['Marathon','Marathon2','MarathonInfinity']:
            try:
                gam_check = Path("{}/scenarios/{}".format(basedir, scen))
            except FileNotFoundError:
                print("Games not detected...downloading")
                url = "https://github.com/{}/releases/download/{}/{}-{}-Data.zip".format(git_rep,rel,scen,rel.split('-')[1])
                http = Request.urlopen(url)
                zip = ZipFile(bio(http.read()))
                zip.extractall(path="{}/scenarios/.".format(basedir,scen))
            else:
                print("Trilogy detected....")
            finally:
                print("Moving Onward...")

tk.mainloop()

