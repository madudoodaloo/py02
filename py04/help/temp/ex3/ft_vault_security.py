#!/usr/bin/env python3

def secure_archive(
    file_name: str, action: str = "read", contents: str = ""
) -> tuple[bool, str]:
    if action == "read":
        try:
            with open(file_name, "r", encoding="utf-8", newline="") as archive:
                return True, archive.read()
        except (OSError, UnicodeError, ValueError) as error:
            return False, f"{error}"

    try:
        var = archive.read()
        print(var)
    except Exception as e:
        print("boom", e)

    if action == "write":
        try:
            with open(file_name, "w", encoding="utf-8", newline="") as archive:
                archive.write(contents)
            return True, "Content successfully written to file"
        except (OSError, UnicodeError, ValueError) as error:
            return False, f"{error}"

    return False, "Unknown action: expected 'read' or 'write'"


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))
    print("\nUsing 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt")
    print(result)
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    if result[0]:
        print(secure_archive("new_fragment.txt", "write", result[1]))
    else:
        print((False, "Source file unavailable; no new file written"))


if __name__ == "__main__":
    main()
