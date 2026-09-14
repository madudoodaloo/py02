#!/usr/bin/env python3

def garden_operations(op_id: int):
	
	if op_id == 0:
		int("abc")
	elif op_id == 1:
		_ = 10 / 0
	elif op_id == 2:
		open("file/not/found")
	elif op_id == 3:
		_ = "str" + 10
	
def	test_error_types() -> None:
	print("Garden Error Types Demo")
	
	for op in range(5):
		print("Operation:", op, "...")
		try:
			garden_operations(op)
			print("=== Sucessful execution ===")
		except ValueError as err:
			print("Caught ValueError:", err)
		except ZeroDivisionError as err:
			print("Caught ZeroDivisionError:", err)
		except FileNotFoundError as err:
			print("Caught FileNotFoundError:", err)
		except TypeError as err:
			print("Caught TypeError:", err)
			
	print("Let's see with one try: block")
	for op in range(5):
		try:
			garden_operations(op)
		except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as err:
			print(f"Caught {op}: {err}")

	print("All error types tested successfully")

if __name__ == "__main__":
	test_error_types()