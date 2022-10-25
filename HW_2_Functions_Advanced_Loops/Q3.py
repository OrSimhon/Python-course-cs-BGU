# *************** HOMEWORK 2 ***************
# GOOD LUCK!

# ************************ QUESTION 3 **************************
def max_series(numbers):
    divided_by_three = -1
    odd_nums = []
    idx = 0
    increase = True

    for num in numbers:
        if num % 2 != 0:  # Odd num
            if len(odd_nums) == 0:
                odd_nums.append(num)
                idx += 1
            elif num > odd_nums[idx - 1] and increase:
                odd_nums.append(num)
                idx += 1
            else:
                increase = False
        if num % 3 == 0 and num > divided_by_three:
            divided_by_three = num

    return [idx, divided_by_three]


print(max_series([1, 3, 13, 3, 0, 4, 6, 8, 22]))
print(max_series([0, 4, 6, 6, 7, 8, 13, 2, 3, 5, 10, 15, 9, 2]))
print(max_series([2, 4, 8, 10]))
