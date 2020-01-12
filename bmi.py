
def calculateBmi(mass, height):
    """
        Calculates Body Mass Index from `mass` and `height` (numbers) and returns it
    """
    if mass < 0:
        raise ValueError('mass < 0')
    if height <= 0:
        raise ValueError('height <= 0')

    return mass / (height ** 2)

def getBmiCategory(bmi):
    """
        Based on `bmi` number, returns one of: "underweight", "normal", "overweight", "obese"
    """
    if bmi < 0:
        raise ValueError('bmi < 0')

    if bmi < 18.5:
        return 'underweight'
    if bmi < 25:
        return 'normal'
    if bmi < 30:
        return 'overweight'
    return 'obese'
