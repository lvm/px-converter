#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pxc.py - Pixel converter.
License: BSD 3-Clause
Copyright (c) 2018, Mauro L; <mauro@sdf.org>
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:
1. Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its
contributors may be used to endorse or promote products derived from
this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

__author__ = 'Mauro L.'
__version__ = '0.01'
__license__ = 'BSD3'

import re
import sys
import math
import argparse

DOT_PER_INCH = 25.4 # an Inch.


def to_pixel(value, dpi):
    return int(round((float(value) * 10 * dpi) / DOT_PER_INCH))


def to_centimeter(value, dpi):
    return round((float(value) / 10 * DOT_PER_INCH) / dpi)


def pixel(cm, dpi):
    return map(lambda c: to_pixel(c, dpi),
               cm.split(","))


def centimeter(px, dpi):
    return map(lambda p: to_centimeter(p, dpi),
               px.split(","))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-d', '--dpi',
                        type=int,
                        default=300,
                        help="DPI. default: 300")
    parser.add_argument('-tp', '--to-pixel',
                        type=str,
                        help=pixel.__doc__)

    parser.add_argument('-tc', '--to-centimeter',
                        type=str,
                        help=centimeter.__doc__)

    args = parser.parse_args()
    dpi = args.dpi

    if args.to_pixel:
        print(pixel(args.to_pixel, dpi))
    elif args.to_centimeter:
        print(centimeter(args.to_centimeter, dpi))
