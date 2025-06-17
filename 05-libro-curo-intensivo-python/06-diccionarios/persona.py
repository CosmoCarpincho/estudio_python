#6-1
persona = {"Nombre" : "Cosmo",
        "Apellido" : "Carpincho",
        "Edad" : 30,
        "Ciudad" : "Termas",
        "Profesión" : "Programador",
        }

print(persona)
print(f"Nombre {persona["Nombre"]}")
print(f"Auto: {persona.get("Auto", "No tiene auto")}")

# 6-2 números favoritos
numeros_favoritos = {
    "Pedro": 1,
    "Richard": 77,
    "Ana":  12,
}


print(f"La persona 'Pedro', tiene como número favorito: {numeros_favoritos['Pedro']}")

for k, v in numeros_favoritos.items():
    print(f"La persona {k}, tiene como número favorito: {v}")

# 6-3 glosario:

glosario = {
    "if": "estructura de control de flujo que ejecuta el codigo a continuación si la expresión condicional dio true",
    "print()": "función que imprime ne consola"
}

for g,v in glosario.items():
    print(f"clave:{g} -> valor: {v}")