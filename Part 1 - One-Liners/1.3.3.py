
def is_funny(string):
    return len(string)>0 and len(filter(lambda x: x!='h' and x!='a',string))<1

print(is_funny("hahahahahaha")) # True
print(is_funny("not funny")) # False
print(is_funny("")) # False