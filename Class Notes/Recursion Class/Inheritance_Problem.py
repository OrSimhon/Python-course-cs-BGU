# Recursion Class
def partition(lst):
    return partition_helper(lst, 0, 0)


def partition_helper(lst, liora, yosi):
    if not lst:
        return liora == yosi
    return partition_helper(lst[1:], liora + lst[0], yosi) or partition_helper(lst[1:], liora, yosi + lst[0])


def partition_memo(lst):
    return partition_memo_helper(lst, 0, 0, {})


def partition_memo_helper(lst, s1, s2, memo):
    if not lst:
        return s1 == s2
    key = (len(lst), s1, s2)
    if key not in memo:
        give_liora = partition_memo_helper(lst[1:], s1 + lst[0], s2, memo)
        give_Yosi = partition_memo_helper(lst[1:], s1, s2 + lst[0], memo)
        memo[key] = give_liora or give_Yosi
    return memo[key]


print(partition([9, 6, 3]))
print(partition([9, 6, 2]))
print(partition([9, 6, 2, 1, 5, 7, 1, 11, 2]))

print("")

print(partition_memo([9, 6, 3]))
print(partition_memo([9, 6, 2]))
print(partition_memo([9, 6, 2, 1, 5, 7, 1, 11, 2]))
