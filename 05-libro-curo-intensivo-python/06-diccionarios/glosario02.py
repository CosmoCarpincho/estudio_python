glosario = {
    'iterable': 'Cualquier objeto que puede ser recorrido por un for',
    'tupla': 'Estructura inmutable que agrupa varios valores',
    'Lista': 'Colección ordeneda y mutable de varios valores',
}

for palabra, definicion in glosario.items():
    print(f"=> {palabra.title()}\n=  {definicion}\n==")

#6-5 ríos

rios_argentina = {
    "Río Parana": "Segundo río mas largo de Sudamérica.",
    "Río de la Plata": "Estuario formado por la confluencia del Párana y el Uruguay",
    "Río Uruguay": "Forma parte del límite este del pais.",
    "Río Colorado": "Recorre el sur de Mendoza",
}

for rio, desc in rios_argentina.items():
    print(f"{rio} -> {desc}")

print("Solo ríos:")
for rio in rios_argentina.keys():
    print(rio)

print("Solo descripciones:")
for desc in rios_argentina.values():
    print(desc)

# 6-6 sondeos

personas = ["Cosmo", "Ana", "Pepe", "Ricardo", "Agusto"]

encuesta = {
    "Cosmo": "C",
    "Ricardo": "Python",
    "Ana": "Ada",
}


for persona in personas:
    if persona in encuesta.keys():
        print(f"{persona} Ya hiciste la encuesta. Gracias por haberla completado")
    else:
        lenguaje = input(f"{persona}: Ingrese su lenguaje preferido:")
        encuesta[persona] = lenguaje


print(encuesta)