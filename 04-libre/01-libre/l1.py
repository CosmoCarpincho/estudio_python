class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0
    
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None
    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return None

    def tamaño(self):
        return len(self.items)

p = Pila()
p.apilar(10)
p.apilar(20)
p.apilar(30)

print("Cima:", p.cima())
print("Desapilado:", p.desapilar())
print("Cime actual:", p.cima())
print("¿Esta vacia?", p.esta_vacia())

