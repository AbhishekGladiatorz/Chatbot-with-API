#!/usr/bin/python2.7

import os
from os.path import join
import sys
def file_finder():
    fname = raw_input("enter the file name to find")
    for root, dirs, files in os.walk('/'):
        print "searching", root
        if fname in files:
            print "found: %s" % join(root, fname)
            break


