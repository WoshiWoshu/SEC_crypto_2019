#!/bin/python3

import sys

from enum import Enum

class Return(Enum):
    SUCCESS = 0
    ERROR = 84

# read file content by it's path

def readFileFromPath(filename):
    try:
        with open(filename) as f:
            file_content = f.read()
        if (file_content == ""):
            raise NotImplementedError
    except FileNotFoundError:
        print("Error: File does not exist.")
        sys.exit(Return.ERROR)
    except NotImplementedError:
        print("Error: Void file.")
        sys.exit(Return.ERROR)
    except PermissionError:
        print("Error: Permission denied.")
        sys.exit(Return.ERROR)
    return (file_content)