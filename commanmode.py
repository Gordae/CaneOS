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
    print('WELCOME TO CANEOS13 COMMAND MODE')

    while True:
        command = input(Fore.MAGENTA + ">")
        if command == "help":
            print('Here Is A List:')
            print('about - Tells You About This OS')
            print('web - The Internet')
            print('reboot - reboots')
        if command == "web":
            print(Fore.RED + "WARNING: This Program Can Harm Your PC." + Fore.RESET)
        if command == "about":
            print('OS: CaneOS 13.02')
            print('Update Number: 139064281')
        if command == "reboot":
            login()