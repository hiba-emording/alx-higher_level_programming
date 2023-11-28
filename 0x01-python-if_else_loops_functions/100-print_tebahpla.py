#!/usr/bin/python3

switch = 0
for char in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(char - switch)), end="")
    if switch == 0:
        switch = 32
    else:
        switch = 0
