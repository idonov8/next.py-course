from functools import reduce
print(reduce(lambda a, b: a + len(b),open('names.txt').read().split(),0))
