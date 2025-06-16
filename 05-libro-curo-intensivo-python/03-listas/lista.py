nombres = ["cosmo", "pepe", "ana", "julia"]

print(f"Hola {nombres[0].upper()}")

print("hola" + nombres[0])
for nombre in nombres:
    print(f"Hooola {nombre.capitalize()}")


l = []

l.append("uno")
l.append("dos")
l.append("tres")

print(l)

a = l.pop() 
print(f"a {a}")
print(l)
