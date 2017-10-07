#!/usr/bin/env python3

'''
    Available backends:
    - scrot
    - gnome-screenshot (recommended due to stability)

    Can be overrided with --backend option
'''
BACKEND='gnome-screenshot'

from random import choice
from time import strftime
from os import system \
                    as sh # increase readability
import argparse

parser = argparse.ArgumentParser()
group_global = parser.add_mutually_exclusive_group()
group_global.add_argument("-s", "--selection", help="select area manually", action="store_true")
group_global.add_argument("-f", "--fullscreen", help="grab the entire screen", action="store_true")
group_global.add_argument("-w", "--window", help="grab only active window", action="store_true")

parser.add_argument("-b", "--borders", help="include window borders, use only with --window", action="store_true")
parser.add_argument("-c", "--cursor", help="include mouse cursor", action="store_true")

parser.add_argument("--backend", help="select backend for action, overrides in-file variable", type=str, choices=['gnome-screenshot', 'scrot'], default=BACKEND)
parser.add_argument("--debug", help="don't use this option", action="store_true", default=False)
args = parser.parse_args()
