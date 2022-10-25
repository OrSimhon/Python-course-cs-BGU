class SmallValueError(Exception):
    """ Raised when input value is too small"""
    pass


def divide(x, y):
    if y < -10:
        raise SmallValueError("y is smaller than -10")
    print(x / y)


try:
    divide(50, -10)
except:
    print("keep on running")
else:
    print("Enter else")
