import os
import re
import webbrowser
import subprocess
import datetime

os.system("title V.E.G.A")
os.system("mode 112, 35")
os.system("color 0A")
command = input("How may I help you? \n")
def get_path(command):
    a = os.popen('where " '+command).readlines()
    if a:
        return a
    b = os.popen('where /r \"\Program Files" ' +command).readlines()
    if b:
        return b
    c = os.popen('where /r ]"\Windows\WinSxS" '+command).readlines()
    if c:
        return c
    
def launch(command):
    try:
        path=get_path(command)
        path='"'+path[0].split('\n')[0]+'"'
        print("Launching " + path)
        os.startfile(path)
        print("If it didn't launch, don't blame me. It's your fault.")

    except:
        A=command[7:]
        print("Launching "+A)
        os.system(A)
        print("If it didn't launch, don't blame me. It's your fault.")
        
def volume():
    #Currently the volume settings work with the help of a third-party software named NirCmd by NirSoft(c). All Rights Reserved
    #So for controlling the volume, the user would have to install nircmd.exe (which is somewhat an inconvenience)
    #Also, two steps are required for setting the volume. This needs to be reduced to one step.
    volnum=int(input("Enter volume level: "))
    if volnum>-1 and volnum<101:
        temp=(volnum/100)*65535
        send= "nircmd.exe setsysvolume "+str(temp)
        os.system("nircmd.exe mutesysvolume 0")
        os.system(send)
        print(volnum*"|" + (100-volnum)*"-")
        print("Volume set at " + str(volnum) + "%")
        print("")
    else:
        print("Invalid volume level")
        volume()
def vega():
    if command == "control panel" or command=="Control Panel" or command=="Control panel":
        os.system("control panel")
    elif "help" in command:
        print("")
        print("######          #######    ####################          #####################         ###########")
        print("######         #######     ####################          #####################         ############")
        print("######        #######      ####################          #####################         #############")
        print("######       #######       #######                       #######                       ###### #######")
        print("######      #######        #######                       #######                       ######  #######")
        print("######     #######         ###############               #######                       ######   #######")
        print("######    #######          ###############               #######      ########         ######    #######")
        print("######   #######           ###############               #######         #####         ######     #######")
        print("######  #######            #######                       #######         #####         ######      #######")
        print("###### #######             #######                       #######         #####         ######       #######")
        print("#############              ####################          #####################         ######        #######")
        print("############    ####       ####################   ####   #####################   ####  ######         #######")
        print("###########     ####       ####################   ####   #####################   ####  ######          #######")
        print("")
        print("<insert V.E.G.A. descriptions here>")
        print("-------------------------------------------------------------")
        print("     <TYPE THIS>         ---         <AND YOU GET THIS>")
        print("-------------------------------------------------------------")
        print("help                     --- To open this help file (duh)")
        print("Control panel            --- To open control panel.")
        print("Terminal                 --- To open terminal")
        print("open <website.com>       --- To browse the mentioned website")
        print("launch <program.exe>     --- Searches through Windows directories and finds the program's exe file to open")
        print("hello                    --- V.E.G.A. ask your name")
        print("music                    --- Opens your Music Folder")
        print("time                     --- Shows the current time")
        print("date                     --- Shows the current date and day")
        print("clear                    --- To clear the screen")
        print("shutdown                 --- Shuts down the system")
        print("exit or bye              --- To quit V.E.G.A.")
        print("")
    elif "terminal" in command:
        print("Which terminal do you want?")
        print("Python terminal or Command Prompt?")
        x = input()
        if "python" in x or "Python" in x or "PYTHON" in x:
            os.system("python")
        elif "cmd" in x or "CMD" in x or "Command Prompt" in x or "command prompt" in x or "COMMAND PROMPT" in x:
            os.system("cmd")
    elif "open" in command:
        website=re.search("open (.+)", command)
        if website:
            domain=website.group(1)
            print ("Opening " + domain + ", sir\n")
            url="https://www." + domain
            webbrowser.open(url)
    elif "launch" in command:
        launch(command)
    elif "hello" in command:
        print ("Hi, there. The name's V.E.G.A. What's yours?")
        name = input()
        print("Hi, " + name)
    elif "music" in command or "Music" in command:
        print ("Ok, I will open the Music folder for you")
        os.system("cd %userprofile%/Music && start .")
    elif "time" in command:
        x=datetime.datetime.now()
        print(x.hour, ":", x.minute, ":", x.second, sep="")
    elif "date" in command:
        x=datetime.datetime.now()
        print(x.strftime("%d"), x.strftime("%m"), x.strftime("%Y"), ",", x.strftime("%A"))
    elif "volume" in command:
        volume()
    elif "clear" in command:
        os.system("cls")
    elif "shutdown" in command:
        os.system("shutdown /h")
    elif "exit" in command:
        exit()
    else:
        print("Sorry. Invalid command.")
while command != "bye":
    vega()
    command=input("How else may I help you? \n")

