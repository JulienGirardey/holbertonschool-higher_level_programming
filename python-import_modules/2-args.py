#!/usr/bin/python3
import sys

if __name__ == "__main__":

    argv = sys.argv

    argc = len(argv) - 1
    print("{} argument{}".format(argc, "." if argc == 0 else ":"))
    for i in range(1, argc):
        print("{}: {}".format(i, argv[i]))
