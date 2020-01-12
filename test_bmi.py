import unittest
from bmi import calculateBmi

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

if __name__ == '__main__':
    unittest.main()
