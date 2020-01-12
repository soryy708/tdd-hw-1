import unittest
from bblsort import bblSort

class TestBblsort(unittest.TestCase):
    # Convention is: `def test_<test name>(self):`
    def test_bblsort_empty(self):
        val = tuple()
        result = bblSort(val)
        self.assertNotEqual(result, None) # Check that function does return something
        self.assertEqual(len(val), len(result)) # Check that no elements were lost
        self.assertTupleEqual(result, ()) # Check that function returns the correct thing
    
    def test_bblsort_oneElement(self):
        val = (42,)
        result = bblSort(val)
        self.assertNotEqual(result, None) # Check that function does return something
        self.assertEqual(len(val), len(result)) # Check that no elements were lost
        self.assertTupleEqual(result, (42,)) # Check that function returns the correct thing
    
    def test_bblsort_twoElAlreadySorted(self):
        val = (1, 2)
        result = bblSort(val)
        self.assertNotEqual(result, None) # Check that function does return something
        self.assertEqual(len(val), len(result)) # Check that no elements were lost
        self.assertTupleEqual(result, (1, 2)) # Check that function returns the correct thing
    
    def test_bblSort_twoElNotSorted(self):
        val = (2, 1)
        result = bblSort(val)
        self.assertNotEqual(result, None) # Check that function does return something
        self.assertEqual(len(val), len(result)) # Check that no elements were lost
        self.assertTupleEqual(result, (1, 2)) # Check that function returns the correct thing

    def test_bblSort_fiveElSorted(self):
        val = (3, 5, 7, 11, 13)
        result = bblSort(val)
        self.assertNotEqual(result, None) # Check that function does return something
        self.assertEqual(len(val), len(result)) # Check that no elements were lost
        self.assertTupleEqual(result, (3, 5, 7, 11, 13)) # Check that function returns the correct thing
    
    def test_bblSort_fiveElReversed(self):
        val = (13, 11, 7, 5, 3)
        result = bblSort(val)
        self.assertNotEqual(result, None) # Check that function does return something
        self.assertEqual(len(val), len(result)) # Check that no elements were lost
        self.assertTupleEqual(result, (3, 5, 7, 11, 13)) # Check that function returns the correct thing

    def test_bblSort_fiveElUnsorted(self):
        val = (7, 3, 13, 5, 11)
        result = bblSort(val)
        self.assertNotEqual(result, None) # Check that function does return something
        self.assertEqual(len(val), len(result)) # Check that no elements were lost
        self.assertTupleEqual(result, (3, 5, 7, 11, 13)) # Check that function returns the correct thing
    
    def test_bblSort_fiveElAllDupes(self):
        val = (7, 7, 7, 7, 7)
        result = bblSort(val)
        self.assertNotEqual(result, None) # Check that function does return something
        self.assertEqual(len(val), len(result)) # Check that no elements were lost
        self.assertTupleEqual(result, (7, 7, 7, 7, 7)) # Check that function returns the correct thing
    
    def test_bblSort_fiveElDupes(self):
        val = (7, 3, 7, 42, 42)
        result = bblSort(val)
        self.assertNotEqual(result, None) # Check that function does return something
        self.assertEqual(len(val), len(result)) # Check that no elements were lost
        self.assertTupleEqual(result, (3, 7, 7, 42, 42)) # Check that function returns the correct thing

    def test_bblsort_stringsempty(self):
        val = tuple()
        result = bblSort(val)
        self.assertNotEqual(result, None) # Check that function does return something
        self.assertEqual(len(val), len(result)) # Check that no elements were lost
        self.assertTupleEqual(result, ()) # Check that function returns the correct thing
    
    def test_bblsort_stringsoneElement(self):
        val = ('bob',)
        result = bblSort(val)
        self.assertNotEqual(result, None) # Check that function does return something
        self.assertEqual(len(val), len(result)) # Check that no elements were lost
        self.assertTupleEqual(result, ('bob',)) # Check that function returns the correct thing
    
    def test_bblsort_stringstwoElAlreadySorted(self):
        val = ('alice', 'bob')
        result = bblSort(val)
        self.assertNotEqual(result, None) # Check that function does return something
        self.assertEqual(len(val), len(result)) # Check that no elements were lost
        self.assertTupleEqual(result, ('alice', 'bob')) # Check that function returns the correct thing
    
    def test_bblSort_stringstwoElNotSorted(self):
        val = ('bob', 'alice')
        result = bblSort(val)
        self.assertNotEqual(result, None) # Check that function does return something
        self.assertEqual(len(val), len(result)) # Check that no elements were lost
        self.assertTupleEqual(result, ('alice', 'bob')) # Check that function returns the correct thing

    def test_bblSort_stringsfiveElSorted(self):
        val = ('alpha', 'bravo', 'charlie', 'delta', 'echo')
        result = bblSort(val)
        self.assertNotEqual(result, None) # Check that function does return something
        self.assertEqual(len(val), len(result)) # Check that no elements were lost
        self.assertTupleEqual(result, ('alpha', 'bravo', 'charlie', 'delta', 'echo')) # Check that function returns the correct thing
    
    def test_bblSort_stringsfiveElReversed(self):
        val = ('echo', 'delta', 'charlie', 'bravo', 'alpha')
        result = bblSort(val)
        self.assertNotEqual(result, None) # Check that function does return something
        self.assertEqual(len(val), len(result)) # Check that no elements were lost
        self.assertTupleEqual(result, ('alpha', 'bravo', 'charlie', 'delta', 'echo')) # Check that function returns the correct thing

    def test_bblSort_stringsfiveElUnsorted(self):
        val = ('charlie', 'alpha', 'bravo', 'echo', 'delta')
        result = bblSort(val)
        self.assertNotEqual(result, None) # Check that function does return something
        self.assertEqual(len(val), len(result)) # Check that no elements were lost
        self.assertTupleEqual(result, ('alpha', 'bravo', 'charlie', 'delta', 'echo')) # Check that function returns the correct thing
    
    def test_bblSort_stringsfiveElAllDupes(self):
        val = ('echo', 'echo', 'echo', 'echo', 'echo')
        result = bblSort(val)
        self.assertNotEqual(result, None) # Check that function does return something
        self.assertEqual(len(val), len(result)) # Check that no elements were lost
        self.assertTupleEqual(result, ('echo', 'echo', 'echo', 'echo', 'echo')) # Check that function returns the correct thing
    
    def test_bblSort_stringsfiveElDupes(self):
        val = ('echo', 'charlie', 'echo', 'zulu', 'zulu')
        result = bblSort(val)
        self.assertNotEqual(result, None) # Check that function does return something
        self.assertEqual(len(val), len(result)) # Check that no elements were lost
        self.assertTupleEqual(result, ('charlie', 'echo', 'echo', 'zulu', 'zulu')) # Check that function returns the correct thing

if __name__ == '__main__':
    unittest.main()
