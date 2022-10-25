def optimize_flowers_selection(flowers, budget):
    if budget == 0:
        return 0, 0
    memo_array = [[None for j in range(len(flowers))] for i in range(budget)]

    def optimize_flowers_selection_helper(possible_flowers, budget_left, fl_idx, memo_array):
        def get_least_expensive(with_fl, without_fl):
            return with_fl if with_fl[0] >= without_fl[0] else without_fl

        if budget_left == 0 or fl_idx < 0:
            return 0, budget_left
        if memo_array[budget_left - 1][fl_idx] is not None:
            return memo_array[budget_left - 1][fl_idx]
        if possible_flowers[fl_idx][2] > budget_left:
            return optimize_flowers_selection_helper(possible_flowers, budget_left, fl_idx - 1, memo_array)

        with_fl = optimize_flowers_selection_helper(possible_flowers, budget_left - possible_flowers[fl_idx][2],
                                                    fl_idx - 1, memo_array)
        with_fl = with_fl[0] + possible_flowers[fl_idx][1], with_fl[1]

        without_fl = optimize_flowers_selection_helper(possible_flowers, budget_left, fl_idx - 1, memo_array)
        memo_array[budget_left - 1][fl_idx] = get_least_expensive(with_fl, without_fl)
        return memo_array[budget_left - 1][fl_idx]

    return optimize_flowers_selection_helper(flowers, budget, len(memo_array[0]) - 1, memo_array)


flowers = [
    # flower_name , aesthetic_value, cost
    ("Lilac", 4, 3),
    ("Hibiscus", 2, 5),
    ("Tulip", 1, 1),
    ("Sunflower", 5, 2),
    ("Rose", 3, 4)
]
answer = optimize_flowers_selection(flowers, 4)
print("accumulated aesthetic value: {0}" \
      "\nRemaining budget: {1}".format(answer[0], answer[1]))
