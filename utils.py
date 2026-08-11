from typing import List, Dict, Any


def merge_dicts(dicts: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Merges a list of dictionaries into a single dictionary.

    Args:
        dicts (List[Dict[str, Any]]): A list of dictionaries to merge.

    Returns:
        Dict[str, Any]: A single dictionary containing all key-value pairs.
    """
    merged = {}
    for d in dicts:
        merged.update(d)
    return merged


def flatten_list(nested_list: List[List[Any]]) -> List[Any]:
    """
    Flattens a nested list into a single list.

    Args:
        nested_list (List[List[Any]]): A list of lists to flatten.

    Returns:
        List[Any]: A single list containing all elements.
    """
    return [item for sublist in nested_list for item in sublist]


def string_to_dict(string: str) -> Dict[str, str]:
    """
    Converts a string of key=value pairs into a dictionary.

    Args:
        string (str): A string formatted as key=value; pairs should be separated by commas.

    Returns:
        Dict[str, str]: A dictionary mapped from the string pairs.
    """
    return dict(pair.split('=') for pair in string.split(', '))
