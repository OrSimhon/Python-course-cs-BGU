# *************** HOMEWORK 1 ***************
# GOOD LUCK!

# ************************ QUESTION 1 **************************
def question1(number):
    num_minus_20 = number - 20
    print("{0:.2f}".format(num_minus_20 ** 0.5)) if num_minus_20 >= 0 else print("imaginary result")


question1(5)
question1(25)
question1(100)
question1(75.5)
question1(0)
question1(20)
question1(-5)
