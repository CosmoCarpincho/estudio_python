# algoritmo de Euclides

def mcd_euclides(num1: int, num2: int) -> int:
    dividendo = num1 // num2
    resto = num1 % num2
    if resto == 0:
        return num2
    return mcd_euclides(num2, resto)

print(mcd_euclides(12, 8))
print(mcd_euclides(2366, 273))

# 14
def mcm_euclides(a: int, b: int) -> int:
    c = mcd_euclides(a, b)
    aux = (a * b ) // c
    return aux

print(f"mcm {mcm_euclides(12, 8)}")