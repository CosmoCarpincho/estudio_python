# secuencia de numeros


for n in range(1, 11):
    print(n)

numeros = list(range(1, 11))
print(numeros)

# funciones de agregación

print(f"suma: {sum(numeros)}")
print(f"numero menor: {min(numeros)}")
print(f"numeros mayor: {max(numeros)}")

# listas por compreción

cuadrados = [valor ** 2 for valor in range(1, 11)]
print(cuadrados)