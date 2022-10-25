# Recursion Class
def LIS_slicing(lst):
    return longest_increasing_rec_slicing(lst, 0)


def longest_increasing_rec_slicing(lst, last_used):
    if len(lst) == 0:
        return 0
    with_next = 0
    if lst[0] > last_used:
        with_next = 1 + longest_increasing_rec_slicing(lst[1:], lst[0])
    without_next = longest_increasing_rec_slicing(lst[1:], last_used)
    return max(with_next, without_next)


def LIS_no_slicing(lst):
    return longest_increasing_rec_no_slicing(lst, 0, 0)


def longest_increasing_rec_no_slicing(lst, last_used, prog_index):
    if len(lst) - prog_index == 0:
        return 0
    with_next = 0
    if lst[prog_index] > last_used:
        with_next = 1 + longest_increasing_rec_no_slicing(lst, lst[prog_index], prog_index + 1)
    without_next = longest_increasing_rec_no_slicing(lst, lst[prog_index], prog_index + 1)
    return max(with_next, without_next)


# print(LIS_slicing([20, 20, 1, 232, 40, 41, 85, 90, 87, 88, 200]))
print(LIS_no_slicing([20, 20, 1, 232, 40, 41, 85, 90, 87, 88, 200]))
