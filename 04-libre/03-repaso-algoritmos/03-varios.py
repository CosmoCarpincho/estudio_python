## ¿Cómo llenar un diccionario con a -> z , b -> y ...?
# Forma estilo C
abc = "abcdefghijklmnopqrstuvwxyz"

dic = {}
for i in range(len(abc)):
    dic[ord(abc[i])] = ord(abc[len(abc) - 1 - i])

print(dic)

for k,v in dic.items():
    print(chr(k) + " -> " + chr(v))


# con zip

abc = "abcdefghijklmnopqrstuvwxyz"
inv_abc = abc[::-1]

dic2 = dict(zip(abc, inv_abc))
print(dic2)

## built-in https://docs.python.org/3.3/library/functions.html

# valor absoluto
a = 12
b = -12
print(abs(a), abs(b))

# all. devuelve True si los elementos del iterable son verdaderos o si esta vacio (Para todo)

a = []
print(all(a)) #Vacio -> True

a = [1,2,3]
print(all(a)) # -> True

a = [1,2,True] # -> True
print(all(a))

a = [1,2,'']
print(all(a)) # -> False xq str vacio es falso


def all2(iterable):
    for element in iterable:
        if not element:
            return False
    return True

# any, devuelve Verdadero si algun elemento del iterable es verdadero. (Existe \E)

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False


# ascii() escapa los caracteres que no son ascii y permite imprimir el objeto
print(ascii('ñandu')) # \xf1andu  observar que lo escapa a  Latin-1 (ISO 8859-1) o Windows-1252.
a = {
    'ñandu': 'Español'
}

print(ascii(a)) # {'\xf1andu': 'Espa\xf1ol'} 
b = ascii('ñ')
print(b)

# bin numero entero -> cadena binaria

print(bin(7)) #0b111

print(bin(7)[2:]) # 111  quitar el 0b