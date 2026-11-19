#!/usr/bin/env python3

import sys
from typing import IO

def ft_ancient_text()-> None:

    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")
        
    try:
        file: IO[str] = open(sys.argv[1], 'r')
        print(f"Accessing file '{sys.argv[1]}'")
        print()
        print("________________")
        print()
        print(file.read())
        print("________________")
        print()
        file.close()
        print(f"Closing '{sys.argv[1]}'")
    except (OSError, Exception, ValueError, UnicodeError) as e:
        print(f"{e.__class__.__name__}: {e}")


if __name__ == "__main__":
    ft_ancient_text()
