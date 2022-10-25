from Exceptions import exception_example

try:
    a, b = exception_example([1, 2, 3], 2, 10)
except IndexError as e:
    print("IndexError Exception: ", e)
except TypeError as e:
    print("TypeError Exception: ", e)
except ValueError as e:
    print("ValueError Exception: ", e)
except Exception as e:
    print("Something else happened: ", e)
else:
    print(a, b)

print("")

try:
    a, b = exception_example([1, 2, 3], 2, 1.0)
except Exception as e:
    print("Exception has occurred!")
    print(e)
    print(type(e))
else:
    print(a, b)

print("")
try:
    a, b = exception_example([1, 2, 3], 2, 1.0)
except:
    print("Exception has occurred!")
else:
    print(a, b)
