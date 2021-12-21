# F-IDE V1-PY
import http
import time
import sys
import os
import http.client
import json
import colorama
import requests
# Imports in comments are either bugged or non-working
from colorama import Fore, Back, Style
from playsound import playsound

os.system("cls")

deps = {
    "conf": {
        "Theme": {
        "Foreground": colorama.Fore.WHITE,
        "Background": colorama.Back.BLACK,
        "ErrorColor": colorama.Fore.RED,
        "SuccessColor": colorama.Fore.GREEN,
    },
    "AutoExec": "print('autoexectest')",
    "IsDevelopmentVersion": True,
    "TempPath": "C:/Users/fixer/Downloads/new thing/FIDE/fs/tmp/",
    }
}

isDevEnv = deps["conf"]["IsDevelopmentVersion"]

if isDevEnv == True:
    print(Fore.YELLOW + "WARNING: Current version is in the development stage, you may come accross bugs on the way." + Fore.RESET)

print(Fore.CYAN + "Merry Christmas! Be Good!" + Fore.RESET)

def resetAll():
    print(Style.RESET_ALL)

def playSound(soundFile):
    playsound(soundFile)

def resetFore():
    Fore.WHITE

def pastebinRaw(pid):
    url = "https://pastebin.com/raw/" + pid + "/"
    responce = requests.get(url)
    return responce.text

def downloadImage(imgurl, name):
    print("Downloading image.")
    r = requests.get(imgurl)
    with open(name + ".png", 'wb') as f:
        f.write(r.content)
        print("Downloaded image! Path: fs/" + name + ".png")

def downloadSource(url, name):
    fullName = name + ".txt"
    print("Downloading URL Source......")
    r = requests.get(url)
    with open(fullName, 'w', encoding="utf-8") as f:
        f.write(str(r.text))
        print("Downloaded!")

def getNetworkInfo():
    response = requests.get("https://httpbin.org/ip")
    return "{0}".format(response.json()['origin'])

# How to make more?
# Format: "varname": value
varsToPass = {"wait": time.sleep, "os": os, "time": time, "httpclient": http.client, "sys": sys, "CF": Fore, "CB": Back, "CS": Style, "reset": resetAll, "playSound": playSound, 'networkInfo': getNetworkInfo, "pastebin": pastebinRaw, "imgdown": downloadImage, "srcdown": downloadSource}

os.chdir("C:/Users/fixer/Downloads/new thing/FIDE/fs")
first = True
latestScript = 0
mode = open("C:/Users/fixer/Downloads/new thing/FIDE/defaults/lastmode", 'r').read()
wmsg = open("C:/Users/fixer/Downloads/new thing/FIDE/defaults/welcomemsg", 'r').read()
ver = "F-IDE V1-PY"

# autorun handler
autorunData = open("C:/Users/fixer/Downloads/new thing/FIDE/defaults/autoexec", 'r').read()
exec(autorunData)

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

def info():
    print("INFO: ")
    print("F-IDE (Fixer-IDE) is a IDE that focuses on the simplest eviroment ever. Created in python. Made in less then 200 lines.")

def changeMode(nmode):
    mode = nmode
    file = open("C:/Users/fixer/Downloads/new thing/FIDE/defaults/lastmode", "w")
    file.truncate()
    file.write(nmode)

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
    open("C:/Users/fixer/Downloads/new thing/FIDE/defaults/scriptsExecuted", 'w').write(scr + "\n")
    print("Executed!")

def init():
    global mode
    print("To exit (with out closing cmd), type exit. To change languages/modes, type mode [lang] to change. Type info to get info about this IDE.")
    typed = input("[ " +  mode.upper() + " ]: ")
    if "mode" in typed:
        if typed == "mode lua":
            mode = "lua"
            changeMode("lua")
            print("Changed mode to lua")

        if typed == "mode python":
            mode = "python"
            changeMode("python")
            print( Fore.GREEN +  "Changed mode to python")
            resetFore()

        if typed == "mode py":
            mode = "python"
            changeMode("python")
            print( Fore.GREEN + "Changed mode to python")
            resetFore()

        if typed == "mode cs":
            mode = "c#"
            changeMode("c#")
            print( Fore.GREEN + "Changed mode to C#")
            resetFore()

        if typed == "mode c#":
            mode = "c#"
            changeMode("c#")
            print( Fore.GREEN + "Changed mode to c#")
            resetFore()

        if typed == "mode web":
            print( Fore.RED + "Can't change mode to HTTP, HTTP is currently disabled due to bugs in the code. Sorry!")
            resetFore()

        if typed == "mode file":
            mode = "file"
            changeMode("file")
            print( Fore.GREEN + "Changed mode to file")
            resetFore()

        if typed == "mode batch":
            mode = "batch"
            changeMode("batch")
            print( Fore.GREEN + "Changed mode to batch")
            resetFore()

        if typed == "mode audio-preset":
            mode = "audio-preset"
            changeMode("audio-preset")
            print( Fore.GREEN + "Changed mode to audio-preset, presets: bad apple")
            resetFore()
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
