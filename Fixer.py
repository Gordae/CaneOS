from colorama import *
import safemode
import commanmode



def fix():
    print('Welcome To The fixer of Caneos13')
    print('1 - Safe Mode')
    print('2 - command mode')

    while True:
        command = input('>')
        if command == "1":
            safe()
        if command == "2":
            comm()