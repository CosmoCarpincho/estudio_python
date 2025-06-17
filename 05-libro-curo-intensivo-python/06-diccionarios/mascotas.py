mascotas = []

mascota = {
    'nombre': 'firulais',
    'tipo': 'perro',
    'duenio': 'Pepe',
}
mascotas.append(mascota)


mascota = {
    'nombre': 'uma',
    'tipo': 'gato',
    'duenio': 'cosmo',
}
mascotas.append(mascota)

mascota = {
    'nombre': 'anton',
    'tipo': 'perro',
    'duenio': 'ana',
}
mascotas.append(mascota)

for mascota in mascotas:
    print(mascota['nombre'])
    print(f" tipo: {mascota['tipo']}")
    print(f" dueño: {mascota['duenio']}\n")

# 6-9 lugares favoritos

lugares_favoritos = {
    'cosmo': ['pc', 'montaña'],
    'ana': ['playa', 'montaña'],
    'pepe': ['cancha', 'playa']
}

for persona, lugares in lugares_favoritos.items():
    print(f"A {persona} le gusta los siguientes lugares:")
    for lugar in lugares:
        print(f" {lugar}")


# 6-10 números favoritos

num_favs = {
    'cosmo': [1, 7, 28],
    'ana': [33, 2, 11],
    'ricardo': [77, 78, 4],
}

for p, nums in num_favs.items():
    print(p + " ->", end="")
    for num in nums:
        print(" " + str(num), end="")
    print()

# 6-11

ciudades = {
    'Buenos Aires': {
        'pais': 'Argentina',
        'poblacion': 'más de 15 millones',
        'atracion principal': 'Obelisco',
        'rio cercano': 'Río de la Plata',
    },
    'Paris': {
        'pais': 'Francia',
        'poblacion': 'más de 11 millones',
        'atracion principal': 'Torre Eiffel',
        'rio cercano': 'Río Sena',
    },
    'Tokio': {
        'pais': 'Japón',
        'poblacion': 'más de 37 millones',
        'atracion principal': 'Templo Sensi-ji',
        'rio cercano': 'Río Sumida',
    },
}

for ciudad , infos in ciudades.items():
    print(f"Ciudad: {ciudad}")
    for info, detalle in infos.items():
        print(f" {info}: {detalle}")
    print()