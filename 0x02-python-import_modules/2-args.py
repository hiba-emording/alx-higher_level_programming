#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    counter = len(argv) - 1

    if counter == 0:
        print("0 arguments.")
    elif counter == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(counter))
    for args in range(counter):
        print("{}: {}".format(args + 1, argv[args+1]))
