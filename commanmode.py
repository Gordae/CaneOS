from colorama import *
from login import login



def comm():
    print('loading Cpu Cores...')
    print('loading commands...')
    print('loaded System/HARDWARE/MOTHERBOARD/CPU/CORE')
    print('loaded System/HARDWARE/STORAGE/SSD/C:/PROGRAMFILES/GORDAE/CANEOS/LOGIN')
    print('TO CONTINUE, TYPE PASSWORD')

    login()

    print('GRANTED')
    print('DONE')
    print('WELCOME TO CANEOS COMMAND MODE')

    while True:
        command = input(Fore.MAGENTA + ">")
        if command == "help":
            print('Here Is A List:')
            print('about - Tells You About This OS')
            print('web - The Internet')
            print('reboot - reboots')
        if command == "web":
            print(Fore.RED + "CLWI Can't Load On Command Mode." + Fore.RESET)
        if command == "about":
            print('OS: CaneOS 16.00')
            print('Build 1602 COMMAND')
        if command == "reboot":
            login()
