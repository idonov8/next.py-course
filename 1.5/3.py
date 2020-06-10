# 1st solution
from functools import reduce
def printy(a):
    print(a)
map(printy, filter(lambda a: len(a)==2,[filter(lambda a: len(name)>len(a), open('names.txt').read().split()) for name in open('names.txt').read().split()])[0])

# 2nt solution
print("\n".join(sorted(open('names.txt').read().split(), key=lambda a: len(a))[:2]))