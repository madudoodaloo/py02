#for name in dir(Exception):
	#print(name)

try:
    # Example triggering a built-in ValueError
    raise ValueError("-12°C is too cold for plants (min 0°C)")
except Exception as err:
    # 'err' holds the exception instance[cite: 1]
    print(f"Handled error: {err}")
    print(f"Error type: {type(err).__name__}")