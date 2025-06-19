# 8-1
def mostrar_mensaje():
    print("aprendiendo funciones")

mostrar_mensaje()

# 8-2
def libro_fav(libro):
    print(f"Libros favoritos: {libro}")

# 8-3
def hacer_camiseta(talla, texto):
    print(f"talla: {talla}, texto: {texto} ")

hacer_camiseta("L", "Python")
hacer_camiseta(texto="C", talla="M")

# 8-4
def hacer_camiseta_2(talle="Grande", texto="C Sharp"):
    print(f"talle: {talle}, texto: {texto}")

hacer_camiseta_2()
hacer_camiseta_2("M")
hacer_camiseta_2("L", "C++")

# 8-5
def describir_ciudad(ciudad, pais="Argentina"):
    print(f"{ciudad} esta en {pais}")

describir_ciudad("Quilmes")
describir_ciudad(pais="Perú", ciudad="Chiclayo")