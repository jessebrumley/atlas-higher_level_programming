#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum of all arguements, followed by new line"""
    import sys
    total = sum(int(arg) for arg in sys.argv[1:])
    print("{}".format(total))
