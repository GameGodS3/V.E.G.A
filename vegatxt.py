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
def launch(command):
    try:
        path=get_path(command)
        path='"'+path[0].split('\n')[0]+'"'
        print("Launching " + path)
        os.startfile(path)
        print("If it didn't launch, don't blame me. It's your fault.")
  #  except AttributeError:
       # print("Attribute Error, check code again.")
    except:
        A=command[7:]
        print("Launching "+A)
        os.system(A)
        print("If it didn't launch, don't blame me. It's your fault.")
        

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

    elif "launch" in command:
        launch(command)

while command != "bye":
    vega()
    command=input("How else may I help you? \n")

