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
        print("______\n")
        print(content, end="")
        print("\n______\n")
        print(f"Closing '{sys.argv[1]}'")
        file.close()
        
    except (OSError, UnicodeError, Exception) as e:
        print(f"{e.__class__.__name__}: {e}")
        print("Terminating program")
        return
    
    try:
        print("\n=== transforming data ===")
        newfile: str = input("Enter new file name (or empty): ")
        if not newfile:
            print("Data not saved")
        else:
            print(f"Saving data to '{newfile}'")
            save: IO[str] = open(newfile, 'w+')
            format: list[str] = content.split('\n')
            for line in format:
                save.write(line + '#\n')
            print(f"Data saved in '{newfile}'")
            
    except EOFError as e:
        print("\nData not saved")
        
    except MemoryError as e:
        print("Failed to allocate memory: The data is too large for the available RAM.")

    except (Exception, KeyboardInterrupt) as e:
        print(f"{e.__class__.__name__}: {e}")
        
if __name__ == "__main__":
    ft_ancient_text()
