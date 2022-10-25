from Examples_From_Class.Exceptions.Exceptions import exception_example
import unittest


class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


c = Calculator()


class TestTirgul8(unittest.TestCase):
    """
    Tests for Calculator class methods: logic error
    Test the exception_example function for different Errors
    """

    def test_add(self):
        self.assertEqual(c.add(2, 5), 7)
        self.assertEqual(c.add(0, 10), 10)
        self.assertEqual(c.add(-10, 10), 0)

    def test_sub(self):
        self.assertEqual(c.sub(100, 15), 85)
        self.assertEqual(c.sub(4, 10), -6)
        self.assertEqual(c.sub(0, 0), 0)
        self.assertEqual(c.sub(50, 50), 0)

    def test_mul(self):
        self.assertEqual(c.mul(0, 15), 0)
        self.assertEqual(c.mul(1, 10), 10)
        self.assertEqual(c.mul(3, 7), 21)
        self.assertEqual(c.mul(7, 3), 21)

    def test_div(self):
        self.assertEqual(c.div(75, 25), 3)
        self.assertEqual(c.div(0, 10), 0)
        self.assertEqual(c.div(7, 1), 7)
        self.assertEqual(c.div(10, 4), 2.5)

    def test_exception_example(self):
        self.assertEqual(exception_example([1, 2, 3], 2, 1),
                         (3, 0))  # If the function would not return (3,0) the test failed

        with self.assertRaises(TypeError):
            exception_example([1, 2, 3], 2,
                              1.0)  # If the function would not raise TypeError for this input, the test failed
        with self.assertRaises(ValueError):
            exception_example([1, 2, 3], 2,
                              5)  # If the function would not raise ValueError for this input, the test failed
        with self.assertRaises(IndexError):
            exception_example([1, 2, 3], 3,
                              1)  # If the function would not raise IndexError for this input, the test failed


unittest.main(argv=[''], verbosity=2, exit=False)
