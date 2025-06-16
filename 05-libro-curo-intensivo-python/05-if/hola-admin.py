nombres = ["Cosmo", "Pepe", "Ana", "Admin", "Julia", "Ricardo"]

nombres = []
if not nombres:
    print("Necesitamos encontrar algún usuario!")
else:
    for nombre in nombres:
        if nombre.lower() == "admin":
            print("Hola Admin, ¿quieres ver un informe de estado?")
        else:
            print(f"Hola, {nombre}, gracias por volver a entrar.")

# 5-10 comprobar nombres de usuario
current_users = ["Cosmo", "Pepe", "Ana", "Admin", "Julia", "Ricardo"]
new_users = ["Cosmo", "PePe", "Juan", "JULIA", "Carlos"]

for new_user in new_users:
    if new_user.lower() in [c.lower() for c in current_users]:
        print(f"El usuario {new_user} no esta disponible")
    else:
        print(f"El usuario {new_user} esta disponible")

# 5-11 Números ordinales en inglés:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for numero in numeros:
    if numero == 1:
        print(f"{numero}st")
    elif numero == 2:
        print(f"{numero}nd")
    elif numero == 3:
        print(f"{numero}rd")
    else:
        print(f"{numero}th")