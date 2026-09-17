#!/usr/bin/env python3
"""Module for parsing and displaying cmdline args through import sys"""

import sys

def ft_command_quest()-> None:
    """Parses sys.argv to display script name and positional args"""
    print("=== Command Quest ===")

    args: list[str] = sys.argv[1:]

    print("Program name:", sys.argv[0])

    if not args:
        print("No arguments provided!")
    else:
        print("Arguments received:", len(args))
        for i in range(len(args)):
            print(f"Argument {i + 1}: {args[i]}")

    print("Total arguments:", len(sys.argv))

if __name__ == "__main__":
    ft_command_quest()
