# Recursion Class
def choose(n, k):
    if k == 0 or n == k:
        return 1
    return choose(n - 1, k - 1) + choose(n - 1, k)


def choose_memo(n, k):
    return choose_memo_helper(n, k, {})


def choose_memo_helper(n, k, results_dict):
    if k == 0 or n == k:
        return 1
    if (n, k) not in results_dict:
        results_dict[(n, k)] = choose_memo_helper(n - 1, k - 1, results_dict) + choose_memo_helper(n - 1, k,
                                                                                                   results_dict)
    return results_dict[(n, k)]


print(choose(4, 2))
print(choose(4, 3))
print(choose(6, 4))
print("")
print(choose_memo(4, 2))
print(choose_memo(4, 3))
print(choose_memo(6, 4))
