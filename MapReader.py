import sys
import re

if (len(sys.argv) == 3):
    key = sys.argv[2]
    mapfile = open(sys.argv[1],"r")
    total = 0
    unit = ""
    for line in mapfile:
        split = re.search(r"(.+):\s*([0-9]+) kB$",line,re.I | re.M)
        if split and split.group(1) == key:
            total = total + int(split.group(2))
    print "********\nkey:\t%s\ntotal:\t%d\nUnit:\tkB" %(key,total)
else:
    print "Usage: python <prog-file> <mapfile> <key>"
