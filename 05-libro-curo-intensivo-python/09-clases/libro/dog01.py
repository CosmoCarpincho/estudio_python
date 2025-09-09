class Dog:
    """Un intento sencilo de modelar un perro."""

    def __init__(self, name, age):
        """Inicializa los atributos de nombre y edad."""
        self.name = name
        self.age = age

    def sit(self):
        """Simula un perro sentándose en respuesta a una orden."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simula hacer la croqueta en respuesta a una orden."""
        print(f"{self.name} rolled over!")
