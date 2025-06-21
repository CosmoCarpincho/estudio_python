from pathlib import Path

# 10-1 Aprender Python
file = Path('./en_python.txt')
contenido = file.read_text()

for i in range(2):
    print(i+1)
    print(contenido)

print("repetir lineas:")
for linea in contenido.splitlines():
    print(linea)
    print(linea)

#10-2 Aprender C:
print("Reemplace por C:")
print(contenido.replace('python', 'C'))