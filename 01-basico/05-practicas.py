
a = "hola mundo hola mundo"

print(a.upper())
print(a.lower())
print(a.index('mundo'))
print(a.count('o'))
print(a.find("mundo"))
print(a.split("h"))

print("===")
print(a.capitalize())
print(a.title())

b = "   hola  mundo aaa    aaa     "
print(b.strip())
print(b.rstrip())

persona = "Pedro Wallace 32 Programador"

llaves = ["\"Nombre: \"", "\"Apellido: \"", "\"Edad: \"", "\"Prof: \"" ]

print(persona.join(llaves)) # NOP

separador = ";;;"

persona = ["Pedro", "Wallace", "32", "Programador"]
print(";".join(persona))
print(separador.join(persona))

print(a.startswith("hola"))
print(a.endswith("mundo"))
print(a.isdigit())
print(a.isalnum())
print(a.isascii())
print(a.isalpha()) #si todos son letras

numero = 78
print(f"el numero es: {str(numero).zfill(6)}") #000078


print("Hola", "que", "tal")
print("Hola" + "que" + "tal")
print("Hola", "que", "tal", sep=";")
print("Hola", "que", "tal", sep=";", end="FINAL\n")

c = "hola"
d = "cosmo"
print("Frase: {}, Nombre: {}".format(c,d))

print(f"numero formateado: {numero:.2f}")