import os
import shutil
import time
import sys

t1 = time.time()
##config
## if you want to change the installation directories, edit the mdir and cdir variables. mdir is the folder to install path, cdir is the civ13 game path to create.
mdir = os.path.dirname(os.path.abspath(__file__))
cdir = "dd-BYONDTOOLS" #name of the directory this script is ran from
byond_version_major = sys.argv[1]
byond_version_minor = sys.argv[2]
####
####

print{"Installing BYOND for Linux..."}
print("Installing dependencies...")
os.system("sudo apt update")
os.system("sudo apt install make git unzip python3 python3-pip lib32z1 lib32ncurses5 libc6-i386 lib32stdc++6")
os.system("sudo apt autoremove")
os.system("sudo apt autoclean")
print("Installing Programs...")
exists = os.path.isfile(os.path.join(mdir,cdir,byond_version_major,".",byond_version_minor,"_byond_linux.zip"))
if not exists:
	os.system("sudo wget http://www.byond.com/download/build/{}/{}.{}_byond_linux.zip".format(byond_version_major,byond_version_major,byond_version_minor))
os.system("unzip {}.{}_byond_linux.zip".format(byond_version_major,byond_version_minor))
os.system("sudo mkdir /usr/share/man/man6")
os.system("make install -C byond")
print("Finished installing newest BYOND in {} seconds".format(t2))