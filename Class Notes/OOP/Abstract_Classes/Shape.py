from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def __repr__(self):
        return type(self).__name__ + \
               '\n' + "Area: %.3f" % (self.get_area()) + \
               '\n' + "Perimeter: %.3f" % (self.get_perimeter()) + \
               '\n' + 25 * '='


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * (self.radius ** 2)

    def get_perimeter(self):
        return 2 * pi * self.radius


class Polygon(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height


class RightTriangle(Polygon):
    def __init__(self, width, height):
        super(RightTriangle, self).__init__(width, height)

    def get_area(self):
        return self.width * self.height / 2

    def get_perimeter(self):
        return self.width + self.height + (self.width ** 2 + self.height ** 2) ** 0.5


class Rectangle(Polygon):
    def __init__(self, width, height):
        super(Rectangle, self).__init__(width, height)

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)


class Square(Rectangle):
    pass


class ShapesContainer:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def get_total_areas(self):
        area = 0
        for shape in self.shapes:
            area += shape.get_area()
        return area

    def __repr__(self):
        s = ''
        for shape in self.shapes:
            s = s + str(shape) + '\n'
        return s.strip()


container = ShapesContainer()
container.add_shape(Square(5, 5))
container.add_shape(RightTriangle(8, 4))
container.add_shape(Circle(7))
container.add_shape(Rectangle(6, 4))
print(f"Total Areas: {container.get_total_areas():.2f}", end='\n\n')
print(container)