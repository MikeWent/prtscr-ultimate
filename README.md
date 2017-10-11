# PrtScr Ultimate

Script that can connect screenshot tools to xclip.

## Usage

```
usage: prtscr-ultimate.py [-h] [-s | -f | -w] [-b] [-c] [-d DELAY]
                          [--backend {gnome-screenshot,scrot,spectacle}]
                          [--debug]

optional arguments:
  -h, --help            show this help message and exit
  -s, --selection       select area manually
  -f, --fullscreen      grab the entire screen
  -w, --window          grab only active window
  -b, --borders         include window borders, works only with --window
  -c, --cursor          include mouse cursor
  -d DELAY, --delay DELAY
                        set delay before screenshot
  --backend {gnome-screenshot,scrot,spectacle}
                        select backend for action, overrides in-file variable
  --debug               don't use this option
```

## Available backends

- gnome-screenshot (recommended)
- spectacle
- scrot

## Installation

### Install software

`<backend>` is one of the available backends

```sh
sudo apt install git xclip <backend>
```

### Clone repo

```sh
git clone git@github.com:MikeWent/prtscr-ultimate.git
cd prtscr-ultimate
```

### Edit backend

```sh
nano ./prtscr-ultimate.py
```

Find var `BACKEND` and set your installed backend

Example:

```python3
BACKEND='gnome-screenshot'
```

## Unsupported backends

- xfce4-screenshooter

## License

GPLv3