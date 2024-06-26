#!/usr/bin/python3
"""Reads and prints a text file"""


def read_file(filename=""):
    """
    Reads a text file in UTF-8 encoding and prints its content to stdout.

    Parameters:
    filename (str): The name of the file to read. Defaults to an empty string.

    Returns:
    None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read().strip()

        if content.strip():
            print(content)

        else:
            pass


if __name__ == "__main__":
    read_file()
