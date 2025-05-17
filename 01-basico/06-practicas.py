# listas

a = ["hola", 2, 3, 4.5]
print(a)

print(f"primer elemento: {a[0]}, segundo elemento: {a[1]}")
a.append("agrega al final")
a.insert(3, "agega en 2 lugar")
print(a)
b = a.pop()
print(f"pop quita el ultimo elemento: {b} ->> arreglo actual {a}")

print(a[2:-1])
print(a[:3])
print(a[3:])

#para copia superficial
mi_slice = a[:]

print(mi_slice)

lista_num = [1, 52, 2 ,56 ,2.5, 2, 2]
print(min(lista_num))
print(max(lista_num))

print(lista_num.remove(2)) # remueve el primero
print(lista_num)

for i, e in enumerate(lista_num):
    print(f"i: {i} e: {e}")

l1 = ["a", "b", "c"]
l2 = ["1", "2", "3"]


for e1, e2 in zip(l1, l2):
    print(e1, e2)

listzip = list(zip('abcdefg', ["cosmo", "carpincho", "prog"], range(4)))
print(listzip)

# sin copia

z1 = [1,2,3]
z2 = z1 # es sin copia porque los dos hacen referencia al la misma lista.
z1.append(4)

print(f"z1: {z1}, z2: {z2}")
# copia superficial vs copia profunda

#superficial
z3 = z1[:] 
z1.append(5)
print(f"z1: {z1}, z2: {z2}, z3: {z3}")


p1 = [["a","b"],[1,2]]
p2 = p1[:] #copiad superficial
p3 = p1.copy() #copia superficial


# importar
import copy
p4 = copy.deepcopy(p1) #copia profunda

p1[0][0] = "nuevo"
print(f"p1: {p1}, p2: {p2}")
print(f"p1: {p1}, p2: {p2}, p3: {p3}, p4: {p4}")

# matrices y tuplas

m1 = [[1,2,3],
      [4,5,6]]

t1 = ((1,2,3),
      (4,5,6))

print("m1:", m1, "t1", t1)

