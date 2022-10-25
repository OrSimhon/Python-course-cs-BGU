"""
Decorator
Adding additional functionality to functions.
Can be coded as wrapper functions which receive the "wrapped" function as input.
Built-in Decorators are abundant in python.
"""


# Manually
def print_with_prefix() -> None:
    print("This does something")


def decorate_any_print(func1) -> None:
    def inner():
        print('#######################')
        func1()
        print('#######################')

    return inner


pretty = decorate_any_print(print_with_prefix)
pretty()

# Using Decorator
print()


def decorate_any_print2(func1) -> None:
    def inner():
        print('#######################')
        func1()
        print('#######################')

    return inner


@decorate_any_print  # call decorate_any_print and send the following function to it
def print_with_prefix2() -> None:
    print("This does something")


print_with_prefix2()


# --------------------------- Decorator example: with arguments --------------------------- #
def protect_from_zero(func):
    def inner(a, b):
        if b == 0:
            print("b cant be 0, protecting!")
            b = 1
        return func(a, b)

    return inner


@protect_from_zero
def division_without_remainder(a: int, b: int):
    return int(a / b)


# --------------------------- Decorator example: generalized --------------------------- #
def works_for_all(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)

    return inner


# --------------------------- Decorator example: generalized --------------------------- #
def star(func):
    def inner(*args, **kwargs):
        print("*" * 3)
        func(*args, **kwargs)
        print("*" * 3)

    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 3)
        func(*args, **kwargs)
        print("%" * 3)

    return inner


@percent
@star
def printer(msg):
    print(msg)


print()
printer("Hello")

# --------------------------- Decorator example: lru_cache --------------------------- #
print()
from functools import lru_cache

num_of_calls = 0


@lru_cache(maxsize=20)  # Memoization: FIFO of up to 20 calls
def factorial(n):
    global num_of_calls
    num_of_calls += 1
    return n * factorial(n - 1) if n else 1


factorial(10)
print(num_of_calls)
num_of_calls = 0
factorial(11)
print(num_of_calls)
num_of_calls = 0
factorial(8)
print(num_of_calls)
num_of_calls = 0
factorial(30)
print(num_of_calls)
num_of_calls = 0
factorial(8)
print(num_of_calls)