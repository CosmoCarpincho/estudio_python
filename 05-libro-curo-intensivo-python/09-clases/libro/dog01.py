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

my_dog = Dog('Willie', 6)

print(f'My dog name is {my_dog.name}')
print(f'My dog name is {my_dog.age}')

my_dog.sit()
my_dog.roll_over()


your_dog = Dog('Lucy', 3)
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()

