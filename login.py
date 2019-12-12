from colorama import *


def login():
    command = input('Password:')
    if command == 'ilovecaneos':
        print('logging in...')

    else:
        login()