def squares(x):
    return x ** 2


def funky_for_loop(iterable, action_to_do):
    for item in iterable:
        print(action_to_do(item))


def funky_for_loop_iter(iterable, action_to_do):
    """
    The code pretty much defines the way looping works under the hood in Python
    :param iterable:
    :param action_to_do:
    :return:
    """
    iterator = iter(iterable)
    done_lopping = False
    while not done_lopping:
        try:
            item = next(iterator)
        except StopIteration:
            done_lopping = True
        else:
            print(action_to_do(item))


numbers = [1, 2, 3]
funky_for_loop(numbers, squares)
print()
funky_for_loop_iter(numbers, squares)


class Count:
    """
    Iterator that counts
    """

    def __init__(self, start=0, end=10):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            current = self.start
            self.start += 1
            return current
        raise StopIteration


print()
count = Count(-2, 10)
next(count)
next(count)
for n in count:
    print(n)

print()
print(next(count))  # Error
