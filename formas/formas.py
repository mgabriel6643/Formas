from math import acos, degrees, sqrt


class TriangleDoesntExist(Exception):
    print("The values typed don't make a triangle.")


class Triangle:

    def __init__(self, side_a, side_b, side_c) -> None:
        """Triangle Constructor
        Args:
            side_a (float): First side of the supposed triangle.
            side_b (float): Second side of the supposed triangle.
            side_c (float): Third side of the supposed triangle.

        Returns:
            None.
        """

        self.side_a: float = side_a
        self.side_b: float = side_b
        self.side_c: float = side_c
        self.type_side: str = ''
        self.type_angle: str = ''
        if not (self.side_a + self.side_b > self.side_c and self.side_b + self.side_c > self.side_a and
                self.side_a + self.side_c > self.side_b):
            raise TriangleDoesntExist

    def type_sides(self) -> str:
        """Informs what type of triangle is formed from the chosen sides.
        Returns:
            type_side (str): The triangle formed type.
        """
        if self.side_a == self.side_b == self.side_c:
            self.type_side = 'Equilateral'
        elif self.side_a != self.side_b and self.side_a != self.side_c and self.side_b != self.side_c:
            self.type_side = 'Scalene'
        else:
            self.type_side = 'Isosceles'
        return self.type_side

    def type_angles(self) -> str:
        """Informs what type of triangle is formed from the chosen sides.
        Returns:
            type_angle (str): The triangle formed type.
        """
        angle_a: float = degrees(acos((self.side_b ** 2 + self.side_c ** 2 - self.side_a ** 2) /
                                      (2 * self.side_b * self.side_c)))
        angle_b: float = degrees(acos((self.side_a ** 2 + self.side_c ** 2 - self.side_b ** 2) /
                                      (2 * self.side_a * self.side_c)))
        angle_c: float = degrees(acos((self.side_a ** 2 + self.side_b ** 2 - self.side_c ** 2) /
                                      (2 * self.side_a * self.side_b)))
        if angle_a == 90 or angle_b == 90 or angle_c == 90:
            self.type_angle = 'Right'
        elif angle_a > 90 or angle_b > 90 or angle_c > 90:
            self.type_angle = 'Obtuse'
        else:
            self.type_angle = 'Acute'
        return self.type_angle

    def perimeter(self) -> float:
        """Informs the perimeter of the triangle formed from the chosen sides.
        Returns:
            perimeter (float): The perimeter value of the triangle formed.
        """
        perimeter: float = self.side_a + self.side_b + self.side_c
        return perimeter

    def area(self) -> float:
        """Informs the area of the triangle formed from the chosen sides.
        Returns:
            area (float): The area value of the triangle.
        """
        semiperimeter: float = self.perimeter() / 2
        area: float = sqrt(semiperimeter * (semiperimeter - self.side_a) * (semiperimeter - self.side_b) *
                           (semiperimeter - self.side_c))
        return area


if __name__ == '__main__':
    tri = Triangle(0, 3, 4)
    print(tri.area())
