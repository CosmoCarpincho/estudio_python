lista = [0,1,2,3,4,5,6]

lista.append(7)
lista.extend((8,9,10))

print(lista)

print(lista[::-1])

cabeza = lista[0]
cuerp = lista[1:]

print(cabeza)
print(cuerp)

# tuplas

print(type((1))) # int
print(type((1,))) # tuple. Para que sea tupla de un elemento poner la coma

t = (1,2,3,4,5,6,7,8,9)

a, *b, c = t

print(a)
print(b)
print(c)

# por lo tanto para sacar cabeza y cuerpo

t1 = (1,2,4,5,6,7)

cabeza, *cuerpo = t1 # ojo *b convirtio en lista
print(f"cabeza: {cabeza}")
print(f"cuerpo: {cuerpo} tipo: {type(cuerpo)}") 

# diccionarios
d = {
    "one": 1,
    "two": 2,
    "three": 3,
}

print("one" in d)

print(d.get("nine")) # None

# si la clave no esta inserta
d.setdefault("nine", 9)

print(d)

d.setdefault("nine", 999) # en teoria no tiene que insertar
print(d)

d.update({"five":5, "six": 6})
print(d)

d["seven"] = 7
print(d)

del d["two"]
print(d)

# del d["algo que no existe"] # da error
print(d)

# INTERESANTE el desempaque de diccionarios toma el de la derecha cuando comparten claves

defaults = {
    "theme": "light",
    "language": "en",
    "autosave": True,
    "volume": 70,
}

user_settings = {
    "language": "es",
    "volume": 40,
}

config = {**defaults, **user_settings}
print(config) # lo de user_settings pisa lo de defaults por estar a la derecha

# Me quede en set