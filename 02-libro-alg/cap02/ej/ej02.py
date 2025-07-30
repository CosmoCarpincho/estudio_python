def suma_numeros(n: int) -> int:
    return 0 if n == 0 else n + suma_numeros(n - 1)

for i in range(13):
    print(suma_numeros(i))