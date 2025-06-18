#7-1 coche alquiler

message = "¿Qué tipo de auto quiere alquilar?: "
respuesta = input(message)
print(f"Veamos si tenemos un {respuesta} para usted.")


# 7-2 Mesa en un restaurante

cant_comensales = input("¿Cuántos vienen a comer?: ")
if int(cant_comensales) > 8:
    print("Van a tener que esperar mesa.")
else:
    print("Su mesa está lista.")

# 7-3 Múltipos de diez
numero = input("Ingrese un número: ")
if int(numero) % 10 == 0:
    print(f"{numero} es multiplo de 10")
else:
    print(f"{numero} no es multiplo de 10")
