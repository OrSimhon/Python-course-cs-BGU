"""
List comprehension
"""
numbers = [1, 2, 3, 4, 5]
squares_lst = [n ** 2 for n in numbers]
print(squares_lst)
print(type(squares_lst))

"""
Generator
"""
print()
numbers = [1, 2, 3, 4, 5]
squares = (n ** 2 for n in numbers)
print(squares)
print(type(squares))
print(tuple(squares))
print(tuple(squares))

"""
Dictionary
"""
print()
counts = {'apples': 2, 'oranges': 1}
x, y = counts
print(x)
print(y)

"""
Iterables:
An iterable is anything you can loop over with a for loop in Python.
Iterables and also Sequences ADT: List, String Tuples
Iterables but Not Sequences ADT: Set, Dictionary
More Iterables: Generator, Iterator, Range
"""

"""
Iterators are the things that power iterables. 
You can get an iterator from any iterable.
You can use an iterator to manually loop over the iterable it came from.
"""
print()
numbers = {1, 2, 3, 4, 5, 7}
coordinates = (4, 5, 7)
words = "hello there"
print(iter(numbers))
print(iter(coordinates))
print(iter(words))

# Iterator example

numbers = [1, 2, 3]
my_iterator = iter(numbers)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
