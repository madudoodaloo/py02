#!/usr/bin/env python3

import sys


def parse_input() -> dict[str, int]:
    
    inventory: dict[str, int] = {}

    for arg in sys.argv[1:]:
        parts = arg.split(':')

        if len(parts) != 2:
            print(f"Error: Invalid format {parts} - discarding")
            continue

        item_name = parts[0]
        qty_str = parts[1]
        try:
            qty = int(qty_str)
            if (qty < 0):
                raise ValueError("Quantity must be positive")
            elif item_name in inventory:
                print(f"Error: Redundant item '{item_name}' - discarding")
            else:
                inventory[item_name] = qty
        except ValueError as e:
            print(f"Error: Invalid quantity for '{item_name}': {e}")
    
    return inventory
    
def ft_inventory_system() -> None:

    inventory = parse_input()

    if not inventory:
        print("Empty inventory: add items in format <item_name>:<quantity>")
        return

    print()
    print("=== Inventory System Analysis ===")
    print(f"Got inventory: {inventory}")
    
    print(f"Item list: {list(inventory.keys())}")

    print()
    total_qty = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_qty}")

    # division by 0 error if not handled
    if total_qty > 0:
        for item in inventory.keys():
            pct = (inventory[item] / total_qty) * 100
            print(f"Item {item} represents {round(pct, 1)}%")

        most_abundant_item = None
        least_abundant_item = None
        most_abundant_qty = -1
        least_abundant_qty = float('inf')

        for item in inventory:
            if inventory[item] > most_abundant_qty:
                most_abundant_qty = inventory[item]
                most_abundant_item = item
            if inventory[item] < least_abundant_qty:
                least_abundant_qty = inventory[item]
                least_abundant_item = item

        print(f"Item most abundant: {most_abundant_item} "
            f"with quantity {most_abundant_qty}")
        print(f"Item least abundant: {least_abundant_item} "
            f"with quantity {least_abundant_qty}")
    else:
            print("Statistics not applicable")

    print()
    inventory.update({'fairy_dust': 1000})
    print(f"Updated inventory: {inventory}")
	
if __name__ == "__main__":
	ft_inventory_system()
