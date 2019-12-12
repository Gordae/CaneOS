from colorama import *
from login import login
import Fixer

login()

print(Fore.LIGHTMAGENTA_EX + "Welcome To CaneOS 14!" + Fore.RESET)
print(Fore.LIGHTMAGENTA_EX + "Type help for a list of commands." + Fore.RESET)
print(Fore.LIGHTMAGENTA_EX + "Updates: Now In Python. Added Fixer. Added Safe mode. added command mode" + Fore.RESET)

while True:
    command = input(Fore.MAGENTA + ">")
    if command == "help":
        print('Here Is A List:')
        print('about - Tells You About This OS')
        print('web - The Internet')
        print('reboot - reboots')
        print('fix - starts fixer')
    if command == "web":
        print(Fore.RED + "WARNING: This Program Can Harm Your PC." + Fore.RESET)
    if command == "about":
        print('OS: CaneOS 14.00')
        print('Update Number: 1020780000')
    if command == "fix":
        fix()
    if command == "reboot":
        login()
