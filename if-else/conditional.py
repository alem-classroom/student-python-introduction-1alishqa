import random

def is_positive(num):
    if num > 0:
        return True
    else:
        return False
    # return true if num is positive, otherwise return false

def is_even(num):
    if (num % 2 == 0):
        return True
    else:
        return False
    # return true if num is even, otherwise return false

def is_positive_and_even(num):
    if (is_positive(num) and is_even(num)):
        return True
    else:
        return False
    # return true if num is positive and even, otherwise return false

def is_positive_or_even(num):
    if (is_positive(num) or is_even(num)):
        return True
    else:
        return False
    # return true if num is positive or even, otherwise return false

# number = random.randint(-1000, 1000)
# print(number)
# print(is_positive(number))
# print(is_even(number))
# print(is_positive_and_even(number))
# print(is_positive_or_even(number))