# Greedy Approximation Solution
def greedy_fruit(items, capacity):
    items = sorted(items, key=lambda item: item[1] / item[2], reverse=True)  # sort by weight
    chosen_fruits = {}
    profit = 0
    for i in range(len(items)):
        name, value, weight = items[i]
        num_of_fruit = capacity // weight
        chosen_fruits[name] = num_of_fruit
        capacity -= num_of_fruit * weight
        profit += num_of_fruit * value
    return round(profit, 2), chosen_fruits


# Dynamic Programming Solution
def dynamic_fruit(items, capacity):
    bag = [0 for i in range(capacity + 1)]
    for i in range(capacity + 1):
        for j in range(len(items)):
            _, value, weight = items[j]
            if weight < i:
                bag[i] = max(bag[i], bag[i - weight] + value)
    return round(bag[capacity])


items = [('avocado', 2.2, 170), ('pomelo', 8, 1500), ('durian', 22, 1500),
         ('cucamelon', 0.26, 15), ('lychee', 0.4, 20), ('star apple', 1, 200)]
print(greedy_fruit(items, 2000))
print(dynamic_fruit(items, 2000))
