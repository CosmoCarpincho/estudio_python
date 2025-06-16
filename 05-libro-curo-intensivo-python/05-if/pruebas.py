# test

car = "subaru"
print("Is car == 'subaru'? I predict True.")
print(car == "subaru")

print("\nIs car == 'audi'? I predict False.")
print(car == "audi")

marcas_autos = ["Toyota", "Volkswagen", "Honda", "Chevrolet", "Nissan"]

print("\npruba de buscar en lista:")
un_auto = "niSSan"
if un_auto.lower() in [marca.lower() for marca in marcas_autos]:
    print("el auto que tenes esta en la lista de venta")

edad = 15

if edad < 4:
    price = 0
elif edad < 18:
    price = 25
else:
    price = 40

print(f"Tiene que pagar: {price}")