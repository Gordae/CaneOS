from colorama import *
from safemode import *
from commanmode import *



def fix():
    print('Welcome To The fixer of CaneOS')
    print('1 - Safe Mode')
    print('2 - command mode')

    while True:
        command = input('>')
        if command == "1":
            safe()
        if command == "2":
            comm()
