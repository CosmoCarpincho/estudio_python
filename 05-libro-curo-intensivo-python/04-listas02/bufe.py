# tuplas

t = (1,2,3,4)

# error ->
# t[2] = 33 # typeError: 'tuple' object does not support item assignament

# las tuplas son inmutables por lo tanto no se les puede asignar valor
# para modificarla reasignar variable

t = (1,2,33,4)

bufe = ("Ensalada Caprese", "Pollo al curry con arroz basmati", "Albóndigas en salsa barbacoa", "Tabla de quesos y fiambres","Empanaditas de verdura y carne")

for comida in bufe:
    print(comida)

mantener = bufe[:3]
print(mantener)

bufe = mantener + ("Brochettes de camarones y vegetales", "Mini quiches de espinaca y queso")
print(bufe)