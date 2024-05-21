#!/usr/bin/python3

def write_file(filename="", text=""):
    """
    Writes a given text to a file and returns the number of characters written
    """
    if not filename:
        filename = "output.txt"

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
