def convertir_romano(num_rom: str) -> int:
    tabla_conversion = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    cabeza = num_rom[0]
    cola = num_rom[1:]

    if tabla_conversion[cabeza] < tabla_conversion[cola[0]]:
        return tabla_conversion[cabeza] + convertir_romano(num_rom)
    else