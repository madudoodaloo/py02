#!/usr/bin/env python3

import sys
from typing import IO

def ft_ancient_text()-> None:

    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")
        
    try:
        print(f"Attempt to open() [read only]: '{sys.argv[1]}'\n")
        file: IO[str] = open(sys.argv[1], 'r', encoding='ascii')
        
        print("______\n", file.read(), end="")
        print("______\n")
        print(f"Attempt to close() '{sys.argv[1]}'")
        file.close()

    except (OSError) as e:
        print(f"{e.__class__.__name__}: {e}")
    except (UnicodeError) as e:
        print(f"{e.__class__.__name__}: {e}")
    except (Exception) as e:
        print(f"{e.__class__.__name__}: {e}")

    


if __name__ == "__main__":
    ft_ancient_text()

#  encoding='ascii'
# https://realpython.com/ref/builtin-functions/open/
# https://docs.python.org/3/builtins/exceptions.html#ChildProcessError
# https://realpython.com/ref/builtin-exceptions/oserror/
# https://www.geeksforgeeks.org/python/handling-oserror-exception-in-python/
# https://www.geeksforgeeks.org/python/file-objects-python/
# https://www.geeksforgeeks.org/python/python-open-function/
# https://stackoverflow.com/questions/47452824/catch-unicodedecodeerror-exception-while-reading-file-line-by-line-in-python-3
# https://stackoverflow.com/questions/24983762/git-ignore-local-file-changes
