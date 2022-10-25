# *************** HOMEWORK 1 ***************
# GOOD LUCK!

# ************************ QUESTION 2 **************************
def question2(k):
    count = 0
    x = 2
    while True:
        if isPrime(x):
            count += 1
        if count == k:
            print(x)
            return
        x += 1


def isPrime(num):
    prime = True
    for i in range(2, int(num/2 + 1)):
        if num % i == 0:
            prime = False
    return prime


question2(1)
question2(2)
question2(5)
question2(27)
question2(50)
