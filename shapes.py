import math

class Shape:
	"""docstring for Shape"""
	def area(self):
		pass

class Circle(Shape):
	"""docstring for Circle"""
	def __init__(self, radius):
		super(Circle, self).__init__()
		if radius <= 0:
			raise ValueError("Radius must be > 0.")
		self.radius = radius

	def area(self):
		return math.pi * (self.radius ** 2)


class Triangle(Shape):
	"""docstring for Triangle"""
	def __init__(self, a, b, c):
		super(Triangle, self).__init__()
		if a <= 0 or b <= 0 or c <= 0:
			raise ValueError("Sides must be > 0.")
		if a + b <= c or a + c <= b or b + c <= a:
			raise ValueError("Invalid triangle sides.")
		self.a = a
		self.b = b
		self.c = c

	def area(self):
		p = (self.a + self.b + self.c) / 2
		return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

	def is_right_triangle(self):
		sides = sorted([self.a, self.b, self.c])
		return math.isclose(sides[2] ** 2, sides[0] **2 + sides[1] ** 2)


def calculate_area(shape):
	return shape.area()
		
		
