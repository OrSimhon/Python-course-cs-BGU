import copy


class Vector:
    """
    A class used to represent a vector.
    :attribute values: a list of numbers that describe the vector
    """

    def __init__(self, lst):
        """
        Constructor for Vector class
        :param lst: a list of numbers
        """
        # Exception
        if not isinstance(lst, list):
            raise ValueError("Wrong parameter type")

        self.values_shallow = lst  # Shallow Copy = pointing to the same address
        self.values_copy = copy.copy(lst)  # pointing to different addresses in one level
        self.values_deep_copy = copy.deepcopy(lst)  # pointing to different addresses in all levels inside!

    def __repr__(self):
        """
        Overriding the print function of the object
        :return: what will be printing when printing object of Vector
        """
        return str(self.values_shallow)

    def __add__(self, vec):
        """
        Overriding the function that execute when adding to Vector objects with "+"
        :param vec:
        :return:
        """
        if not isinstance(vec, Vector) or len(vec.values_shallow) != len(self.values_shallow):
            raise ValueError("Wrong type or dimension")
        res_lst = []
        for i in range(len(self.values_shallow)):
            res_lst.append(self.values_shallow[i] + vec.values_shallow[i])
        return Vector(res_lst)  # Return new Vector object that is the sum of the two

    def __mul__(self, other):
        """
        dot product
        :param other:
        :return:
        """
        if isinstance(other, (int, float)):
            return Vector([other * x for x in self.values_shallow])
        if isinstance(other, Vector) and len(self.values_shallow) == len(other.values_shallow):
            return sum([self.values_shallow[i] * other.values_shallow[i] for i in range(len(self.values_shallow))])
        raise ValueError("Wrong type or dimensions")  # From here, rather than raise an error, it goes to __rmul__

    def __rmul__(self, other):
        """
        Turns the sides of the parameters that sends to __mul__
        :param other:
        :return:
        """
        return self * other  # calling to __mull__ magic method

    def __neg__(self):
        """
        negative of the object
        :return:
        """
        return Vector([-x for x in self.values_shallow])

    def __sub__(self, other):
        """
        add (we implemented) object and negative (we implemented) other
        :param other:
        :return:
        """
        return self + (-other)  # Using __add__ and __neg__

    def __len__(self):
        return len(self.values_shallow)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        return self.values_shallow == other.values_shallow

    def __getitem__(self, i):
        """
        Enable to use indexing on Vector object
        :param i: the index
        :return:
        """
        return self.values_shallow[i]


# -------------------------- Vector Class Functionality --------------------------
if __name__ == '__main__':
    lst = [3, 3, 7]
    vec1 = Vector(lst)
    lst.append(10)  # If lst changed -> also vec1.values changed
    print("Copy\n---------------")
    print("shallow copy: {}".format(vec1.values_shallow))
    print("copy: {}".format(vec1.values_copy))

    print("\nDeep Copy\n---------------")
    lst2 = [[1, 2], [3, 4]]
    vec2 = Vector(lst2)
    lst2[0].append(8)
    print("no copy: {}".format(vec2.values_shallow))
    print("copy: {}".format(vec2.values_copy))
    print("deep copy: {}".format(vec2.values_deep_copy))

    print("\n__repr__ method\n---------------")
    print(vec1)
    print(vec2)

    print("\n__add__ method\n---------------")
    # using the __add__ magic method
    vec3 = vec1 + vec1
    print("vec1 + vec1 = {}".format(vec1 + vec1))
    print("vec3 = {}".format(vec3))
    print("vec2 + vec2 = {}".format(vec2 + vec2))  # do not work for multidimensional

    print("\n__mul__ method\n---------------")
    # using the __mul__ magic method
    sum1 = vec1 * vec1
    print("vec1 * vec1 = {}".format(vec1 * vec1))
    print("sum1 = {}".format(sum1))
    print("vec1 * 3 = {}".format(vec1 * 3))
    print("vec1 * 3 = {}".format(3 * vec1))  # using the __rmul__ magic method

    print("\n__neg__ method\n---------------")
    # using the __sub__ magic method
    print("-vec1 = {}".format(-vec1))

    print("\n__sub__ method\n---------------")
    # using the __sub__ magic method
    vec3 = vec1 - vec1
    print("vec1 - vec1 = {}".format(vec1 - vec1))
    print("vec3 = {}".format(vec3))

    print("\n__len__ method\n---------------")
    # using the __len__ magic method
    print("len(vec1) = {}".format(len(vec1)))

    print("\n__eq__ method\n---------------")
    # using the __eq__ magic method
    print("vec1 == vec1: {}".format(vec1 == vec1))
    print("vec1 == vec2: {}".format(vec1 == vec2))

    print("\n__getitem__ method\n---------------")
    # using the __getitem__ magic method
    print("vec1[2]: {}".format(vec1[2]))
