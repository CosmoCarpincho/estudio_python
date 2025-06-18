import time

# 7-4 Ingredientes de pizza
ingredientes = []
ingrediente = ""
while ingrediente != "quit":
    ingrediente = input("Ingrese ingrediente de pizza (quit para salr): ") 
    if ingrediente != "quit":
        print(f"{ingrediente} agregado a su pizza")
        ingredientes.append(ingrediente)
        
print(ingredientes)

# 7-5 entradas de cine
inicio = time.time()
fin = inicio + 10

print("El precio depende de la edad.")
precio_total = 0
mostrar_precio = True
while True:
    if time.time() > fin:
        print("Te tardasme mucho intentar devuelta.")
        mostrar_precio = False
        break

    respuesta = input("Edad?: ")
    if respuesta == "quit":
        break
    elif int(respuesta) < 3:
        print("Menores de 3 es gratis")
    elif int(respuesta) < 13:
        print("De 3 a 8 años sale 8 euros")
        precio_total += 8
    elif int(respuesta) >= 13:
        print("Mayores de 12 son 12 euros.")
        precio_total += 12
    print(f"Debes pagar por el momento: {precio_total}")

if mostrar_precio:
    print(f"Precio final de las entradas: {precio_total}")
else:
    print("Vuelva a cargar el programa")


