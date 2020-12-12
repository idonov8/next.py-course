def intersection(list_1, list_2):
    return list({(num) for num in list_1 if num in list_2})

# test
print(intersection([1, 2, 3, 4], [8, 3, 9])) # [3]
print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6])) # [5,6]

