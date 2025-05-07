#!/usr/bin/python3
import sys

if __name__ == "__main__":
    print("{} argument{}".format(len(sys.argv) - 1, "."
                                 if len(sys.argv) == 1 else ":"))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
