#!/usr/bin/env python3

import math


def get_distance(
    first: tuple[float, float, float],
        second: tuple[float, float, float]) -> float:

    return math.sqrt(
        (second[0]-first[0])**2 +
        (second[1]-first[1])**2 +
        (second[2]-first[2])**2
    )


def get_player_pos() -> tuple[float, float, float] | None:

    while True:
        try:
            user_input = input(
                "Enter coordinates as floats in format 'x,y,z': ")
            coord: list[str] = user_input.split(',')

            if len(coord) != 3:
                raise IndexError("Expecting 3 coordinates, comma seperated")
            x = float(coord[0].strip())
            y = float(coord[1].strip())
            z = float(coord[2].strip())
        except KeyboardInterrupt:
            print("\n<KeyboardInterrupt> ... terminating ...")
            return None
        except EOFError:
            print()
        except Exception as err:
            print(f"Invalid input: {err}")
        else:
            return (x, y, z)


def main() -> None:
    print("Getting first set of coordinates")
    first = get_player_pos()
    if not first:
        return
    print(f"Got a first tuple: {first}")
    print(f"It includes: X={first[0]}, Y={first[1]}, Z={first[2]}")
    center = (0, 0, 0)
    print("Distance to center:", round(get_distance(center, first), 4))

    print()
    print("Getting second set of coordinates")
    second = get_player_pos()
    if not second:
        return
    print(f"Got a second tuple: {second}")
    print(f"It includes: X={second[0]}, Y={second[1]}, Z={second[2]}")
    print("Distance to center:", round(get_distance(first, second), 4))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{e}")
