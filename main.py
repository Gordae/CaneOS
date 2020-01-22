from colorama import *
from login import *
from Fixer import *
from activatekey import *
try:
    from CLWI import *
except ModuleNotFoundError:
    print('CLWI Is Not Working Cause You Need To Install CLWI.')
login()

print(Fore.LIGHTMAGENTA_EX + "Welcome To CaneOS 16!" + Fore.RESET)
print(Fore.LIGHTMAGENTA_EX + "Type help for a list of commands." + Fore.RESET)
print(Fore.LIGHTMAGENTA_EX + "Updates: Added Product Keys." + Fore.RESET)

while True:
    command = input(Fore.MAGENTA + ">")
    if command == "help":
        print('Here Is A List:')
        print('about - Tells You About This OS')
        print('web - The Internet')
        print('reboot - reboots')
        print('fix - starts fixer')
        print('Defend - CaneDefend')
        print('key - Activate CaneOS')
    if command == "web":
        print('Loading CLWI 8.0 Beta')
        web()
    if command == "about":
        print('OS: CaneOS 16.00')
        print('Build 1602')
    if command == "fix":
        fix()
    if command == "reboot":
        login()
    if command == "defend":
        print('Welcome to CaneDefend System, We Do Not See Any viruses in This OS Folder.')
    if command == "key":
        activate()