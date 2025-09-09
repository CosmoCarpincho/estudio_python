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
