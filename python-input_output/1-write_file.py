#!/usr/bin/python3
"""Saves text to a file"""

def write_file(filename="", text=""):
    """
    Writes a given text to a file and returns the number of characters written

    Parameters:
    filename (str): The name of the file to read or create
    text (str): the text to add

    Returns:
    int: The number of characters written
    """
    if not filename:
        filename = "output.txt"

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

        return len(text)


if __name__ == "__main__":
  write_file()