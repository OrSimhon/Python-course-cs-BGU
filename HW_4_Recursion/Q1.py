def fibonacci_chars(n, k):
    def fibonacci_chars_helper(n):
        if n == 0:
            return 'a'
        if n == 1:
            return 'bc'
        return fibonacci_chars_helper(n - 2) + fibonacci_chars_helper(n - 1)

    return fibonacci_chars_helper(n)[k]


print(fibonacci_chars(n=4, k=2))
print(fibonacci_chars(n=5, k=8))
