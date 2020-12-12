def duplicate(letter):
    return str(letter*2)

def double_letter(my_str):
    return "".join(map(duplicate, my_str))

# test
print(double_letter("python")) # ppyytthhoonn
print(double_letter("we are the champions!")) # wwee  aarree  tthhee  cchhaammppiioonnss!!