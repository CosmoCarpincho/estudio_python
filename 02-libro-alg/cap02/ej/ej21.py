# Dada una lista de valores ordenadas, desarrollar un algoritmo que modifique el método de búsqueda binaria para que funcione de forma recursiva, y permita determinar si un valor dado está o no en dicha lista.

# Busqueda binaria

def busqueda_binaria(arreglo, objetivo):
    if len(arreglo) == 1 and objetivo != arreglo[0]:
        return False
    elif arreglo[0] == objetivo:
        True

    pos = len(arreglo) // 2
    contenido = arreglo[pos]

    if contenido == objetivo:
        return True

    if contenido < objetivo:
        return busqueda_binaria(arreglo[pos:], objetivo)
    elif contenido > objetivo:
        return busqueda_binaria(arreglo[:pos], objetivo)
    

a1 = [1,2,3,4,5,6,7,8,9]
a2 = [1,5,7,9,11]

print(busqueda_binaria(a1, 4))
print(busqueda_binaria(a2,1))
print(busqueda_binaria(a2,11))
print(busqueda_binaria(a2,7))
print(busqueda_binaria(a2,3))