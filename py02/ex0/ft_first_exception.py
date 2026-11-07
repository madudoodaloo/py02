#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
	return (int(temp_str))


def test_temperature() -> None:
	print("=== Testing Garden Temperature ===")
	print("\n")
	test_value = "25"
	print(f"Input data is: '{test_value}'")
	try:
		temp = input_temperature(test_value)
	except Exception as err:
		print(f"Caught input_temperature() error: {err}")
	else:
		print(f"Temperature is now {temp}°C")
	finally:
			print("\n")

	test_value = "abc"
	print(f"Input data is: '{test_value}'")
	try:
		temp = input_temperature(test_value)
	except Exception as err:
		print(f"Caught input_temperature() error: {err}")
	else:
		print(f"Temperature is now {temp}°C")
	finally:
			print("\n")
		
	print("All tests, all errors successfully handled!")
	
if __name__ == "__main__":
	test_temperature()
