#!/usr/bin/evn python
import sys
# input comes from STDIN (standard input)
for line in sys.stdin:
# remove leading and trailing whitespace
    line = line.strip()
# split the line into words
    print line
