# importa todo las funciones
# se usa m1.funcion()
import m1

user_profile = {}
user_profile.update(m1.build_profile("Cosmo", "Carpincho", edad=65, ciudad="Bariloche"))
user_profile.update(m1.build_profile("Pepe", "Argento", edad=35, ciudad="Quilmes"))

print(user_profile)
