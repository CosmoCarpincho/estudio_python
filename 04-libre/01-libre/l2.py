import os

a = {'0': 0,
     '1': [1,2,['a']]}

b = {'0':0,
     '1': [1,2,['a']]}

print(a == b) # compara los valores => True
print(a is b) # compara los punteros => False

print(1 and 2 and 3 and 4) # Devulve el primer falso o el ultimo valor => 4
print(1 and 2 and 0 and 3) # => 0

print(1 or 2 or 3 or 4) # Devuelve el primer True. (todos los num True salvo el 0 que es False)
print(0 or 0 or 0 or -1 or 1 or 2) # => -1

# Usos del comportamiento del or
## Asignaciones condicionales elegantes
nombre = input("Tu nombre: ") or 'Anónimo' # si no insertas nombre como es Null es false entonces devuelve Anónimo que es True
print(nombre)

# Evaluaciones perezosas (Lazy Evaluation)
archivo = os.path.exists("archivo.txt") and open("archivo.txt") # si no existe el path no ejecuta el open
print(f"archivo -> {archivo}")

# Cadena de Valores "fallback" (valor alternaitivo)
## encadenas muchos or para buscar el primer valor 'útil'
user_config = ''
env_config = ''
default_config = 'tengo config'
config = user_config or env_config or default_config

print(config)

# Expresiones en Retornos Condicionales
def obterner_precio(descuento):
    return descuento and descuento * 0.9 or 100
# Si hay descuento (truthy), aplica 10%
# Si no hay descuento (falsy como None o 0), devuelve 100

# Atajos de Evaluación para Objetos
#user = get_user() or GuestUser() 


# or devuelve el primer true
# and devuelve el primer false o el ultimo si son todos verdaderos


# Guard Clause
# Corta la ejecución de una función temprano si algo no cumple una condición, en vez de anidar muchos if
# con and, podés hacer esto sin if explícito

def abrir_archvo(nombre_archivo):
    # Si el archivo no existe, devuelve None si intentar abrirlo
    return os.path.exists(nombre_archivo) and open(nombre_archivo)

def enviar_mensaje(usuario, mensaje):
    # Si el usuairo es None, no hace nada
    usuario and usuario.enviar(mensaje)

## Ejemplo de optimización "lazy" (no evalúa lo innecesario)
def dividir(a, b):
    return b != 0 and (a / b) or "División por cero"

# 'Operador ternario de'
print("Hola" if 0 > 1 else "Chau") # => Chau
print("Hola" if 0 < 1 else "Chau") # => Hola


nom: str # ahora se puede declarar en python
num = str


print("Hola")

nom = "11hola"
print(nom)

num = "pepe"

print(num)



