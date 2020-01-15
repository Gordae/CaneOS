from colorama import *
from login import *
from Fixer import *
try:
    from CLWI import *
except ModuleNotFoundError:
    print('CLWI Is Not Working Cause You Need To Install CLWI.')
login()

print(Fore.LIGHTMAGENTA_EX + "Welcome To CaneOS 15!" + Fore.RESET)
print(Fore.LIGHTMAGENTA_EX + "Type help for a list of commands." + Fore.RESET)
print(Fore.LIGHTMAGENTA_EX + "Updates: Now In Python. Added Fixer. Added Safe mode. added command mode. added Defender app, Added CLWI (Web)" + Fore.RESET)

while True:
    command = input(Fore.MAGENTA + ">")
    if command == "help":
        print('Here Is A List:')
        print('about - Tells You About This OS')
        print('web - The Internet')
        print('reboot - reboots')
        print('fix - starts fixer')
        print('Defend - CaneDefend')
    if command == "web":
        print('Loading CLWI 7.0')
        web()
    if command == "about":
        print('OS: CaneOS 15.00')
        print('Update Number: 100890017')
    if command == "fix":
        fix()
    if command == "reboot":
        login()
    if command == "defend":
        print('Welcome to CaneDefend System, We Do Not See Any viruses in This OS Folder. You Are Good,')