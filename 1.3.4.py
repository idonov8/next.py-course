password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
print("".join(map(lambda char: chr(ord(char)+2) if 97<=ord(char)<=122 else char, password)))
