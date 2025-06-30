# Operadores de conjuntos

conjunto = {1,2,4,5,6,1}

print(conjunto)

# interseccion
a = {1,2,3}
b = {3,4,5}

r = a.intersection(b)
print(r)

r2 = set.intersection(a,b)
print(r2)

# existe

print(2 in a)

a = set('abracadabra')
b = set('alacazam')

print(a)
print(b)

print("a - b", a - b) # resta de conjuntos
print("a | b", a | b) # union
print("a & b", a & b) # interseccion
print("a ^ b", a ^ b) # en a o b pero no en ambas

vacio = set()
print(vacio)


