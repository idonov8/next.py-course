from functools import reduce

def is_prime(number):
    return reduce(lambda a, b: a and b,[False for num in range(2,number) if number%num==0],True)

# test
print(is_prime(42)) # False
print(is_prime(43)) # True


