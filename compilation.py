#!/usr/bin/python
import sys

def usage():
    print "Usage: python compilation.py args\nargs can be the names of one or more csv files, seperated by spaces\nthe first file must contain all the entries found in succeeding files\nOutput: one csv file compiled by field name"

if len(sys.argv) < 2:
    print "Error; no arguments given."
    usage()
    
else:
    input = []
    for arg in sys.argv[1:]:
        with open(arg) as temp_file:
            input.append(map(lambda x: x.strip().split(','),temp_file.readlines()))

