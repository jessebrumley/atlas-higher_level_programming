#!/usr/bin/python3
"""returns the dictionary description with simple data structure"""

import json


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
    json_obj = []
    
    for attr_name, attr_value in obj.__dict__.items():
        if isinstance(attr_value, (list, dict)):
            json_attr = class_to_json(attr_value)
        elif isinstance(attr_value, bool):
            json_attr = str(attr_value).lower()
        else:
            json_attr = attr_value
        
        json_obj.append({attr_name: json_attr})
    
    json_str = "{\n"
    for item in json_obj:
        json_str += "  \"" + next(iter(item)) + "\": " + str(item[next(iter(item))]) + ",\n"
    json_str = json_str.rstrip(",\n") + "\n}\n"
    
    return json_str


if __name__ == "__main__":
    class_to_json()
