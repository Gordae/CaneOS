from colorama import *
from login import login

def safe():

    login()

    print(Fore.LIGHTMAGENTA_EX + "Welcome To CaneOS SafeMode" + Fore.RESET)
    print(Fore.LIGHTMAGENTA_EX + "Type help for a list of commands." + Fore.RESET)
    print(
        Fore.LIGHTMAGENTA_EX + "Updates: Now In Python. Added Fixer. Added Safe mode. added command mode" + Fore.RESET)

    while True:
        command = input(Fore.MAGENTA + ">")
        if command == "help":
            print('Here Is A List:')
            print('about - Tells You About This OS')
            print('web - The Internet')
            print('reboot - reboots')
        if command == "web":
            print(Fore.RED + "We Set This As Safemode Without WI-FI" + Fore.RESET)
        if command == "about":
            print('OS: CaneOS 16.00 Safe Mode')
            print('Build 1602 Safemode')
        if command == "reboot":
            login()
