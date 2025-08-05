# 11. Desarrollar un algoritmo que invierta un número entero sin convertirlo a cadena.
def invertir_numero(n:int) -> int:
    if n < 10:
        return n
    
    ultimo = n % 10
    otro = n // 10

    # 2345 -> 5432
    return int(str(ultimo) + str(invertir_numero(otro)))

print(invertir_numero(123))
print(invertir_numero(12345))
print(invertir_numero(4529))
print(invertir_numero(14592))