def is_divisible(num):
    return num % 4 == 0

def four_dividers(number):
    return list(filter(is_divisible, range(1,number)))

# test
print(four_dividers(9)) # [4, 8]
print(four_dividers(3)) # []