import unittest
from bmi import calculateBmi, getBmiCategory

class TestBmi(unittest.TestCase):
    # Convention is: `def test_<test name>(self):`
    def test_calculateBmi_zeroMass(self):
        result = calculateBmi(0, 120)
        self.assertEqual(result, 0)

    def test_calculateBmi_negativeMass(self):
        with self.assertRaises(ValueError):
            calculateBmi(-1, 120)
    
    def test_calculateBmi_negativeWeight(self):
        with self.assertRaises(ValueError):
            calculateBmi(0, -1)

    def test_calculateBmi_zeroWeight(self):
        with self.assertRaises(ValueError):
            calculateBmi(0, 0)
        
    def test_calculateBmi_simpleCase(self):
        result = calculateBmi(120, 1)
        self.assertEqual(result, 120)
    
    def test_calculateBmi_complexCase(self):
        result = calculateBmi(120, 8)
        self.assertEqual(result, 120 / (8*8))
    
    def test_calculateBmi_floats(self):
        result = calculateBmi(60.5, 4.6)
        self.assertEqual(result, 60.5 / (4.6*4.6))
    
    def test_getBmiCategory_negative(self):
        with self.assertRaises(ValueError):
            getBmiCategory(-1)
    
    def test_getBmiCategory_zero(self):
        result = getBmiCategory(0)
        self.assertEqual(result, 'underweight')
    
    def test_getBmiCategory_underweight(self):
        result = getBmiCategory(18.4)
        self.assertEqual(result, 'underweight')
    
    def test_getBmiCategory_normal(self):
        result = getBmiCategory(18.5)
        self.assertEqual(result, 'normal')
    
    def test_getBmiCategory_normalHigh(self):
        result = getBmiCategory(24.9999)
        self.assertEqual(result, 'normal')

    def test_getBmiCategory_overweight(self):
        result = getBmiCategory(25)
        self.assertEqual(result, 'overweight')
    
    def test_getBmiCategory_overweightHigh(self):
        result = getBmiCategory(29.141592657)
        self.assertEqual(result, 'overweight')

    def test_getBmiCategory_obese(self):
        result = getBmiCategory(30)
        self.assertEqual(result, 'obese')

    def test_getBmiCategory_superHigh(self):
        result = getBmiCategory(3141592657)
        self.assertEqual(result, 'obese')

if __name__ == '__main__':
    unittest.main()
