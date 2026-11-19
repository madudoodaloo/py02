#!/usr/bin/env python3

import sys
from typing import IO

def ft_ancient_creation()-> None:

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
        print("______\n")
        print(f"Closing '{sys.argv[1]}'")
        file.close()

    except (OSError, UnicodeError, Exception) as e:
        print(f"{e.__class__.__name__}: {e}")
        print("Terminating program")
        return

    try:
        print("\n=== transforming data ===")
        new: list[str] = (line + "#\n" for line in content.splitlines())
        print("______\n")
        for line in new:
            print(line, end="")
        print("______\n")
        
    except Exception as e:
        print(f"Error: {e}")
    
    try:
        newfile: str = input("Enter new file name (or empty): ")

        if not newfile:
            print("Data not saved")
            return

        print(f"Saving data to '{newfile}'")
        save: IO[str] = open(newfile, 'w+')
        new: list[str] = (line + "#\n" for line in content.splitlines())
        for line in new:
            save.write(line)
        print(f"Data saved in '{newfile}'")
            
    except (EOFError, KeyboardInterrupt) as e:
        print("\nData not saved")
        
    except MemoryError as e:
        print("Failed to allocate memory: The data is too large for the available RAM.")

    except (OSError, UnicodeError, Exception) as e:
        print(f"{e.__class__.__name__}: {e}")


if __name__ == "__main__":
    ft_ancient_creation()
