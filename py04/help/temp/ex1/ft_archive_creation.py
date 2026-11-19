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


def mark_lines(contents: str) -> str:
    marked_lines: list[str] = []
    lines = contents.splitlines(keepends=True)
    for line in lines:
        if line.endswith("\r\n"):
            marked_lines.append(line[:-2] + "#\r\n")
        elif line.endswith("\n") or line.endswith("\r"):
            marked_lines.append(line[:-1] + "#" + line[-1])
        else:
            marked_lines.append(line + "#")
    return "".join(marked_lines)


def show_contents(contents: str) -> None:
    print("---")
    print(contents, end="")
    if contents and contents[-1] != "\n":
        print()
    print("---")


def write_archive(file_name: str, contents: str) -> None:
    archive: typing.IO[str]
    print(f"Saving data to '{file_name}'")
    try:
        archive = open(file_name, "w", encoding="utf-8", newline="")
    except (OSError, ValueError) as error:
        print(f"Error opening file '{file_name}': {error}")
        print("Data not saved.")
        return

    saved = False
    try:
        archive.write(contents)
        saved = True
    except (OSError, UnicodeError) as error:
        print(f"Error writing file '{file_name}': {error}")
    finally:
        try:
            archive.close()
        except OSError as error:
            saved = False
            print(f"Error closing file '{file_name}': {error}")

    if saved:
        print(f"Data saved in file '{file_name}'.")
    else:
        print("Data not saved.")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    file_name = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")
    contents = read_archive(file_name)
    if contents is None:
        return

    show_contents(contents)
    print(f"File '{file_name}' closed.")
    transformed = mark_lines(contents)
    print("\nTransform data:")
    show_contents(transformed)

    try:
        destination = input("Enter new file name (or empty): ")
    except (KeyboardInterrupt, EOFError):
        print("\nInput interrupted. Not saving data.")
        return

    if destination == "":
        print("Not saving data.")
        return
    write_archive(destination, transformed)


if __name__ == "__main__":
    main()
