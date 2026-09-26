#super() = function used in a child to call methods from a parent class (superclass)
class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius
# method ovveriding if it was ovveride in child it eill be as ovverided
    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}")

class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height

circle = Circle("red", True, radius=5)
print(circle.color)

circle.describe()