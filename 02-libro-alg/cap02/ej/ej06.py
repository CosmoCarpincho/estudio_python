def invertir(texto: str) -> str:
    if len(texto) <= 0:
        return ""

    cabeza = texto[0]
    cola = texto[1:]
    return invertir(cola) + cabeza

print(invertir("Hola"))
print(invertir(""))
print(invertir("que onda la banda como andan?"))