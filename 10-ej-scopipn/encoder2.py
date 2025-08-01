
# el ejercicio mas o menos es para convertir caracteres repetidos en caracter numero
# es para comprimir
# aaaaccde -> a4c2de
abecedario = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ'


def encode(text: str) -> str:
    abecedario = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    resultado = ''
    contador = 0
    vieja_letra = ''
    # Truco: porque necesito un ciclo mas.
    text += '-'
    for i in range(len(text)):
        l = text[i]
        if len(text)-1 != i and l not in abecedario:
            print("Error no esta en el abecedario")

        if vieja_letra == '':
            contador += 1
        elif vieja_letra == l:
            contador += 1
        elif vieja_letra != l and contador == 1:
            resultado += f"{vieja_letra}"
        else:
            resultado += f"{vieja_letra}{contador}"
            contador = 1
        
        vieja_letra = l

    return resultado
        


def cantEncode(text: str )-> str:
    pass

print(encode("AAAAABBCD"))
print(encode("AABBCCDhDzDAAABBHyHHsssaaaffff"))