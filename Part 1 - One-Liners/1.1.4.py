from functools import reduce

def sum (num1, num2):
    return int(num1) + int(num2)

def sum_of_digits(number):
    return reduce(sum, str(number))

# test
print(sum_of_digits(104)) # 5