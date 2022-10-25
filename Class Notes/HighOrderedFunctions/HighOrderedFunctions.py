# High-order functions are functions that take other functions as arguments

def my_comparator(string): return len(string), string


names = ["Avocado", "Apple", "Banana", "apple", "Baboon"]
print(sorted(names, key=my_comparator))  # Sort first by len and then by string (climatography)

"""
Three predefined higher-order functions are especially useful
For working with lists (but it can work on every "iterable")
map, reduce, filter
"""

"""
map
map(function, sequence) calls functions(item) for each of the sequence's
items and returns a list of the return values.
"""


def cube(x): return x ** 3


print(map(cube, range(10)))
print(list(map(cube, range(10))))
print(type(map(cube, range(10))))


def calc_sum(x1, x2): return x1 + x2


print(list(map(calc_sum, [1, 2, 3, 4, 5], [10, 20, 30])))

"""
filter
filter(function, sequence) returns a sequence consisting of those 
items from the sequence for which function(item) is true.
The function must return 1 bool value.
"""


def is_above_70(x): return x > 70


grades = [55, 82, 47, 95, 88, 68, 99]
print(filter(is_above_70, grades))
print(grades)
print(list(filter(is_above_70, grades)))
print(type(filter(is_above_70, grades)))

"""
reduce
reduce(func, sequence) returns a single value constructed by
calling the binary func on the first two items of the sequence,
then on the result and the next item, and so on.
The function needs to be imported
The function used as a parameter should receive 2 parameter 
itself and return 1 value
"""
from functools import reduce


def add_nums(x, y): return x + y


print(reduce(add_nums, range(11)))
print(type(reduce(add_nums, range(11))))
print(reduce(add_nums, range(10), 10))

"""
Anonymous Functions: lambda
lambda function can take any number of arguments but return
only one expression (calculated argument)
lambda arguments: expression
"""
print((lambda x, y: x ** y)(4, 5))
squared = lambda x, y: x ** y
print(squared(4, 5))
