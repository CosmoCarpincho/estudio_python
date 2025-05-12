print("Hola mundo")

# unpack a colletion

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x, y)
print(z)


varibleGlobal = "variable global"

def una_funcion():
    global otra_var_global
    otra_var_global = "var global dentro de una funcion"
    print("Hola bro", varibleGlobal)


una_funcion()

print(type(otra_var_global))

# casting
x = str(3)
y = int(3)
z = float(3)

print(x, y, z)


x = "Cosmo"

def myFunc():
    print("Hola ", x)

myFunc()

print("hola concatenado" + x)

print(f"Como C {x}\n\n\n")

# tipos de datos
x = "str"
x = 20 #int
x = 20.5 #float
x = 1j #complex
x = ["hola", "que", "tal"] #list
x = ("hola", "que", "tal") #tuple
x = range(6) #range
x = {"hola", "que", "tal"} #set
x = frozenset({"hola", "que"}) # frozenset
x = True
x = False
x = b"Hello" #bytes
print(x)
x = bytearray(5) #bytearray
x = memoryview(bytes(5))
x = None

