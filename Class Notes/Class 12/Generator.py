"""
An iterator in Python serves as a holder for objects so that they can be iterated over.
A generator facilitates the creation of a custom iterator.

Iterator:
        Implemented using a class.
        Does not use the yield keyword.
Generator:
        Implemented using a function.
        Uses the yield keyword.
"""


# --------------------------- Iterator --------------------------- #
class square_all_it:
    def __init__(self, numbers):
        self.numbers = iter(numbers)

    def __next__(self):
        return next(self.numbers) ** 2

    def __iter__(self):
        return self


my_numbers = [x for x in range(10)]
squares_iterator = square_all_it(my_numbers)  # Like map and filter, but not inheritance iterator
print(squares_iterator)
print(next(squares_iterator))
print(next(squares_iterator))
print(next(squares_iterator))
print(next(squares_iterator))
print(next(squares_iterator))
print(next(squares_iterator))

print()


# --------------------------- Generator example --------------------------- #
def square_all_gen(numbers):
    for n in numbers:
        yield n ** 2  # Freeze function and trturn value, when calling again will continue from here


squere_all_gen = square_all_gen(my_numbers)
print(squere_all_gen)
print(next(squere_all_gen))
print(next(squere_all_gen))
print(next(squere_all_gen))
print(next(squere_all_gen))
print(next(squere_all_gen))
print(next(squere_all_gen))

# --------------------------- Generator example --------------------------- #

print()
square_all_gen2 = (n ** 2 for n in my_numbers)
print(square_all_gen2)
print(next(square_all_gen2))
print(next(square_all_gen2))
print(next(square_all_gen2))
print(next(square_all_gen2))
print(next(square_all_gen2))
print(next(square_all_gen2))

# --------------------------- Generator example --------------------------- #
print()
numbers = [1, 2, 3, 5, 7]
squares = (n ** 2 for n in numbers)
print(9 in squares)
print(list(squares))
print(list(squares))
