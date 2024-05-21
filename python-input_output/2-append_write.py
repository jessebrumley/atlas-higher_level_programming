#!/usr/bin/python3
"""Appends text to a file"""


def append_write(filename="", text=""):
    """
    Appends a given text to the end of a file
    and returns the number of characters added

    Parameters:
    filename (str): The name of the file to append to or create
    text (str): The text to append

    Returns:
    int: The number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as file:
        if file:
            original_content = file.read()
            original_length = len(original_content)
        else:
            original_length = 0

        file.write(text)

        new_content = file.read()
        new_length = len(new_content)

        return (new_length - original_length)


if __name__ == "__main__":
    append_write()
