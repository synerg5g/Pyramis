from messagetypes import *
from cppvariable import *


def find_parent_key_by_key(nested_dict, target):
    """
    Helper function to return the parent key where the given key is a value.
    """
    for key, value in nested_dict.items():
        if isinstance(value, dict):
            if target in value:
                yield key
            yield from find_parent_key_by_key(value, target)
        elif value[0] == target:
            yield key


def find_key(key, dictionary):
    """
    When given a name attribute, it checks if attr (key)
    is a key in the given dict.
    is key -> has a reducible type.
    This reducible type could also be a key
    """
    if key in dictionary:
        return True
    for value in dictionary.values():
        if isinstance(value, dict) and find_key(key, value):
            return True
    else:
        return False
