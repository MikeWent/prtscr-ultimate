#!/usr/bin/env python3

'''
    Available backends:
    - scrot
    - gnome-screenshot (recommended due to stability)

    Unsupported backends:
    - xfce4-screenshooter (doesn't have saving to file option, only to folder)

    Can be overrided with --backend option
'''
BACKEND='gnome-screenshot'

from random import choice
from time import strftime
from os import remove
import subprocess
import argparse
import string

'''
    Args parser
'''
parser = argparse.ArgumentParser()
group_global = parser.add_mutually_exclusive_group()
group_global.add_argument("-s", "--selection", help="select area manually", action="store_true")
group_global.add_argument("-f", "--fullscreen", help="grab the entire screen", action="store_true")
group_global.add_argument("-w", "--window", help="grab only active window", action="store_true")
parser.add_argument("-b", "--borders", help="include window borders, works only with --window", action="store_true")
parser.add_argument("-c", "--cursor", help="include mouse cursor", action="store_true")
parser.add_argument("--backend", help="select backend for action, overrides in-file variable", type=str, choices=['gnome-screenshot', 'scrot'], default=BACKEND)
parser.add_argument("--debug", help="don't use this option", action="store_true", default=False)
options = parser.parse_args()

'''
    Functions and abstractions
'''

def random_symbols(length=10):
    alphabet = string.ascii_letters + string.digits
    return ''.join([choice(alphabet) for _ in range(length)])

def rm(filename):
    try:
        remove(filename)
    except:
        pass

'''
    Gnome Screenshot backend
'''
if options.backend == 'gnome-screenshot':
    command = ['gnome-screenshot']
    if options.cursor:
        command.append('--include-pointer')
    if options.selection:
        command.append('--area')
    if options.borders:
        command.append('--include-border')
    else:
        command.append('--remove-border')
    if options.window:
        command.append('--window')
    
    command.append('-f')

'''
    Scrot backend
'''
if options.backend == 'scrot':
    command = ['scrot', '--silent --quality 100']
    if options.cursor:
        command.append('--include-pointer')
    if options.selection:
        command.append('--select')
    if options.borders:
        command.append('--border')
    if options.window:
        command.append('--focused')

'''
    Use backend with prepared params
'''
temp_filename = random_symbols() + '.png'
command.append(temp_filename)
if options.debug:
    code = subprocess.run(command).returncode
else:
    # mute output
    code = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode

if options.debug:
    print('Debug:', command)
    print('Debug:', 'backend exit code', code)

'''
    Copy file to clipboard and delete it
'''
xclip_command = ['xclip', '-selection', 'clipboard', '-t', 'image/png', '-i', temp_filename]
code = subprocess.run(xclip_command).returncode
if options.debug:
    print('Debug:', xclip_command)
    print('Debug:', 'xclip exit code', code)

code = subprocess.run(['rm', temp_filename]).returncode
if options.debug:
    print('Debug:', 'rm exit code', code)
