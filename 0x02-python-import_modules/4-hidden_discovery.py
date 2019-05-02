#!/usr/bin/python3.4
import hidden_4
if __name__ == "__main__":
    for string in dir(hidden_4):
        if string[:2] != "__":
            print("{}" .format(string))
