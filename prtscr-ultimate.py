#!/usr/bin/env python3

# PrtScr Ultimate
# https://github.com/MikeWent/prtscr-ultimate

BACKEND='gnome-screenshot'
EDITOR='pinta'

from os.path import expanduser
from random import choice
from time import sleep
from os import remove, path, stat
import subprocess
import argparse
import string
import time

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
parser.add_argument("-d", "--delay", help="set delay before taking a screenshot", type=int, default=0)
parser.add_argument("-o", "--output", help="output file to save screenshot", type=str, default=False, metavar="FILE")
parser.add_argument("-e", "--edit", help="open image editor after taking a screenshot", action="store_true")
parser.add_argument("--backend", help="select backend for action, overrides in-file variable", type=str, choices=['gnome-screenshot', 'scrot', 'spectacle'], default=BACKEND)
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
    except FileNotFoundError:
        pass

def debug(something_to_print):
    if options.debug:
        print(str(something_to_print))

def copy_png_to_clipboard(filepath):
    xclip_command = ['xclip', '-selection', 'clipboard', '-t', 'image/png', '-i', output_filename]
    debug(xclip_command)
    try:
        subprocess.run(xclip_command)
    except FileNotFoundError:
        print('Unable to copy screenshot to clipboard: "xclip" is not installed.')
        if not options.output:
            yn = input('Delete temporary screenshot file? ('+output_filename+') [Y/n]: ')
            if yn in ('', 'y', 'Y'):
                rm(output_filename)
            else:
                exit()

class FileWatchdog(object):
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        self.cached_stamp = stat(self.path_to_file).st_mtime

    def file_changed(self):
        stamp = stat(self.path_to_file).st_mtime
        if stamp != self.cached_stamp:
            # file changed
            self.cached_stamp = stamp
            return True
        else:
            return False

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
    command = ['scrot', '--silent']
    if options.cursor:
        command.append('--include-pointer')
    if options.selection:
        command.append('--select')
    if options.borders:
        command.append('--border')
    if options.window:
        command.append('--focused')

'''
    Spectacle backend
'''
if options.backend == 'spectacle':
    command = ['spectacle', '--background', '--nonotify']
    if options.cursor:
        command.append('--include-pointer')
    if options.selection:
        command.append('--region')
    if options.borders:
        command.append('--border')
    if options.window:
        command.append('--activewindow')
    if not options.window and not options.selection:
        command.append('--fullscreen')
    command.append('--output')

'''
    Delay if --dealy is set
'''
if options.delay > 0:
    n = options.delay
    while n > 0:
        print('Screenshot in ' + str(n) + ' seconds', end='\r')
        sleep(1)
        n -= 1
    print('\033[K' + ' '*20) # clear line

'''
    Use backend with prepared params
'''
if not options.output:
    output_filename = "/tmp/" + random_symbols() + '.png'
else:
    output_filename = time.strftime(options.output)
    # fix gnome-screenshot bug
    if output_filename[0] != "/":
        # save file to homedir
        output_filename = expanduser("~/") + output_filename

command.append(output_filename)
debug(command)

if options.debug:
    # don't mute output,
    # don't handle exceptions
    # don't show help messages
    subprocess.run(command)
else:
    try:
        # mute output and run
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        print('Backend "'+options.backend+'" is not installed. What you can do:')
        print('    - install it')
        print('    - change backend by editing BACKEND var in this script')
        print('    - temporary change backend with --backend option')
        exit(1)
    except AttributeError:
        # when using python3.4 subprocess.run raises
        # "AttributeError: module object has no attribute run"
        print('Installed Python is old, upgrade it to version 3.5')
        exit(1)

'''
    Copy file to clipboard
'''
# check if exists
if not path.exists(output_filename):
    print('No screenshot taken. Try running with --debug')
    exit(1)
copy_png_to_clipboard(output_filename)

'''
    Open image editor if set
'''
if options.edit:
    editor_command = [EDITOR, output_filename]
    debug(editor_command)
    if options.debug:
        editor_process = subprocess.Popen(editor_command)
    else:
        # mute output and run
        editor_process = subprocess.Popen(editor_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    screenshot_file = FileWatchdog(output_filename)
    # while editor is alive
    while editor_process.poll() == None:
        if screenshot_file.file_changed() == True:
            copy_png_to_clipboard(output_filename)
        time.sleep(0.2)

'''
    Remove temp file if -o/--output isn't set
'''
if not options.output:
    rm_command = ['rm', output_filename]
    subprocess.run(rm_command)
    debug(rm_command)
