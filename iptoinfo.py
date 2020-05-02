#!/usr/bin/python3
# -*- coding: utf-8 -*-


from src.IPtoGeoInfo import Detective
from src.logger import Logger
from time import sleep
from colorama import Fore, init
from sys import platform, argv
from os import system


__author__ = 'rady'
name = Fore.RED + '\n----IP To Info Detective----\n'
clear = 'clear'
help = Fore.YELLOW + '''-h   ---   that text.
-t *IP*   ---   info about ip.   
'''

if platform == 'win32':
    init()
    clear = 'cls'

def main():
    if len(argv) == 1:
        system(clear)
        print(name)
        ip = input(Fore.YELLOW + '[*] Enter IP: ')
        sleep(1)

    elif len(argv) == 2 and argv[1] == '-h':
        print(name)
        print(help)
        print(Fore.WHITE)
        exit(1)
        
    elif len(argv) == 3 and argv[1] == '-t':
        system(clear)
        print(name)
        ip = argv[2]
        print(Fore.YELLOW + '[*] IP: ' + ip)
        sleep(1)

    else:
        print(name)
        print(help)
        print(Fore.WHITE)
        exit(1)
        
    system(clear)
    print(name)
    ipinfo = Detective(ip)
    json = ipinfo.get_json()

    if 'error' in json:
        print(Fore.RED + '[!] ERROR: Wrong IP!')
        exit(1)
        
    ipinfo.json_edit(json)
    var_list = ipinfo.return_all_var()

    print(Fore.YELLOW + 'IP:', Fore.GREEN + var_list[0])
    print(Fore.YELLOW + 'Country:', Fore.GREEN + var_list[1])
    print(Fore.YELLOW + 'Region:', Fore.GREEN + var_list[2])
    print(Fore.YELLOW + 'City:', Fore.GREEN + var_list[3])
    print(Fore.YELLOW + 'Time Zone:', Fore.GREEN + var_list[4])
    print(Fore.YELLOW + 'Zip Code:', Fore.GREEN + var_list[5])
    print(Fore.YELLOW + 'Organization:', Fore.GREEN + var_list[6])
    print(Fore.YELLOW + 'Location:', Fore.GREEN + var_list[7])
    print(Fore.YELLOW + 'Host Name:', Fore.GREEN + var_list[8])
    print(Fore.WHITE)

    log = Logger()
    log.save_log(var_list)


main()