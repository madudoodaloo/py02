#!/usr/bin/env python3

from typing import Generator
import random


def gen_event() -> Generator[tuple[str, str], None, None]:
    actions: list = [
        "breath", "laugh", "love", "drive", "work", "sleep",
        "dance", "touch grass", "eat", "dance", "code"
    ]

    names: list = [
        "ana", "beatriz", "carlota", "daniela", "emilia", "fernanda",
        "gertrudes", "guilhermina", "henriquetta", "inacia", "joaquina",
        "kamila", "katya", "lucinda", "leopolda", "leopoldina",
        "marilayne", "jhennyfer",
    ]

    while True:
        yield (random.choice(names), random.choice(actions))


def consume_event(
        events: list[tuple[str, str]]
        ) -> Generator[tuple[str, str], None, None]:

    if not events:
        return
    while len(events) > 0:
        del_event: tuple = random.choice(events)
        events.remove(del_event)
        yield del_event


def main() -> None:
    print("=== Game Data Stream Processor ===")

    for i in range(1, 1001):
        current: tuple = next(gen_event())
        print(f"Event {i}: {current[0]} did action {current[1]}")

    print()
    print("=== Creating list of 10 events ===")
    list_events: list[tuple] = list()
    for i in range(10):
        list_events.append(next(gen_event()))
    print()
    print(f"Built list of 10 events: {list_events}")
    for consumed in consume_event(list_events):
        print()
        print(f"Remains in list: {list_events}")
        if len(list_events) > 0:
            print(f"Got event: {consumed}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{e}")
