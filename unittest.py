
import unittest
from project import *
  
class SimpleTest(unittest.TestCase):

    def test_main(self):
        image_dimensions = [3,3]
        corner_points = [(3,1),(1,1),(1,3),(3,3)]

        res = main(image_dimensions,corner_points)

        expected = [
            [[1.0, 3.0], [2.0, 3.0], [3.0, 3.0]],
            [[1.0, 2.0], [2.0, 2.0], [3.0, 2.0]],
            [[1.0, 1.0], [2.0, 1.0], [3.0, 1.0]]
        ]
        
        self.assertEqual(res,expected)
