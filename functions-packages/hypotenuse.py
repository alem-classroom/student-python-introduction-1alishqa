import math

def get_hypotenuse(catet1, catet2):
    res = catet1 * catet1 + catet2 * catet2
    return math.sqrt(res)
    # calculate hypotenuse of right triangle based on 2 catets and return it

# print(get_hypotenuse(6, 9))