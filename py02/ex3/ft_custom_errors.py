#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def ft_custom_errors() -> None:
    print("Custom Garden Errors Demo") 

    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as err:
        print(f"Caught PlantError: {err}")

    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as err:
        print(f"Caught WaterError: {err}")

    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as err:
        print(f"Caught GardenError: {err}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as err:
        print(f"Caught GardenError: {err}")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    ft_custom_errors()