#!/usr/bin/env python3
import random


def ft_data_alchemist() -> None:

    print("=== Game Data Alchemist ===")
    print()

    initial: list[str] = [
        "Gertrudes", "guilhermina", "Henriquetta",
        "Inacia", "joaquina", "kamila", "Yannik", "Joanne"
    ]

    print(f"Initial list of players: {initial}")
    print()

    all_cap: list[str] = [name.capitalize() for name in initial]
    print(f"New list with all names capitalized: {all_cap}")
    print()

    are_cap: list[str] = [name for name in initial if name[0].isupper()]
    print(f"New list of capitalized names only: {are_cap}")
    print()

    all_scores: dict[str, int] = {
        name: random.randint(0, 1000) for name in all_cap}
    print(f"Score dict: {all_scores}")
    print()

    avg: float = sum(all_scores.values())/len(all_scores)
    print(f"Score average is {round(avg, 2)}")
    print()

    high_scores: dict[str, int] = {
        name: value for name, value in all_scores.items() if value > avg}
    print(f"High scores: {high_scores}")
    print()


if __name__ == "__main__":
    ft_data_alchemist()
