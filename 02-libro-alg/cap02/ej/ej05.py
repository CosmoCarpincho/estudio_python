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

    se_pueden_repetir_3 = ('I', 'X', 'C', 'M')

    cabeza = num_rom[0]
    cola = num_rom[1:]
    if len(num_rom) == 1:
        return tabla_conversion[cabeza]
    siguiente = num_rom[1]

    if cabeza not in se_pueden_repetir_3 and siguiente not in se_pueden_repetir_3 and cabeza == siguiente:
        print(f"ERROR: no se puede tener mas de 3 veces {cabeza}")
        return -999
    
    if cabeza == siguiente:
        return tabla_conversion[cabeza] + convertir_romano(cola)
    if cabeza != siguiente and tabla_conversion[cabeza] < tabla_conversion[siguiente]:
        return tabla_conversion[cabeza] * -1 + convertir_romano(cola)
    if cabeza != siguiente and tabla_conversion[cabeza] > tabla_conversion[siguiente]:
        return tabla_conversion[cabeza] + convertir_romano(cola)


print(convertir_romano('I'))
print(convertir_romano('II'))
print(convertir_romano('III'))
print(convertir_romano('IV'))
print(convertir_romano('V'))
print(convertir_romano('VI'))
print(convertir_romano('VII'))
print(convertir_romano('VIII'))
print(convertir_romano('IX'))
print(convertir_romano('X'))
print(convertir_romano('XI'))
print(convertir_romano('XV'))
print(convertir_romano('XX'))
print(convertir_romano('MMX'))
print(convertir_romano('MMV'))
print(convertir_romano('MMXXV'))
print(convertir_romano('XVV'))
