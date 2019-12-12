from colorama import *
from login import login

def safe():

    login()

    print(Fore.LIGHTMAGENTA_EX + "Welcome To CaneOS 14 SafeMode" + Fore.RESET)
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
            print(Fore.RED + "WARNING: This Program Can Harm Your PC Even In Safe Mode." + Fore.RESET)
        if command == "about":
            print('OS: CaneOS 13.02 Safe Mode')
            print('Update Number: 139064281')
        if command == "reboot":
            login()
