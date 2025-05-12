s = "  Hola Mundo  "
lista = ["Hola", "Mundo"]

print(s.lower())            # "  hola mundo  "
print(s.upper())            # "  HOLA MUNDO  "
print(s.capitalize())       # "  hola mundo  "
print(s.title())            # "  Hola Mundo  "
print(s.strip())            # "Hola Mundo"
print(s.lstrip())           # "Hola Mundo  "
print(s.rstrip())           # "  Hola Mundo"

print(s.replace("Mundo", "Python"))  # "  Hola Python  "
print(s.split())           # ['Hola', 'Mundo']
print("-".join(lista))     # "Hola-Mundo"

print(s.find("Mundo"))     # 7 (empieza en ese índice)
print(s.startswith("  Ho"))  # True
print(s.endswith("ndo  "))   # True

num_str = "12345"
letras_str = "Hola"
alnum_str = "Hola123"
espacio_str = "   "

print(num_str.isdigit())   # True
print(letras_str.isalpha()) # True
print(alnum_str.isalnum()) # True
print(espacio_str.isspace()) # True

print(s.count("o"))        # 2
print(s.index("Mundo"))    # 7

print("42".zfill(5))       # "00042"
