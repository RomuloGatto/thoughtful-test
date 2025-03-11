BULKY_VOLUME_THRESHOLD = 1000000
BULKY_DIMENSION_THRESHOLD = 150
HEAVY_WEIGHT_THRESHOLD = 20

def valid_dimensions(width: float, height: float, length: float, mass: float) -> bool:
    return width > 0 and height > 0 and length > 0 and mass > 0

def sort(width: float, height: float, length: float, mass: float) -> str:
    if not valid_dimensions(width, height, length, mass):
        return "INVALID"

    volume = width * height * length
    bulky = volume >= BULKY_VOLUME_THRESHOLD or width >= BULKY_DIMENSION_THRESHOLD or height >= BULKY_DIMENSION_THRESHOLD or length >= BULKY_DIMENSION_THRESHOLD
    heavy = mass >= HEAVY_WEIGHT_THRESHOLD
    
    if bulky and heavy:
        return "REJECTED"
    
    if bulky or heavy:
        return "SPECIAL"
    
    return "STANDARD"
