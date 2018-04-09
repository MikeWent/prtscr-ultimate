# PrtScr Ultimate

Lightweight python script that provides single command line interface for different screenshot tools.

It makes a screenshot, copies it to clipboard and deletes temporary screenshot file (optionally can save screenshot to file). Screenshot can be edited "in place" via any supported picture editor (and unsupported too, see below). Works everywhere, with any DE and even without it (for example with i3).

## Usage

```
usage: prtscr-ultimate.py [-h] [-s | -f | -w] [-b] [-c] [-d DELAY] [-o FILE]
                          [-e] [--backend {gnome-screenshot,scrot,spectacle}]
                          [--debug]

optional arguments:
  -h, --help            show this help message and exit
  -s, --selection       select area manually
  -f, --fullscreen      grab the entire screen
  -w, --window          grab only active window
  -b, --borders         include window borders, works only with --window
  -c, --cursor          include mouse cursor
  -d DELAY, --delay DELAY
                        set delay before taking a screenshot
  -o FILE, --output FILE
                        output file to save screenshot
  -e, --edit            open image editor after taking a screenshot
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

### Unsupported backends

- xfce4-screenshooter

### Install software

`<backend>` is one of the available backends

Ubuntu: `sudo apt install git python3 xclip <backend>`

Arch Linux: `sudo pacman -S git python xclip <backend>`

### Clone repo

```sh
git clone git@github.com:MikeWent/prtscr-ultimate.git
cd prtscr-ultimate
```

### Set backend

Open `prtscr-ultimate.py` in text editor, find var `BACKEND` and set your installed backend

Example:

```python3
BACKEND='gnome-screenshot'
```

### Set editor (optionally)

See inctruction above

```python3
EDITOR='PhotoFlare'
```

#### Supported editors

- PhotoFlare
- gimp
- imeditor
- any editor with command line syntax `editorname /path/to/file`

## License

MIT
