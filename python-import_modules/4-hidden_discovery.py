#!/usr/bin/python3
import hidden_4
def discover_names(module):
    for name in dir(module):
        if not name.startswith("__"):
            print(name)

if __name__ == "__main__":
    module = hidden_4
    discover_names(module)

