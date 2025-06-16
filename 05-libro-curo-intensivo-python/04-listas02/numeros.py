import numpy as np

# 4-6 números impares
num_impares = list(range(1, 21, 2))
for impar in num_impares:
    print(impar)

# multiplos de 3
print("\nMultiplos de 3\n")
multiplos_tres = [n for n in range(1, 31) if n % 3 == 0]
for mult_tres in multiplos_tres:
    print(mult_tres)

multiplos_tres_2 = list(range(3, 31, 3))
print(multiplos_tres_2)

multiplos_tres_3 = list(filter(lambda x: x % 3 == 0, range(1, 31)))
print(multiplos_tres_3)

# numpy
multiplos_tres_4 = np.arange(3, 31, 3).tolist()
print(multiplos_tres_4)

# cubos
cubos = []
for c in range(1,11):
    cubos.append(c ** 3)

print(cubos)

cubos_2 = [n ** 3 for n in range(1, 11)]
print(cubos_2)

cubos_3 = list(map(lambda x: x ** 3, range(1, 11)))
print(cubos_3)

nombres = ["cosmo", "pepe", "ana"]
print(list(map(lambda x: "Hola " + x, nombres)))

cubos_4 = (np.arange(1, 11) ** 3).tolist()
print(cubos_4)