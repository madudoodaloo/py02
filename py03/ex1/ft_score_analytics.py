#!/usr/bin/env python3
"""Module for crunching and analyzing player scores from command-line arguments."""

import sys

def ft_score_analytics() -> None:
    """Parses score arguments, performs statistical calculations, and prints results."""
    print(("=== Player Score Analytics ==="))

    raw_args: list[str] = sys.argv[1:]

    scores: list[int] = []
    for arg in raw_args:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Error: '{arg}' is not a valid numerical score.")
            continue

    if not scores:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    scores.sort()

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores):.1f}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    ft_score_analytics()