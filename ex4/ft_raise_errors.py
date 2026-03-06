def check_plant_health(plant_name: str, water_lvl: int, sunlight: int) -> str:
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")
    if water_lvl < 1:
        raise ValueError(f"Water level {water_lvl} is too low (min 1)")
    if water_lvl > 10:
        raise ValueError(f"Water level {water_lvl} is too high (max 10)")
    if sunlight < 2:
        raise ValueError(f"Sunlight hours {sunlight} is too low (min 2)")
    if sunlight > 12:
        raise ValueError(f"Sunlight hours {sunlight} is too high (max 12)")
    return f"Plant '{plant_name}' is healthy!\n"


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    try:
        print(check_plant_health("tomato", 5, 8))
    except ValueError as e:
        print(f"Error: {e}\n")

    print("Testing empty plant name...")
    try:
        print(check_plant_health("", 5, 8))
    except ValueError as e:
        print(f"Error: {e}\n")

    print("Testing bad water level...")
    try:
        print(check_plant_health("tomato", 15, 8))
    except ValueError as e:
        print(f"Error: {e}\n")

    print("Testing bad sunlight hours...")
    try:
        print(check_plant_health("tomato", 5, 0))
    except ValueError as e:
        print(f"Error: {e}\n")

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
