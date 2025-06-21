# 8-15 Imprimir modelos:

# user_profiles = {}

def build_profile(nombre, apellido, **user_profiles):
    user_profiles['nombre'] = nombre
    user_profiles['apellido'] = apellido
    return user_profiles

#user_profiles.update(build_profile("Cosmo", "Carpincho", edad=65, ciudad="Bariloche"))
#user_profiles.update(build_profile("Pepe", "Argento", edad=35, ciudad="Quilmes", profesion="Zapatero"))

#print(user_profiles)

# 8-14
def make_car(name, brand, **car):
    car['name'] = name
    car['brand'] = brand
    return car

#car = make_car('subaru', 'outback', color='blue', tow_package=True)