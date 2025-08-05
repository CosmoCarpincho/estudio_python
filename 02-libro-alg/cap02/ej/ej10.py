# 10. Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero. (recursivo)
def contar_digitos(n: int):
    if n == 0:
        return 1
    if n < 0 :
        n = n*-1
    if n < 10:
        return 1
    return 1 + contar_digitos(n // 10)

print(contar_digitos(123))
print(contar_digitos(1234))
print(contar_digitos(12345))
print(contar_digitos(123456))
print(contar_digitos(-123))
print(contar_digitos(-1234))
print(contar_digitos(-12345))
print(contar_digitos(-123456))
print(contar_digitos(-1000))
print(contar_digitos(-0))
print(contar_digitos(0))