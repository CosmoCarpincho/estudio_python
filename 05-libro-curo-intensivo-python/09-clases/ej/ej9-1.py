class Restaurante:
    """Un restaurante"""
    
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre = nombre_restaurante
        self.tipo_cocina = tipo_cocina
    
    def describir_restaurante(self):
        print(f"El restaurante {self.nombre} tiene la cocina tipo {self.tipo_cocina}")
    
    def abrir_restaurante(self):
        print(f"El restaurante {self.nombre} esta abierto")


r = Restaurante("Los manolos", "buffet")
r.describir_restaurante()
r.abrir_restaurante()

r2 = Restaurante("Argenchina", "Comida China")
r3 = Restaurante("El señor de los novillos", "Asado")

r2.describir_restaurante()
r3.describir_restaurante()

class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def describir_usuario(self):
        return f"El usuario de nombre: {self.nombre} y apellido {self.apellido}"

    def saludar_usuario(self):
        print(f"Buenas {self.nombre}")
    

cosmo = Usuario("Cosmo", "Carpincho")
pepe = Usuario("Pepe", "Argento")

print(cosmo.describir_usuario())
cosmo.saludar_usuario()

print(pepe.describir_usuario())
pepe.saludar_usuario()
