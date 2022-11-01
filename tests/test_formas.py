import unittest
from unittest.mock import MagicMock
from formas.formas import Triangle, TriangleDoesntExist


class TestTriangle(unittest.TestCase):

    def test_area(self):
        """Tests area calculation."""
        with self.subTest():
            Triangle.perimeter = MagicMock(return_value=24)
            self.assertEqual(Triangle(6, 8, 10).area(), 24)
        with self.assertRaises(TriangleDoesntExist):
            Triangle(3, 4, 10)
        with self.assertRaises(TypeError):
            Triangle(6, 8, 'asd')

    def test_exists(self):
        """Tests the existence test of a triangle."""
        with self.assertRaises(TriangleDoesntExist):
            Triangle(3, 4, 10)
        with self.assertRaises(TypeError):
            Triangle(6, 8, 'asd')

    def test_type_sides(self):
        """Tests the classification of a triangle by sides."""
        with self.subTest():
            self.assertEqual(Triangle(3, 4, 5).type_sides(), 'Scalene')
        with self.subTest():
            self.assertEqual(Triangle(3, 3, 4).type_sides(), 'Isosceles')
        with self.subTest():
            self.assertEqual(Triangle(3, 3, 3).type_sides(), 'Equilateral')

    def test_type_angles(self):
        """Tests the classification of a triangle by angles."""
        with self.subTest():
            self.assertEqual(Triangle(3, 4, 5).type_angles(), 'Right')
        with self.subTest():
            self.assertEqual(Triangle(3, 3, 3).type_angles(), 'Acute')
        with self.subTest():
            self.assertEqual(Triangle(4, 8, 11).type_angles(), 'Obtuse')

    def test_perimeter(self):
        """Tests perimeter calculation."""
        with self.subTest():
            self.assertEqual(Triangle(6, 8, 10).perimeter(), 24)


if __name__ == '__main__':
    unittest.main()
