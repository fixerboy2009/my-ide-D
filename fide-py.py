# F-IDE V1-PY
import http
import time
import sys
import os
import http.client
# Imports in comments are either bugged or non-working
from colorama import Fore, Back, Style
from playsound import playsound

def resetAll():
    print(Style.RESET_ALL)

def playSound(soundFile):
    playsound(soundFile)

# How to make more?
# Format: "varname": value
varsToPass = {"wait": time.sleep, "os": os, "time": time, "httpclient": http.client, "sys": sys, "CF": Fore, "CB": Back, "CS": Style, "reset": resetAll, "playSound": playSound}

os.chdir("C:/Users/fixer/Downloads/new thing/FIDE/fs")
first = True
latestScript = 0
mode = open("C:/Users/fixer/Downloads/new thing/FIDE/defaults/dm", 'r').read()
wmsg = open("C:/Users/fixer/Downloads/new thing/FIDE/defaults/welcomemsg", 'r').read()
ver = "F-IDE V1-PY"

def setDefault(default):
    file = open("C:/Users/fixer/Downloads/new thing/FIDE/defaults/dm", 'w')
    file.truncate()
    file.write(default)
    file.close()

firstNew = os.path.exists("C:/Users/fixer/Downloads/new thing/FIDE/defaults/first")

if firstNew == True:
    os.remove("C:/Users/fixer/Downloads/new thing/FIDE/defaults/first")
    print(wmsg)

def execute(cmd):
    os.system(cmd)

execute("cls")

def info():
    print("INFO: ")
    print("F-IDE (Fixer-IDE) is a IDE that focuses on the simplest eviroment ever. Created in python. Made in less then 200 lines.")

def changeMode(nmode):
    mode = nmode

def otherLang(scr, lang):
    if lang == "lua":
        print("Executing in lua...")
        file = open("luaexec.lua", 'w')
        file.write(scr)
        print("Writtin to file.")
        execute("C:\Windows\System32\cmd.exe lua ../luaexec.lua")
        file.close()
        # os.remove("luaexec.lua")

    if lang == "file":
        print("Loading file data......")
        loaded = open(scr, 'r')
        print("Loaded, reading and printing data.....")
        data = loaded.readlines()
        print(str(data))

    if lang == "http":
        url = scr
        got = http.client.HTTPConnection(url)
        print(got.request("GET", url))

    if lang == "batch":
        cmd = scr
        exe = os.system
        print("Executing batch......")
        exe(cmd)

def stop():
    sys.exit()

def wait(sec): # lol stop decompiling
    time.sleep(sec)

def runScript(scr):
    if scr == "exit":
        print("Exiting...")
        stop()
    print("Executing script.....")
    wait(2)
    exec(scr, varsToPass)
    print("Executed!")

def init():
    global mode
    print("To exit (with out closing cmd), type exit. To change languages/modes, type mode [lang] to change. Type info to get info about this IDE.")
    typed = input("[ " +  mode.upper() + " ]: ")
    if "mode" in typed:
        if typed == "mode lua":
            mode = "lua"
            print("Changed mode to lua")

        if typed == "mode python":
            mode = "python"
            print( Fore.GREEN +  "Changed mode to python" + Style.RESET_ALL)

        if typed == "mode py":
            mode = "python"
            print( Fore.GREEN + "Changed mode to python" + Style.RESET_ALL)

        if typed == "mode cs":
            mode = "c#"
            print( Fore.GREEN + "Changed mode to C#" + Style.RESET_ALL)

        if typed == "mode c#":
            mode = "c#"
            print( Fore.GREEN + "Changed mode to c#" + Style.RESET_ALL)

        if typed == "mode web":
            print( Fore.RED + "Can't change mode to HTTP, HTTP is currently disabled due to bugs in the code. Sorry!" + Style.RESET_ALL)

        if typed == "mode file":
            mode = "file"
            print( Fore.GREEN + "Changed mode to file" + Style.RESET_ALL)

        if typed == "mode batch":
            mode = "batch"
            print( Fore.GREEN + "Changed mode to batch" + Style.RESET_ALL)

        if typed == "mode audio-preset":
            mode = "audio-preset"
            print( Fore.GREEN + "Changed mode to audio-preset, presets: bad apple" + Style.RESET_ALL)
    else:
        if typed == "info":
            info()
        else:
            if mode == "python":
                runScript(typed)
            if mode != "python":
                otherLang(typed, mode)
    init()

init()