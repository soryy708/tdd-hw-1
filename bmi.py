
def calculateBmi(mass, height):
    """
        Calculates Body Mass Index from `mass` and `height` (numbers) and returns it
    """
    if mass < 0:
        raise ValueError('mass < 0')
    if height <= 0:
        raise ValueError('height <= 0')

    return mass / (height ** 2)
