#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":

    names = dir(hidden_4)

    names_tries = sorted(names)

    for names in names_tries:
        if not names.startswith("__"):
            print(names)
