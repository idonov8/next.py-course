def combine_coins(currency, numbers):
    return ", ".join([str(num) + currency for num in numbers])


# test
print(combine_coins("$", range(1,5))) # 1$, 2$, 3$, 4$