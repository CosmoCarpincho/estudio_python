# 7-8 Bocatería
bocadillos = ["Empanaditas", "Mini tortilla de papa", "Bruschettas con tomate y albahaca", "Pinchos de jamón y melón"]
bocadillos_terminados = []

while bocadillos:
    b = bocadillos.pop()
    bocadillos_terminados.append(b)
    print(f"Su bocadillo esta terminado. {b}")

print(f"bocadillos: {bocadillos}")
print(f"terminados: {bocadillos_terminados}")

# 7-9 Ya no hay pastrami

bocadillos = ["Empanaditas", "Mini tortilla de papa", "Bruschettas con tomate y albahaca", "Pinchos de jamón y melón", "Pastrami", "Pastrami", "Pastrami"]
bocadillos_terminados = []

while True:
    print("bocadillos: 1)Empanaditas, 2)Mini tortilla de papa, 3)Bruchetas con tomaye y albahca, 4)Pinchos de jamón y melón, 5)Pastrami q)quit")
    respuesta = input()

    elemento = ""
    if respuesta == "1":
        elemento = "Empanaditas"
    elif respuesta == "2":
        elemento = "Mini tortilla de papa"
    elif respuesta == "3":
        elemento = "Bruschettas con tomate y albahaca"
    elif respuesta == "4":
        elemento = "Pinchos de jamón y melón"
    elif respuesta == "5":
        elemento = "Pastrami"
    elif respuesta == "q":
        break
    else:
        print("No tenemos ese bocadillo")
        continue
    if elemento in bocadillos:
        bocadillos.remove(elemento)
        bocadillos_terminados.append(elemento)
        print(f"Su bocadillo esta terminado. {elemento}")
    else:
        print(f"No tenemos mas {elemento}")

    
print(f"bocadillos: {bocadillos}")
print(f"terminados: {bocadillos_terminados}")

# 7-10 Vacaiones de ensueño
vacaciones = []
while True:
    respuesta = input("Si pudieras visitar cualquier lugar del mundo, ¿dónde irías? (q quit): ")

    if respuesta == "q":
        break

    vacaciones.append(respuesta)

print("Vacaciones que te gustaria ir:")
for v in vacaciones:
    print(f"- {v}")
