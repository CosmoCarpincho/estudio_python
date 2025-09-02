# 17. Escribir una función recursiva que permita mostrar los valores de un vector de atrás hacia adelante.

vector = [1,2,3,4,5,6,7]

def mostrar(v):
    if len(v) == 1:
        print(v[0])
        return
    elif len(v) == 0:
        print("No hay elementos")
        return
    print(v[-1])
    mostrar(v[:-1])

mostrar(vector)
print(vector)
