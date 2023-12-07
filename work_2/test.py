import unittest
from main import Engine2D


class TestUnit(unittest.TestCase):


    def test_circle(self):
        obj = Engine2D()
        x, y, r = obj.random()
        self.assertGreaterEqual((x, y, r), (50, 50, 10))
        self.assertLessEqual((x, y, r), (850, 550, 100))

    def test_square(self):
        obj = Engine2D()
        x, y, r = obj.random()
        self.assertGreaterEqual((x, y, r), (50, 50, 10))
        self.assertLessEqual((x, y, r), (850, 550, 100))

    def test_triangle(self):
        obj = Engine2D()
        x, y, r = obj.random()
        self.assertGreaterEqual((x, y, r), (50, 50, 10))
        self.assertLessEqual((x, y, r), (850, 550, 100))

    def test_color(self):
        obj = Engine2D()
        self.assertGreaterEqual(obj.col[0], (0, 0, 0))



