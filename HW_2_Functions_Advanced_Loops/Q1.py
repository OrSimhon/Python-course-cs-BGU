# *************** HOMEWORK 2 ***************
# GOOD LUCK!

# ************************ QUESTION 1 **************************
def rhombus(side_size):

    for i in range(int((side_size * 2 - 1) / 2)):
        print(end=' ' * (side_size - i - 1))
        print("*" * (i * 2 + 1))

    print("*" * (side_size * 2 - 1))

    for i in reversed(range(int((side_size * 2 - 1) / 2))):
        print(end=' ' * (side_size - i - 1))
        print("*" * (i * 2 + 1))


print('---1---')
rhombus(1)
print('---2---')
rhombus(2)
print('---5---')
rhombus(5)
print('---8---')
rhombus(8)
