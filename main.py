import os,platform
os.system('git pull')
os.system("clear")
crk=platform.architecture()[0]
if crk=="32bit":
    __import__("file32")
elif crk=="64bit":
    __import__("file64")
