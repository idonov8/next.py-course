length = input("Enter name length: ")
print("\n".join(filter(lambda a: len(a)==length, open('names.txt').read().split())))