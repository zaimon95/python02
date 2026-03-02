class GardenError(Exception):

    def __init__(self, message, errors) -> None:
        super().__init__(message)
        self.errors = errors


class PlantError(GardenError):
    def __init__(self, message, errors) -> None:
        super().__init__(message, errors)


class WaterError(GardenError):
    def __init__(self, message, errors) -> None:
        super().__init__(message, errors)


"""if Plant.days >= 50:
    raise GardenError("Caught a garden error: The tomato plant is wilting!")"""
