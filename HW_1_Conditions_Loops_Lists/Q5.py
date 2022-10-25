# *************** HOMEWORK 1 ***************
# GOOD LUCK!

# ************************ QUESTION 5 **************************
def question5(str):
    """
    string is immutable
    :param str:
    :return:
    """
    if len(str) < 4:
        print(str)
        return

    new_str = str[:-3] + str[-3:].upper()
    print(new_str)


question5("Hi")
question5("Cat")
question5("Happy")
question5("good")
question5("dog")
