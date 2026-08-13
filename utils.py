import os
import json
from typing import Any, Dict, Optional, Union

class FileError(Exception):
    pass

def read_json_file(file_path: str) -> Optional[Dict[str, Any]]:
    if not os.path.isfile(file_path):
        raise FileError(f'File not found: {file_path}')  
    if not file_path.endswith('.json'):
        raise FileError(f'Incorrect file format, expected .json: {file_path}')  
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        raise FileError(f'Error decoding JSON from file: {file_path}\n{str(e)}')
    except Exception as e:
        raise FileError(f'Unexpected error: {str(e)}')


def write_json_file(file_path: str, data: Union[Dict[str, Any], list]) -> None:
    if not file_path.endswith('.json'):
        raise FileError(f'Incorrect file format, expected .json: {file_path}')  
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        raise FileError(f'Error writing to file: {file_path}\n{str(e)}')  


def validate_json_schema(data: Dict[str, Any], schema: Dict[str, Any]) -> bool:
    # A simple mock function to validate the data structure
    # In a real use case, a library like `jsonschema` would be used
    for key in schema.keys():
        if key not in data:
            raise FileError(f'Missing key in data: {key}')  
    return True