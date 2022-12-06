#   About:

#   This is an enumeration tool built for the purpose of combining tools I have written into a single command line interface.  I am aiming to make it as easy as possible to
#   add more  functionality as I learn and progress.  This entire project was started to learn how to implement the tools I have learned from Kali
#   with my python skills.  Inspired by David Bombal and Network Chuck and their advice to not be a script kiddie.
#   This sort of becomes a pseudo shell also, which inspired me to write a version that can be deployed once access is gained... thats next.. maybe

#   Author:      Jeff Schowe----Github: unfondoffondu-----E-mail jaschowe@gmail.com

#   Disclaimer:  This is made for educational purposes only and meant for use in a lab environment against willing targets.  The Author takes no
#                responsibility for how this is used.  Use at your own risk.

#   License:     Feel free to use it and modify and make it your own, redistribute it.

#   Bugs:        I am sure there are a lot of them.  Please report to me any you find, and I would *LOVE* any feedback at all.  The service
#                detection feature isn't necessarily accurate, and goes by common uses of the port in question.  I need to do more research
#                into the output of my connection to try to be more accurate and gather more information.  This is just a start.
import pydiscover
import pymap
import pybuster
from clr import clr as clr
import time
import os
from random import choice as choice

# add functions here

def bash(cmd):
    os.system(cmd)
    engine(returns)
def col(letters):
    colors = ["30","31","32","33","34","35", "36"]
    prompt = f"\033[1;{choice(colors)};40m"
    for i in letters:
        color = choice(colors)
        c = f"\033[1;{color};40m"
        prompt = prompt + f"{i}{c}"
    return prompt
def pyre():
    w = time.sleep(.01)
    prompt = col("<pyRe> ")
    inpt = input(f"{prompt}\033[0;0m")
    if "^" in inpt:
        pyre()
    return inpt
def helps(): # add help entry here
    print(col(f"\n?: display commands\nclr: clear screen\nx: exit\nv: view knowledge base\nr: reset knowledge base\n1: scan local network\n2: scan ports\n3: directory bruteforce\nTo run a shell command just add - to the beggnning like -ls -la\n"))
    engine(returns)
def view(returns):
    if len(returns) > 0:
        print(returns)
    else:
        print(col("!pyre! no knowledge base yet."))
        engine(returns)
def clear():
    print(col("pyre: deleting the knowledge base will delete the knoledge base, are you sure? y/n"))
    sure = pyre()
    if sure == "y":
        returns = []
        engine(returns)
    else:
        engine(returns)
def exit_nice():
    print(col("have a nice day."))
    exit()
def do_pydiscover():
    print(col(f"pyro: expect first 3 octets of subnets you wish to scan ---.---.---."))                 #  FIX THIS
    host = pyre()
    scan = pydiscover.scan(host)
    returns.append(("pydiscover", scan))
    engine(returns)
def do_pymap():

    if len(returns) > 0:
        print(col(f"1: read from hosts 2: enter host 3: return to menu"))
        inpt = pyre()
        if inpt == "1":
            for i in returns:
                if "pydiscover" in i:
                    hosts = i[1]
                else:
                    print(col("pyro: have you scanned your network?  returning to main menu..."))
                    engine(returns)
                print(col(f"pick a target: \n {hosts}"))
                target = pyre()
                map = pymap.scan(target)
                returns.append(("network_map", map))
                engine(returns)
    if inpt == "2":
        print(col("enter host"))
        host = pyre()
        map = pymap.scan(host)
        returns.append(("net_map", map))
        engine(returns)
    elif inpt == "3":
        engine(returns)
    else:
        print(col("enter a target ip or domain"))
        target = pyre()
        map = pymap.scan(target)
        returns.append(("network_map", map))
        engine(returns)
def do_pybuster():
    print(col("enter target"))
    target = pyre()
    print(col("request delay 0-5?"))
    scan_timer = float(pyre())
    dirs = pybuster.scan(target, scan_timer)
    returns.append(("pybuster", dirs))
    engine(returns)

def engine(returns):

    inpt = pyre()
    if inpt == "":
        engine(returns)
    if inpt in ["?","h","help","Help","wtf"]:
        helps()
    if inpt[0] == "-":
        bash(inpt.lstrip("-"))
    if inpt == "x":
        exit_nice()
    if inpt == "rm":
        clear()
    if inpt == "v":
        view(returns)
    if inpt == "1":   # pydiscover
        do_pydiscover()
    if inpt == "2":   # pymap
        do_pymap()
    if inpt == "3":
        do_pybuster()
# add function call conditions here
    else:
        engine(returns)

returns = []
print(col("welcome to pyRecon"))
clr()

def main():
    try:
        knowledge = engine(returns)
    except RecursionError:
        main()
    except KeyboardInterrupt:
        print(col("\nYou want to leave?"))
        inpt = pyre()
        if inpt in ['quit','y','yes','leave','exit']:
            print(col("smell ya later."))
            exit()
        else:
            engine(returns)
if __name__ == "__main__":
    main()
