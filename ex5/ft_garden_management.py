class GardenError(Exception):
    pass


class InvalidPlantError(GardenError):
    pass


class WaterTankError(GardenError):
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants: list[str] = []
        self.water_tank: int = 10

    def add_plant(self, n: str) -> None:
        if not n or not isinstance(n, str):
            raise InvalidPlantError("Plant name cannot be empty!")
        if n in self.plants:
            raise InvalidPlantError(f"Plant '{n}' already exists in garden!")
        self.plants.append(n)
        print(f"Added {n} successfully")

    def water_plants(self, plant_list: list[str]) -> None:
        print("Opening watering system")
        try:
            for p in plant_list:
                if not isinstance(p, str) or not p:
                    raise InvalidPlantError(f"Cannot water invalid plant: {p}")
                if self.water_tank <= 0:
                    raise WaterTankError("Not enough water in tank")
                self.water_tank -= 1
                print(f"Watering {p} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, p: str, water_lvl: int, sunlight: int) -> str:
        if not p:
            raise InvalidPlantError("Plant name cannot be empty!")
        if water_lvl < 1:
            raise ValueError(f"Water level {water_lvl} is too low (min 1)")
        if water_lvl > 10:
            raise ValueError(f"Water level {water_lvl} is too high (max 10)")
        if sunlight < 2:
            raise ValueError(f"Sunlight hours {sunlight} is too low (min 2)")
        if sunlight > 12:
            raise ValueError(f"Sunlight hours {sunlight} is too high (max 12)")
        return f"healthy (water: {water_lvl}, sun: {sunlight})"

    def check_water_tank(self) -> None:
        if self.water_tank <= 0:
            raise WaterTankError("Not enough water in tank")


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    manager = GardenManager()

    print("\nAdding plants to garden...")
    for plant in ["tomato", "lettuce", ""]:
        try:
            manager.add_plant(plant)
        except (InvalidPlantError, GardenError) as e:
            print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    try:
        manager.water_plants(["tomato", "lettuce"])
    except (InvalidPlantError, WaterTankError) as e:
        print(f"Error watering plants: {e}")

    print("\nChecking plant health...")
    health_checks: list[tuple[str, int, int]] = [
        ("tomato", 5, 8),
        ("lettuce", 15, 8),
    ]
    for plant, water, sun in health_checks:
        try:
            result = manager.check_plant_health(plant, water, sun)
            print(f"{plant}: {result}")
        except ValueError as e:
            print(f"Error checking {plant}: {e}")

    print("\nTesting error recovery...")
    try:
        empty_manager = GardenManager()
        empty_manager.water_tank = 0
        empty_manager.check_water_tank()
    except WaterTankError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


test_garden_management()
