lista = ["hola", 10, 2.5]
print(lista)
print(type(lista))
print(f"tamaño: {len(lista)} {lista.__len__()}")

print("Primer elemento: ", lista[0])
print("Último elemento: ", lista[-1])

# slices (cortar la lista)
num_str = "123456789"
#tener en cuenta que arranca en 0.
#el segundo digito toma el anterior. Digamos si pones 3 va a la posición 2.
# [inicio:final-1]
print(num_str[0:3]) #123
print(num_str[1:3]) #23
print(num_str[2:3]) #3
print(num_str[3:3]) # nada
print(num_str[-1:3]) # nada
print(num_str[-1:-3]) # nada
print(num_str[4:]) #56789
print(num_str[:5]) #12345
print(num_str[2:-2]) #34567

#append agrega al final
lista.append("append") # ["hola", 10, 2.5, "append"]
#insert agrega en posición asignada
lista.insert(1,"en segundo lugar") # ['hola', 'en segundo lugar', 10, 2.5, 'append']


#index devuelve primera aparición del elemento
print(lista.index(10)) # 2

#max min en lista de números
lista_num = [4, 2, 6.6, 21, 3.8, 22.5, 3]
print(max(lista_num)) # 22.5
print(min(lista_num)) # 2

# borrar elementos
del lista_num[-3:-2] # borra 3.8
print(lista_num)
del lista_num #borra lista