#!/usr/bin/python2.7


import sys
import os

def file_read_from_tail():

    bufsize = 8192

    lines = input('enter the number of lines')
    fname = raw_input('enter the file name along with path')
    fsize = os.stat(fname).st_size

    iter = 0
    with open(fname) as f:
        if bufsize > fsize:
            bufsize = fsize-1
        data = []
        while True:
            iter +=1
            f.seek(fsize-bufsize*iter)
            data.extend(f.readlines())
            if len(data) >= lines or f.tell() == 0:
                print(''.join(data[-lines:]))
                break

