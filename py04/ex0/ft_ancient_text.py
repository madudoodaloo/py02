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
    except (OSError, Exception) as e:
        print(f"{e.__class__.__name__}: {e}")


if __name__ == "__main__":
    ft_ancient_text()


# https://realpython.com/ref/builtin-functions/open/
# https://docs.python.org/3/builtins/exceptions.html#ChildProcessError
# https://realpython.com/ref/builtin-exceptions/oserror/
# https://www.geeksforgeeks.org/python/handling-oserror-exception-in-python/
# https://www.geeksforgeeks.org/python/file-objects-python/
# https://www.geeksforgeeks.org/python/python-open-function/
# https://stackoverflow.com/questions/47452824/catch-unicodedecodeerror-exception-while-reading-file-line-by-line-in-python-3
# https://stackoverflow.com/questions/24983762/git-ignore-local-file-changes
