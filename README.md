# PrtScr Ultimate

Lightweight python script that provides single command line interface for different screenshot tools.

It makes screenshot, copies it to clipboard and deletes temporary screenshot file (optionally can save screenshot to file). Works everywhere, with any DE and even without it (for example with i3).

## Usage

```
usage: prtscr-ultimate.py [-h] [-s | -f | -w] [-b] [-c] [-d DELAY] [-o FILE]
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
  -o FILE, --output FILE
                        output file to save screenshot
  --backend {gnome-screenshot,scrot,spectacle}
                        select backend for action, overrides in-file variable
  --debug               don't use this option
```

### Useful tip

`-o/--output` option supports Python [time.strftime](http://strftime.org/), for example `--output "screenshot-%Y.%m.%d-%H:%M:%S.png"` will produce `screenshot-2018.04.08-21:48:58.png`.

## Installation

### Available backends

- gnome-screenshot (**recommended**)
- spectacle (kde-spectacle)
- scrot

### Install software

`<backend>` is one of the available backends

Ubuntu: `sudo apt install git python3 xclip <backend>`

Arch Linux: `sudo pacman -S git python xclip <backend>`

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

MIT
