#!/usr/bin/env python3

import sys
from typing import IO

def ft_ancient_text()-> None:

    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== cat a file ===")
        
    try:
        print(f"Opening [read only]: '{sys.argv[1]}'\n")
        file: IO[str] = open(sys.argv[1], 'r')
        content: str = file.read()
        while (t)
        print("______\n", 
        print(content, end="")) 
        print("______\n")
        print(f"Closing '{sys.argv[1]}'")
        file.close()
        
    except (OSError) as e:
        print(f"{e.__class__.__name__}: {e}")
    except (UnicodeError) as e:
        print(f"{e.__class__.__name__}: {e}")
    except (Exception) as e:
        print(f"{e.__class__.__name__}: {e}")

    try:
        print("=== transforming data ===")
        print("______\n", file.read(), end="")
        print("______\n")
        file.close()
        
        

    except
if __name__ == "__main__":
    ft_ancient_text()
