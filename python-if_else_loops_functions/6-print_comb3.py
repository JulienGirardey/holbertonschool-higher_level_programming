#!/usr/bin/python3

for i in range(0, 10):
    for j in range(i + 1, 10):
        if i == 0 and j == 1:
            print("{}{}".format(i, j), end="")
            continue
        if i == j:
            continue
        print(", {}{}".format(i, j), end="")
print()
