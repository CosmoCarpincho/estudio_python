lista_invitados = ["cosmo carpincho", "pepe argento", "ada lovelace"]

mensaje = "Esta invitado a la cena ..."

m1 = f"{lista_invitados[0]}, {mensaje}"
m2 = f"{lista_invitados[1]}, {mensaje}"
m3 = f"{lista_invitados[2]}, {mensaje}"

print(m1)
print(m2)
print(m3)

print(f"No puede asistir: {lista_invitados[1]}")

elimina = "pepe argento"

lista_invitados.remove(elimina)

print(lista_invitados)

print("Se agrega a maire curie")

lista_invitados.append("marie curie")


m1 = f"{lista_invitados[0]}, {mensaje}"
m2 = f"{lista_invitados[1]}, {mensaje}"
m3 = f"{lista_invitados[2]}, {mensaje}"

print(m1)
print(m2)
print(m3)


print(lista_invitados)

# mas invitados
principio = "Lord Kelvin"
mitad = "Gauss"
final = "Planck"
print(f"Se agrega al principio {principio}")
lista_invitados.insert(0, principio)
print(lista_invitados)
print(f"se agrega a la mitad {mitad}")
lista_invitados.insert(len(lista_invitados)//2, mitad)
print(lista_invitados)
print(f"se agrega al final {final}")
lista_invitados.insert(len(lista_invitados), final)
print(lista_invitados)


mf = "Estan invitados a la cena las siguientes personas:", lista_invitados[0], lista_invitados[1], lista_invitados[2], lista_invitados[3], lista_invitados[4], lista_invitados[4]
print(mf)


# reducir lista a dos invitados

print("Solo se puede invitar a dos invitados")
mensaje = "lo siento no hay suficiente espacio"
print(lista_invitados.pop(),mensaje)
print(lista_invitados)
print(lista_invitados.pop(),mensaje)
print(lista_invitados)
print(lista_invitados.pop(),mensaje)
print(lista_invitados)
print(lista_invitados.pop(),mensaje)
print(lista_invitados)

print(lista_invitados[0], lista_invitados[1], "Siguen invitados")

# borrar lista
del lista_invitados[1]
del lista_invitados[0]

print(lista_invitados)
