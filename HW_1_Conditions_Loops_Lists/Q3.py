# *************** HOMEWORK 1 ***************
# GOOD LUCK!

# ************************ QUESTION 3 **************************
def question3(lst):
    min_odd_lst = []
    min_even_lst = []
    len_sub = len(lst)

    for i, num in enumerate(lst):
        if num == 0:
            len_sub = i

    for num in lst[:len_sub]:
        if num % 2 == 0:
            if len(min_even_lst) == 0:
                min_even_lst.append(num)
            elif len(min_even_lst) == 1:
                min_even_lst.append(num)
            elif num < min_even_lst[0]:
                min_even_lst[0] = num
            elif num < min_even_lst[1]:
                min_even_lst[1] = num
        else:
            if len(min_odd_lst) == 0:
                min_odd_lst.append(num)
            elif len(min_odd_lst) == 1:
                min_odd_lst.append(num)
            elif num < min_odd_lst[0]:
                min_odd_lst[0] = num
            elif num < min_odd_lst[1]:
                min_odd_lst[1] = num

    print((sum(min_even_lst) + sum(min_odd_lst)) / 4)


question3([1, 2, 3, 4, 5, 6, 0, 7, 8])
question3([1000, 1, 50, 49, 63, 64, 0, -80, 50])
question3([34, 23, 55, 151, 777, -30, 0, 1, 2, 3, 4])
