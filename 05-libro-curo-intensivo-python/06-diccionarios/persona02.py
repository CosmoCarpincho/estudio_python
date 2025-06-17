persona = {
    'Nombre': 'Cosmo',
    'Apellido': 'Carpincho',
    'Edad': '45',
    'Ciudad': 'Bariloche',
    'Profesion': 'Programador',
}

personas = []
personas.append(persona)

persona = {
    'Nombre': 'Ana',
    'Apellido': 'Lovelace',
    'Edad': '23',
    'Ciudad': 'CABA',
    'Profesion': 'Analista',
}
personas.append(persona)

persona = {
    'Nombre': 'Pepe',
    'Apellido': 'Argento',
    'Edad': '50',
    'Ciudad': 'Ensenada',
    'Profesion': 'Zapatero',
}
personas.append(persona)

for persona in personas:
    print(persona['Nombre'])
    print(f"\t{persona['Apellido']}")
    print(f"\t{persona['Edad']}")
    print(f"\t{persona['Ciudad']}")
    print(f"\t{persona['Profesion']}")