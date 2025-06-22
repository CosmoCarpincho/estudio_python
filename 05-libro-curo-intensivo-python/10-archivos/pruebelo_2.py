# 10-04 Invitado

from pathlib import Path

nombre = input("Ingrese su nombre: ")
archivo_nombre = Path('nombres.txt')
archivo_nombre.write_text(f"{nombre}\n")


# 10-5 libro de inviados:
nom = ""
nombres = ""
while True:
    nom = input("Ingrese un nombre (q para salir): ")
    if nom == "q":
        print("Finalizo el programa")
        break
    nombres += f"{nom}\n"

file_libro_invitados = Path('libro_invitados.txt')
file_libro_invitados.write_text(nombres)

