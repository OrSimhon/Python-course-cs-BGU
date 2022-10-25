# *************** HOMEWORK 2 ***************
# GOOD LUCK!

# ************************ QUESTION 2 **************************
def lagrange_four_square_theorem(num):
    lst = []
    for i in range(int(num ** 0.5) + 1):
        for j in range(int(num ** 0.5) + 1):
            for k in range(int(num ** 0.5) + 1):
                for t in range(int(num ** 0.5) + 1):
                    if (i ** 2 + j ** 2 + k ** 2 + t ** 2) == num and sorted([i, j, k, t]) not in lst:
                        lst.append(sorted([i, j, k, t]))
    return lst


print(lagrange_four_square_theorem(5))
print(lagrange_four_square_theorem(36))
print(lagrange_four_square_theorem(100))
