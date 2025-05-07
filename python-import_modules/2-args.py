#!/usr/bin/python3
import sys

if __name__ == "__main__":

    argv = sys.argv

    argc = len(argv) - 1
    print("{} argument{}{}".format(argc, "s" if argc != 1
                                   else "", "." if argc == 0 else ":"))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
