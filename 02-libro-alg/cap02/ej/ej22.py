# 22. El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u otro, el que más le guste) 
# está atrapado, pero muy cerca está su mochila que contiene muchos objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con ayuda de la fuerza” realizar las siguientes actividades:

# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no queden más objetos en la mochila; 
# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;
# c. Utilizar un vector para representar la mochila.

objetos = ["obj2", "cantimplora", "sable luz"]

def buscar_sable_luz(objetos):
    cant = 0
    cabeza = objetos[0]
    cola =  objetos[1:]

    if cabeza == 'sable luz' and len(objetos) > 1:
        return print(f"El primer objeto es el sable de Luz")

    if cabeza == 'sable luz':
        return 1
    
    if len(objetos) > 1:
        if buscar_sable_luz(cola) > 0:
            cant += buscar_sable_luz(cola)
        elif buscar_sable_luz(cola) < 1:
            cant = -1
    elif len(objetos) == 1:
        return -1
     
    if cant < 0:
        print(f"no hay sable de luz.")
    else:
        print(f"Hay sable de luz despues de {cant} de objetos")


buscar_sable_luz(objetos)
    


    
