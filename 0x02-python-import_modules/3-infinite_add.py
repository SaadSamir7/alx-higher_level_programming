#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

argc = len(sys.argv) - 1

i = 0
res = 0
for cntr in sys.argv:
    if i != 0:
        res += int(cntr)
    else:
        i += 1
print("{:d}".format(res))
