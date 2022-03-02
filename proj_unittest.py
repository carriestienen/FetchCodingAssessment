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

    def test_organizeCPs(self):
        corner_points = [
            (1.5, 1.5),
            (4.0, 1.5),
            (1.5, 8.0),
            (4.0, 8.0)
        ]

        expected = [
            [[1, 3], [3, 3]], 
            [[1, 1], [3, 1]]
        ]

        res = organizeCPs(corner_points)

        self.assertEqual(res,expected)

    def test_getAllPts(self):
        expected = [
            [[1, 3], [2, 3], [3, 3]], 
            [[1, 2], [2, 2], [3, 2]], 
            [[1, 1], [2, 1], [3, 1]]
        ]

        res = getAllPts(3,1,3)

        self.assertEqual(res,expected)
        
    def test_createMatrix(self):
        m = [1,2,3],[1,2,3]

        expected = [
            [[1.0, 3.0], [2.0, 3.0], [3.0, 3.0]], 
            [[1.0, 2.0], [2.0, 2.0], [3.0, 2.0]], 
            [[1.0, 1.0], [2.0, 1.0], [3.0, 1.0]]
        ]

        res = createMatrix(m)

        self.assertEqual(res,expected)
