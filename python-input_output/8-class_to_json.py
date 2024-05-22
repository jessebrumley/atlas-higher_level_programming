#!/usr/bin/python3
"""returns the dictionary description with simple data structure"""

def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object:

    Parameters:
    obj: an instance of a Class, all objects of this Class must
    already be serializable (list, dictionary, string, integer and boolean)
    
    Returns:
    A dictionary with a simple data structure
    """
    return vars(obj)


if __name__ == "__main__":
    class_to_json()
