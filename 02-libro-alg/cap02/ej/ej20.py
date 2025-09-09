# 20. Desarrollar un algoritmo que permita implementar la búsqueda secuencial con centinela de manera recursiva, y permita determinar si un valor dado está o no en dicha lista.

def busqueda_secuencial_sentinela(arreglo: list, objetivo):
    if not arreglo:
        print("Esta vacio")
        return 

    if arreglo[-1] != objetivo:
        arreglo = arreglo + [objetivo]

    if arreglo[0] == objetivo:
        resultado = len(arreglo) > 1
        return resultado
    
    return busqueda_secuencial_sentinela(arreglo[1:], objetivo)


arreglo = [1,2,3,4,5,6,7]

# print(busqueda_secuencial_sentinela(arreglo, 4))
# print(busqueda_secuencial_sentinela(arreglo, 9))
print(busqueda_secuencial_sentinela([], 9))