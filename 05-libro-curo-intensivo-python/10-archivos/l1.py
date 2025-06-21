from pathlib import Path

# archivo = Path('05-libro-curo-intensivo-python/10-archivos/pi_digits.txt')
archivo = Path('./pi_digits.txt')
contenido = archivo.read_text().rstrip()
print(contenido)


lista_lineas = contenido.splitlines()
i = 1
for linea in lista_lineas:
    print(f"{i} -> {linea}")
    i += 1

# unir lineas
union_lineas = ''
for linea in lista_lineas:
    union_lineas += linea.lstrip()

print(union_lineas)
