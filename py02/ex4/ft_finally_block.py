#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, msg: str = "Uknown Garden Error") -> None:
        super().__init__(msg)

class PlantError(GardenError):
    def __init__(self, msg: str = "Uknown Plant Error") -> None:
        super().__init__(msg)

def water_plant(plant_name: str) -> None:
    if not plant_name or not plant_name.capitalize() == plant_name:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")

def test_watering_system(plants: list[str]) -> None:
    
    print("Opening watering system")
    try:
        for plant in plants:
                water_plant(plant)
    except PlantError as err:
        print(f"Caught PlantError: {err}")
        print(".. ending tests and returning to main")
        #return
    finally:
        print("Closing watering system")

def main() -> None:
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