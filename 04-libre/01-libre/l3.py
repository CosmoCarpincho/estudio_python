li = []

li.append(1)
li.append(2)
li.append(3)
li.append(4)
li.append(5)

a = li.pop()

li.remove(4)
print(li)

li.insert(3,'tres')
print(li)

print(li.index(3))

print('tres' in li)

print(type(1))
tupla1 = (1,2)
tupla2 = (2,3)
print(tupla1 + tupla2)
print(len(tupla1 + tupla2))

a, b, c, _ = tupla1 + tupla2
print(a,b,c)