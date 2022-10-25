def exception_example(lst, i, value):
    if i >= len(lst):
        raise IndexError("Given index is greater that list length")
    if type(value) != int:
        raise TypeError("Given type is not int")
    if value not in lst:
        raise ValueError("Given value is not in list")
    return lst[i], lst.index(value)


if __name__ == '__main__':
    a, b = exception_example([1, 2, 3], 2, 1.0)
    print(a, b)
