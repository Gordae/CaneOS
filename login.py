from colorama import *


def login():
    command = input('Password:')
    if command == 'ilovecaneos':
        print('logging in...')

    else:
        print(Fore.RED + "Wrong Password. Please Try Again." + Fore.RESET)
        login()