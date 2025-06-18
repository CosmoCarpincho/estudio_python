# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/python
def duplicate_encode(word):
    r = ""
    word = [w.lower() for w in word]
    for w in word:
        if word.count(w) > 1:
            r += ")"
        else:
            r += "("
    return r

print(duplicate_encode("Success"))
print(duplicate_encode('(( @"),"))(('))

