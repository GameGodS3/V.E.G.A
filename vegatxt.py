import os
import re
import webbrowser
import subprocess

command = input("How may I help you? \n")

def get_path(command):
    a = os.popen('where " '+command).readlines()
    if a:
        return a
    b = os.popen('where /r \"\Program Files" ' +command).readlines()
    if b:
        return b
    c = os.popen('where /r ]"\Program Files (x86)" '+command).readlines()
    if c:
        return c

def vega():
    if command == "control panel" or command=="Control Panel" or command=="Control panel":
        os.system("control panel")

    elif "open" in command:
        website=re.search("open (.+)", command)
        if website:
            domain=website.group(1)
            print ("Opening " + domain + ", sir\n")
            url="https://www." + domain
            webbrowser.open(url)
            
    elif "run" in command:
        #os.system("explorer.exe Shell:::{2559a1f3-21d7-11d4-bdaf-00c04f60b9f0}")
        subprocess.run("wmplayer.exe")

    elif "launch" in command:
        path=get_path(command)
        path='"'+path[0].split('\n')[0]+'"'
        os.startfile(path)

while command != "bye":
    vega()
    command=input("How else may I help you? \n")
