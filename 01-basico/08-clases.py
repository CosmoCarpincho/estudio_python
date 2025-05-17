class Person:
    def __init__(self, name, age):
            self.name = name
            self.age = age

    def greet(self):
        return f"Mi nombre es {self.name} y tengo {self.age}"


persona1 = Person("Ana", 32)
persona2 = Person("Cosmo", 88)
persona3 = Person("Pepe", 23)
personas = [persona1, persona2, persona3]

for p in personas:
    print(p.greet())



