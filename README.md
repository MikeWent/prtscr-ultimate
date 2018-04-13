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
EDITOR='pinta'
```

#### Supported editors

Common name and (`command`).

- Pinta (`pinta`): powerful and has an intuitive UI. Would recommend.
- Krita (`krita`): this one is more about drawing like a pro, but does screenshot editing well too.
- PhotoFlare (`PhotoFlare`): fast but has a bit non-intuitive UI.
- GIMP (`gimp`): no need to introduce. Powerful and old-known. Has a bit non-intuitive UI, even more than PhotoFlare. Also you need to "Export" pic, _not_ "Save" it to get autocopy working. Wouldn't recommend for fast editing. Choose another option if you can.
- Imeditor (`imeditor`): seems lightweight, but last time I used it was a piece of crap. Wouldn't recommend.
- any editor with command line syntax `editorname /path/to/file`

## License

MIT
