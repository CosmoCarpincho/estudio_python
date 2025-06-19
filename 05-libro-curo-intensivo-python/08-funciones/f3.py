# 8-9 Mensajes

mensajes = ["Hola", "Cómo andas?", "Cómo anda la hinchada?"]

def mostrar_mensajes(mensajes):
    for m in mensajes:
        print(m)
    

mostrar_mensajes(mensajes)

# 8-10 Enviar mensajes

mensajes_enviados = []
def enviar_mensajes(mensajes):
    while mensajes:
        m = mensajes.pop(0)
        mensajes_enviados.append(m)

enviar_mensajes(mensajes)
print(mensajes)
print(mensajes_enviados)

# 8-11 Mensajes archivados
print("---")
mensajes = mensajes_enviados[:]
mensajes_enviados.clear()

enviar_mensajes(mensajes[:])
print(mensajes)
print(mensajes_enviados)
