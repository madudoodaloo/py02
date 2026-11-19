#!/usr/bin/env python3
import sys


def display_scores(scores: list[int]) -> None:
    scores.sort()

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores):.1f}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


def ft_score_analytics() -> None:
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
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2> ...")
        return

    display_scores(scores)


if __name__ == "__main__":
    try:
        ft_score_analytics()
    except Exception as e:
        print(f"{e}")
