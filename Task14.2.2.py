# Написать функцию, которая будет перемножать любое количество переданных ей аргументов.

def multiple(*nums):
    mult_ = 1
    for n in nums:
        mult_ = n * mult_

    return mult_

print(multiple(2, 2, 9))