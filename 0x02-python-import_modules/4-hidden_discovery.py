#!/usr/bin/python3
import sys
import hidden_4 as hidden

if __name__ != "__main__":
    exit()

for n in dir(hidden):
    if n[0:2] != "__":
        print(n)