def check_temperature(temp_str) -> int:
    if not type(temp_str) is int:
        raise TypeError(f"Error: '{temp_str}' is not a number")
    elif temp_str > 40:
        raise Exception(f"Error: {temp_str}°C is too hot for plants (max 40°C)")
    elif temp_str < 0:
        raise Exception(f"Error: {temp_str}°C is too cold for plants (min 0°C)")
    else:
        print(f"Temperature {temp_str}°C is perfect for plants!")
