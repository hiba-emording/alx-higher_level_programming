#!/usr/bin/python3

def uppercase(str):
    text = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        text = text + c
    print("{}".format(text))
