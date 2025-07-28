# cifrar es símbolo a símbolo

cifrado01 = {
    'a': 'b',
    'b': 'c',
    'c': 'd',
}

def cifrar_siguiente_caracter(texto: str) -> str:
    texto_cifrado = ""
    for c in texto:
        texto_cifrado += chr(ord(c) + 1)
    return texto_cifrado

def descifrar_siguiente_caracter(texto: str) -> str:
    texto_descifrado = ""
    for c in texto:
        texto_descifrado += chr(ord(c) - 1)
    return texto_descifrado


texto = "Hola zzz"
cifrado = cifrar_siguiente_caracter(texto)
print(cifrado)

descifrado = descifrar_siguiente_caracter(cifrado)
print(descifrado)



# codificar es palabra a otra