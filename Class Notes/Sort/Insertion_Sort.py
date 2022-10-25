# O(n^2)
def insertion_sort(lst):
    for i in range(1, len(lst)):  # Traverse through 1 to len(lst)
        value = lst[i]
        j = i - 1

        # Move elements of lst[0,...i-1], that are greater than value
        while j >= 0 and lst[j] > value:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = value


lst = [5, 1, 8, 6, 7]
insertion_sort(lst)
print(lst)
