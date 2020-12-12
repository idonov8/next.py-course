from functools import reduce
print(reduce(lambda a, b: a if len(a)>len(b) else b,[name for name in open('names.txt').read().split()]),"")