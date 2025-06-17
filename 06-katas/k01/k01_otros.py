# otras soluciones

def d1(n):
    return n if n < 10 else d1(sum(map(int,str(n))))

def d2(n):
    if n < 10:
        return n

    n = str(n) # convertir en string ej "936"
    n = map(int, str(n)) # mapea que para cada caracter ahora sea un int PERO DEVUELVE UN OBJETO MAP??
    n = sum(n)
    n = d2(n)
    return n

print(d2(936))


def d3(n):
    return n%9 or n and 9

print(d3(936))


def d3_explicado(n):
    """
        Usa teorema de la raíz digital:
        la raíz digitan de un número en base 10 es congruente con ese número módulo 9 salvo para los múltiplos de 9
        digital_root(n) ->  9       , si n != 0 y n mod 9 = 0
                            n mod 9 , en otro caso
        n = 942
        942 mod 9 = 6
        raíz digital = 6

        n = 729
        729 mod 9 = 0 pero 720 != 0
        raíz digital = 9
    """
    resultado = n % 9


    if resultado == 0 and n != 0:
        resultado = 9
    return resultado

print(d3_explicado(942))
print(d3_explicado(729))