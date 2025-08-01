# set

empty_set = set()

some_set = {1, 1, 2, 2, 3, 4}
print(some_set)

# los elementos de set deben ser inmutable
invalid_set = {[1], 1} # TypeError: unhashable type: 'list'
valid_set = {(1,), 1}

valid_set.add(2)
valid_set.add(2)
print(valid_set)

# interseccion
a = {1,2,3,4,5}
b = {3,4,5,6,8,9}

r = a & b
print(r)

# union
r = a | b
print(r)

# difference
a = {1,2,3,4,5}
b = {4,5}
c = a - b
print(c)

# diferencia simetrica??
# estan en a o en b pero no en ambos. (se escribe con un triangulo en matematicas)
# a \triangulo b = (a U b) - (a \interseccion b)
d = a ^ b
print(d)