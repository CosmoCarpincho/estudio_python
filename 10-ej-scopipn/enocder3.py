
abecedario = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

def encode(text: str) -> str:
    if len(text) == 0:
        return ''

    abecedario = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    resultado = ''
    contador = 1
    vieja_letra = text[0]

    for i in range(1,len(text) + 1):
        if i != len(text):
            l = text[i]
        if l not in abecedario:
            print("Error no esta en el abecedario")
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