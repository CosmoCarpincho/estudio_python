from abc import ABC, abstractmethod
from typing import List

class Vehiculo(ABC):
    def __init__(self, marca:str , anio: str):
        self.marca = marca
        self.anio = anio

    @abstractmethod
    def get_info(self):
        pass
        # raise NotImplementedError("La subclase debe impletentar el método get_info()")

class Motor:
    def __init__(self, info_motor: str):
        self.info_motor = info_motor

    def get_info(self):
        return f"Información del motor: {self.info_motor}"

class Auto(Vehiculo):
    def __init__(self, marca: str, anio: str, motor: Motor=None):
        super().__init__(marca, anio)
        self.motor = motor
    
    def get_info(self):
        info_motor = self.motor.get_info() if self.motor else "Sin motor"
        return f"Marca: {self.marca} Año: {self.anio} Info Motor: {info_motor}"

class Bateria:
    def __init__(self, marca_bateria: str, carga_bateria: str):
        self.marca = marca_bateria
        self.carga_bateria = carga_bateria
    
    def get_info(self):
        return f"Marca Bateria: {self.marca}, Carga Bateria: {self.carga_bateria}"


class AutoElectrico(Auto):
    def __init__(self, marca: str, anio: str, bateria: Bateria):
        super().__init__(marca, anio)
        self.bateria = bateria
    
    def get_info(self):
        return f"{super().get_info()} Info Bateria:{self.bateria.get_info()}"

motor1 = Motor("V8 5.0L - 460 HP, gasolina, inyección directa")
a1 = Auto("Ford Mustang GT", "2022", motor1)

bateria1 = Bateria("Panasonic", "82 kWh - Autonomía estimada: 505 km")
a2 = AutoElectrico("Tesla Model 3 Long Range", "2023", bateria1)

motor2 = Motor("1.0L Turbo - 116 HP, 3 cilindros, nafta")
a3 = Auto("Volkswagen Polo TSI", "2021", motor2)

bateria2 = Bateria("BYD", "44.9 kWh - Autonomía estimada: 300 km")
a4 = AutoElectrico("BYD Dolphin", "2024", bateria2)

vehiculos: List[Vehiculo] = [a1, a2, a3, a4]

for vehiculo in vehiculos:
    print(vehiculo.get_info())