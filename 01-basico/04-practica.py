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


# matrices y tuplas
matrix = [[1,2,3],
          [4,5,["a","b"]]]

tupla = ((1,2,3),
         (4,5,["a", "b"]))

print(f"matrix: {matrix}\ntupla: {tupla}")
# matrix: [[1, 2, 3], [4, 5, ['a', 'b']]]
# tupla: ((1, 2, 3), (4, 5, ['a', 'b']))

# las matrices son mutables, las tuplas no lo son
# pero si dentro de una tupla pones un array
# como guarda la referencia si se puede editar
# por lo tanto ese array interno es mutable


matrix[1][2] = 6
tupla[1][2][0] = "Hola"
print(f"matrix: {matrix}\ntupla: {tupla}")
# matrix: [[1, 2, 3], [4, 5, 6]]
# tupla: ((1, 2, 3), (4, 5, ['Hola', 'b']))