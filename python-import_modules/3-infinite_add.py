#!/usr/bin/python3
import sys

argv = sys.argv

argc = len(argv)

result = 0

for i in range(1, argc):
    result += int(argv[i])
print(result)
