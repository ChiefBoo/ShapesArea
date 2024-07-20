import unittest
from shapes import Circle, Triangle, calculate_area

class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(10)
        self.assertAlmostEqual(circle.area(), 314.1592653589793)

    def test_invalid_circle(self):
        with self.assertRaises(ValueError):
            Circle(-5)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0)

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 3)

    def test_right_angle_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())

    def test_non_right_angle_triangle(self):
        triangle = Triangle(3, 4, 6)
        self.assertFalse(triangle.is_right_triangle())

    def test_calculate_area_circle(self):
        circle = Circle(10)
        self.assertAlmostEqual(calculate_area(circle), 314.1592653589793)

    def test_calculate_area_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(calculate_area(triangle), 6.0)


if __name__ == '__main__':
    unittest.main()