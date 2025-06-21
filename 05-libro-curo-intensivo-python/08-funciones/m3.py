# 8-15 
from m1 import build_profile, make_car as mc

user_profiles = {}


user_profiles.update(build_profile("Cosmo", "Carpincho", edad=65, ciudad="Bariloche"))
user_profiles.update(build_profile("Pepe", "Argento", edad=35, ciudad="Quilmes", profesion="Zapatero"))

print(user_profiles)

car = mc('subaru', 'outback', color='blue', tow_package=True)
print(car)