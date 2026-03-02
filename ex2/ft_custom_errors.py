class GardenError(Exception):



class PlantError(GardenError):



class WaterError(GardenError):



"""if Plant.days >= 50:
    raise GardenError("Caught a garden error: The tomato plant is wilting!")"""
