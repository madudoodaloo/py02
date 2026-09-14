#!/usr/bin/env python3

class GardenError(Exception):
    """Base exception for all garden-related errors."""

    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    """Raised for problems related to plants."""

    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    """Raised for problems related to the watering system."""

    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def ft_custom_errors() -> None:
    """Demonstrates creating, raising, and catching custom domain exceptions."""
    print("Custom Garden Errors Demo") 

    # 1. Testing specific catch for PlantError
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as err:
        print(f"Caught PlantError: {err}")

    # 2. Testing specific catch for WaterError
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as err:
        print(f"Caught WaterError: {err}")

    # 3. Testing catching all garden errors via parent class GardenError
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