# 8-6 Nombres de ciudad

def ciudad_pais(ciudad, pais):
    return f"{ciudad}, {pais}"

print(ciudad_pais("Santiago", "Chile"))
print(ciudad_pais(ciudad="Quilmes", pais = "Argentina"))

# 8-7 Álbun
def hacer_albun(nombre_artista, titulo_albun, cant_canciones=None):
    d = {'nombre': nombre_artista, 'titulo_albun': titulo_albun}
    if cant_canciones:
        d['cant_canciones'] = cant_canciones
    return d

a1 = hacer_albun("Charly Garcia", "Yendo de la cama al living")
a2 = hacer_albun("Charly Garcia", "Clics modernos", cant_canciones=9 )
a3 = hacer_albun("Almendra", "Almendra", 9 )

print(a1)
print(a2)
print(a3)

carga_usuario = []
while True:
    albun = {}
    print("q para salir en cualquier momento")
    artista = input("Ingrese nombre de artista: ")
    if artista == "q":
        break
    albun = input("Ingrese nombre del álbun: ")
    if artista == "q":
        break
    cant_canciones = input("Ingrese la cantidad de canciones del álbun (puede ser vacio): ")
    if not artista or not albun:
        print("ERROR: Obligatorio artista o albun")
        continue

    if cant_canciones.isdigit():
        albun = hacer_albun(artista,albun,cant_canciones)
    else:
        albun = hacer_albun(artista,albun)

    carga_usuario.append(albun)

print("sali")
for a in carga_usuario:
    print(a)
