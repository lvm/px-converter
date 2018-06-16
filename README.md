# Pixel Converter

Small tool to convert from / to pixels.

## Install

`$ wget https://raw.githubusercontent.com/lvm/px-converter/master/pxc.py`


## Module Usage

```
$ python3
>>> import pxc
>>> pxc.to_pixel(12, 300)
1417
pxc.to_centimeter(1417, 300)
12
```

## CLI Usage

```
usage: pxc.py [-h] [-d DPI] [-tp TO_PIXEL] [-tc TO_CENTIMETER]

optional arguments:
  -h, --help            show this help message and exit
  -d DPI, --dpi DPI     DPI. default: 300
  -tp TO_PIXEL, --to-pixel TO_PIXEL
  -tc TO_CENTIMETER, --to-centimeter TO_CENTIMETER
```

## LICENSE

See `pxc.py`
