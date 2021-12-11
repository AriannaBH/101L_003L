import unittest
import Grades
import math

class Grade_Test(unittest.TestCase):
    def test_total_returns_total_of_list(self):
        result = Grades.total([1, 10, 22])
        self.assertEqual(result, 33, 'The total function should return 33')
    
    def test_total_returns_0(self):
        result = Grades.total([])
        self.assertEqual(result, 0, 'The total function should return 33')
    
class SimpleTest(unittest.TestCase):

    def test_average_one(self):
        values = (2,5,9)
        self.assertAlmostEqual(Grades.average(values),5.33333,5)
    
    def test_average_two(self):
        values = (2,15,22,9)
        self.assertAlmostEqual(Grades.average(values),12.0000,4)
    
    def test_average_returns_nan(self):
        values = ()
        self.assertIs(Grades.average(values),math.nan)

class Test(unittest.TestCase):
    def test_odd(self):
        self.assertEqual(Grades.median([2, 5, 1]), 2)
    
    def test_even(self):
        self.assertEqual(Grades.median([5, 2, 1, 3]), 2.5)

    def test_empty(self):
        with self.assertRaises(ValueError):
           result = Grades.median([])


unittest.main()
