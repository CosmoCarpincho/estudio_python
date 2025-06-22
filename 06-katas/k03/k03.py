# https://www.codewars.com/kata/565b9d6f8139573819000056

import string

def decode(message):
    a1 = list(string.ascii_lowercase)
    d = {}
    i = 0
    while i < len(a1):
        d[a1[i]] = a1[len(a1) - i -1]
        i += 1
        
    trad = ""    
    for l in message:
        if l in string.whitespace:
            trad += l
        else:
            trad += d[l]
    return trad


print(f"whitespace: {string.whitespace}")
print(f"punctuation: {string.punctuation}")
print(f"ascii_uppercase: {string.ascii_uppercase}")
print(f"ascii_letters: {string.ascii_letters}")
print(f"ascii_lowercase: {string.ascii_lowercase}")
print(f"digits: {string.digits}")
print(f"printable: {string.printable}")

# crear un diccionario donde se mapea primer letra con ultima

a1 = list(string.ascii_lowercase)
i = 0
d = {}
while i < len(a1):
    # print(i, len(a1))
    d[a1[i]] = a1[len(a1) - i - 1]
    i += 1

print(d)

message = "r slkv mlylwb wvxlwvh gsrh nvhhztv"
trad = ""
for l in message:
    if l in string.whitespace:
        trad += l
    else:
        trad += d[l]

print(trad)

string.ascii_lowercase.translate()
