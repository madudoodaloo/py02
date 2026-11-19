#!/usr/bin/env python3

import random

achievements: list = [
    'Crafting Genius',
    'Strategist',
    'World Savior',
    'Speed Runner',
    'Survivor',
    'Master Explorer',
    'Treasure Hunter',
    'Unstoppable',
    'First Steps',
    'Collector Supreme',
    'Untouchable',
    'Sharp Mind',
    'Boss Slaye'
]


def gen_player_achievements() -> set:
    player: set = set()
    total: int = random.randint(1, len(achievements))
    count: int = 0

    while count < total:
        player.add(random.choice(achievements))
        count += 1

    return player


def main() -> None:
    print("=== Achievement Tracker System ===")

    npc1: set = gen_player_achievements()
    npc2: set = gen_player_achievements()
    npc3: set = gen_player_achievements()
    npc4: set = gen_player_achievements()
    total_ach: set = npc1.union(npc2, npc3, npc4)
    common_ach: set = npc1.intersection(npc2, npc3, npc4)

    print()
    print("=====================")
    print("Players:")
    print("===================")
    print("NPC_1:", npc1)
    print("NPC_2:", npc2)
    print("NPC_3:", npc3)
    print("NPC_4:", npc4)

    print()
    print("=====================")
    print("Distinct achievements:")
    print("===================")
    print(total_ach)

    print()
    print("===================")
    print("Common achievements:")
    print("===================")

    print(common_ach)

    print()
    print("===================")
    print("Unique achievements:")
    print("===================")
    print("NPC_1:", npc1.difference(npc2, npc3, npc4))
    print("NPC_2:", npc2.difference(npc1, npc3, npc4))
    print("NPC_3:", npc3.difference(npc1, npc2, npc4))
    print("NPC_4:", npc4.difference(npc1, npc2, npc3))

    print()
    print("===================")
    print("Missing achievements:")
    print("===================")
    print("NPC_1: ", total_ach.difference(npc1))
    print("NPC_2: ", total_ach.difference(npc2))
    print("NPC_3: ", total_ach.difference(npc3))
    print("NPC_4: ", total_ach.difference(npc4))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{e}")
