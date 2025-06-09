n = [1,2,3,4,5,6,7,8,9,10]

pares = [ num  for num in n if num % 2 == 0]

print(pares)


impares = [ num for num in n if num % 2 != 0]

print(impares)

matrix = [[1,2,3, "a"], # esto rompe la transpuesta
          [4,5,6],
          [7,8,9]]


# transpuesta = [[fila[i] for fila in matrix] for i in range(len(matrix[0]))]
# print(transpuesta)


a = []
for i in range(len(matrix[0])):
    b = []
    for row in matrix:
        b.append(row[i])
    a.append(b)

print(a)



# doble de los numeros
a = [1,2,3,4,5]
doble = [n * 2 for n in a]
print(doble)

# filtrar y transformar en un paso
a = ["sol", "mar", "montaña", "rio", "estrella", "hola"]
mas_3_letras = [p for p in a if len(p) > 3]
print(mas_3_letras)

# crear un diccionario con list comprehension
a = ["nombre", "edad", "ocupacion", "a"]
b = ["Pepe", "30", "Ingeniero", "b"]
d = {c: v for c, v in zip(a, b)}
print(d)


if len(a) != len(b):
    raise ValueError("Las listas de claves y valores deben tener el mismo largo.")
d2 = {a[i]: b[i] for i in range(min(len(a), len(b)))}
print(d2)

# anidación de list comprehensions
m = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

t = [[r[i] for r in m] for i in range(len(m[0]))]
print(m)
print(t)

#extraer información de una lista de diccionarios
p = [
    {"nombre": "pepe", "edad": 35, "ciudad": "madrid"},
    {"nombre": "ana", "edad": 23, "ciudad": "madrid"},
    {"nombre": "Laura", "edad": 35, "ciudad": "bercelona"},
    {"nombre": "Pedro", "edad": 52, "ciudad": "madrid"},
]

lista_nombres_madrid = [per["nombre"] for per in p if per["ciudad"] == "madrid" and per["edad"] >= 30]
print(lista_nombres_madrid)

# list comprehension con un else

numeros = [1,2,4,5,6,7,8,9,10]

transformados = [x * 2 if x % 2 == 0 else x * 3 for x in numeros]
print(numeros)
print(transformados)