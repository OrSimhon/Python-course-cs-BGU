from functools import total_ordering


@total_ordering
class Vector:
    def __init__(self, cords):
        self.cords = tuple(cords)

    def __repr__(self):
        return str(self.cords)

    def norm(self):
        return sum([x ** 2 for x in self.cords]) ** 0.5

    def cords(self):
        return self.cords

    def __gt__(self, other):
        return self.norm() > other.norm()

    def __eq__(self, other):
        return self.norm() == other.norm()


v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
v3 = Vector([7, 8, 9])

print(sorted([v1, v2, v3]))
print(v1 > v2)
print(v1 < v2)
print(Vector([1, 2, 3]) == Vector([1, 2, 3]))
print(Vector([1, 2, 3]) != Vector([1, 2, 3]))
print(Vector([4, 5, 6]) >= Vector([1, 2, 3]))
print("==", v1 == v2)
print("!=", v1 != v2)
print(">:", v1 > v2)
print("<:", v1 < v2)
print(">=:", v1 >= v2)
print("<=:", v1 <= v2)

print()


class Person:
    def __init__(self, gender):
        self._gender = gender
        pass

    @staticmethod  # Dont get self
    def static():
        return "ve ben ellll"

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        """Set the gender"""
        if not isinstance(value, str):
            raise TypeError("must be string")
        self._gender = value

    @property
    def toilet_type(self):
        return 'M' if self._gender in ['M', 'G', 'B', 'Etc.'] else 'W'

    @classmethod
    def give_birth(cls):
        return cls('T')

    def __repr__(self):
        return "I'm a: %s\nAnd i use the %s" % (self.gender, self.toilet_type)


p = Person('M')
p.gender = 'G'
p.gender = 'T'
print(p.toilet_type)
p.toilet_type = 'ATGC'
