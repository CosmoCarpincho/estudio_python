# ej14 suma de dígitos de un número entero.
# siempre devuelve positivo
def sum_digitos(num):
    
    if num < 0:
        num = num * -1
    if num < 10:
        return num
    return num % 10 + sum_digitos(num // 10)

print(sum_digitos(123456))