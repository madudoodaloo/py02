#!/usr/bin/env python3

class GardenError(Exception):
    """Base exception for all garden-related errors"""

    def __init__(self, msg: str = "Uknown Garden Error") -> None:
        super().__init__(msg)

class PlantError(GardenError):
    """Exception raised for plant-specific problems."""

    def __init__(self, msg: str = "Uknown Plant Error") -> None:
        super().__init__(msg)

def water_plant(plant_name: str) -> None:
    """Attempts to water a plant.

    Raises:
        PlantError: If the plant_name is not capitalized.
    """
    if not plant_name or not plant_name[0].isupper():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")

def test_watering_system(plants: list[str]) -> None:
    """Simulates watering a list of plants with resource cleanup."""
    try:
        print("Opening watering system")
        for plant in plants:
                water_plant(plant)
    except PlantError as err:
        print(f"Caught PlantError: {err}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")

def main() -> None:
    """Main execution function to test errors"""
    print("=== Gardenning Watering System ===")

    print("Testing valid plants...")
    valid_plants = ["Tomato", "Lettuce", "Carrots"]
    test_watering_system(valid_plants)

    print()
    print("Testing invalid plants...")
    invalid_plants = ["Tomato", "lettuce", "Carrots"]
    test_watering_system(invalid_plants)

    print()
    print("Cleanup always happen, even with errors!")

if __name__ == "__main__":
    main()