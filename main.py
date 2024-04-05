import os,platform
os.system('git pull')
os.system("clear")
crack=platform.architecture()[0]
if crack=="32bit":
    __import__("file32")
elif crack=="64bit":
    __import__("file64")
