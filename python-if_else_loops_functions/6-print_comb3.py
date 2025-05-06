#!/usr/bin/python3

for i in range(0, 10):
    for j in range(i + 1, 10):
        if i == 0 and j == 1:
            print(f"{i}{j}", end="")
            break
        if i == j:
            continue
        print(f", {i}{j}", end="")
print()