#!/usr/bin/env python3

import sys
import typing


def read_archive(file_name: str) -> str | None:
    archive: typing.IO[str]
    try:
        archive = open(file_name, "r", encoding="utf-8", newline="")
    except (OSError, ValueError) as error:
        print(f"Error opening file '{file_name}': {error}")
        return None

    try:
        contents = archive.read()
    except (OSError, UnicodeError) as error:
        print(f"Error reading file '{file_name}': {error}")
        return None
    finally:
        try:
            archive.close()
        except OSError as error:
            print(f"Error closing file '{file_name}': {error}")

    return contents


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    file_name: str = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_name}'")
    contents = read_archive(file_name)
    if contents is None:
        return

    print("---")
    print(contents, end="")
    if contents and contents[-1] != "\n":
        print()
    print("---")
    print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    main()
