# PrtScr Ultimate

Script that can connect screenshot tools to xclip.

## Usage
```
usage: prtscr-ultimate.py [-h] [-s | -f | -w] [-b] [-c]
                          [--backend {gnome-screenshot,scrot}] [--debug]

optional arguments:
  -h, --help            show this help message and exit
  -s, --selection       select area manually
  -f, --fullscreen      grab the entire screen
  -w, --window          grab only active window
  -b, --borders         include window borders, works only with --window
  -c, --cursor          include mouse cursor
  --backend {gnome-screenshot,scrot}
                        select backend for action, overrides in-file variable
  --debug               don't use this option
```

## Available backends

- gnome-screenshot (recommended)
- scrot

## Unsupported backends

- xfce4-screenshooter


## License

GPLv3