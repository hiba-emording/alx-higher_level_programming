#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

result = 0

for args in range(len(argv) - 1):
    result = result + int(argv[args + 1])
print("{}".format(result))
