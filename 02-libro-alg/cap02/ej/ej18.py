#18. Implementar una función recursiva que permita recorrer una matriz y mostrar sus valores.

matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

def mostrar(m):
    if not m:
        return
    
    if isinstance(m[0], list):
        mostrar(m[0])
        mostrar(m[1:])
    else:
        print(m[0])
        mostrar(m[1:])

mostrar(matriz)
print("===")
mostrar([1,2,3])
mostrar([])