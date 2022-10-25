# *************** HOMEWORK 1 ***************
# GOOD LUCK!

# ************************ QUESTION 4 **************************
def question4(number):
    sum = 0
    for i in range(1, int(number / 2) + 1):
        if number % i == 0:
            sum += i
    print("True") if sum == number else print("False")


question4(6)  # 1 + 2 + 3
question4(21)
question4(28)  # 1 + 2 + + 4 + 7 + 14
question4(2)
question4(199)
