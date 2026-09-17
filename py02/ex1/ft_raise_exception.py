#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
	"""Converts a temperature string to an integer and checks plant safety bounds.

	Args:
        temp_str: The temperature string input to convert.

    Returns:
        The temperature as an integer if within [0, 40] °C.

    Raises:
        ValueError: If temp_str is not a valid integer or falls outside
                    the safe range for plants (0°C to 40°C).
    """
	temp = int(temp_str)
	if temp < 0:
		raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
	if temp > 40:
		raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
	return temp


def test_temperature() -> None:
	"""Tests input_temperature with valid, invalid, and extreme values."""
	print("=== Testing Garden Temperature ===")
	print("\n")

	test_cases = ["25", "abc", "100", "-50"]

	for data in test_cases:
		print(f"Input data is '{data}'")
		try:
			temp = input_temperature(data)
			print(f"Temperature is now {temp}°C")
		except Exception as err:
			print(f"Caught input_temperature error: {err}")
	
	print("\n")
	print("All tests, all errors successfully handled!")
	
if __name__ == "__main__":
	test_temperature()
