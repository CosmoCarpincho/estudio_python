# copiar listas en python
# listas por referencia

a = [1,2,3,4,5]
b = a

a.insert(0, "hola")
print(b) # ["hola",1,2,3,4,5]

# ver dirección de memoria
print(id(a)) #1736451336448
print(id(b))  #1736451336448

# para copiar datos hay que usar slices
del a[0] # [1,2,3,4,5]
c = a[0:]
a.insert(0, "hola")
print(c)

print(id(a)) #1736451336448
print(id(c)) #1736453210304

# otra forma de copiar todo
d = a[:]