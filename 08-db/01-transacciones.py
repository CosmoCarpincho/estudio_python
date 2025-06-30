# ¿Cómo armar un grafo de precedencia?
# Hasta 9 planificaciones

from collections import defaultdict

# R1(A)R3(C)
p1 = 'r1a,r3c,r2b,w1a,r4d,w3c,w2b,w4d'



def crear_grafo_precedencia(text):
    ap1 = str.split(text,',')
    # print(ap1)

    planificacion = []
    for op in ap1:
        planificacion.append((op[0], op[1], op[2], op))

    # print(planificacion)

    # un grafo es (nodo, salida, entrada) (nodosalida, nodoentrada)

    grafo = []
    for i in range(len(planificacion)):
        # print(i, planificacion[i])
        if planificacion[i][0] == 'w':
            variable = planificacion[i][2]
            for j in range(len(planificacion)):
                if ((planificacion[j][0] == 'w' or planificacion[j][0] == 'r') and
                    planificacion[j][2] == variable and planificacion[j][1] != planificacion[i][1]):
                    if i < j:
                        grafo.append((planificacion[i], planificacion[j]))
                    elif i > j:
                        grafo.append((planificacion[j], planificacion[i]))
                    else:
                        pass
    return grafo

p2='r2a,w2b,r4b,w4b,r3c,w3b,r1a,r1b,r1d,w1a,w1d'
g2 = crear_grafo_precedencia(p2)
# print(g2)


g2n = [(e[0][3], e[1][3]) for e in g2]
for g in g2n:
    print(g)


def construir_diccionario_adyacencia(lista_aristas):
    grafo = defaultdict(list)
    for origen, destino in lista_aristas:
        grafo[origen].append(destino)
    return grafo

def tiene_ciclo(grafo):
    visitado = set()
    en_recursion = set()

    def dfs(nodo):
        visitado.add(nodo)
        en_recursion.add(nodo)

        for vecino in grafo.get(nodo, []):
            if vecino not in visitado:
                if dfs(vecino):
                    return True
            elif vecino in en_recursion:
                return True
        
        en_recursion.remove(nodo)
        return False
    
    for nodo in grafo:
        if nodo not in visitado:
            if dfs(nodo):
                return True
    
    return False


grafo_dict = construir_diccionario_adyacencia(g2n)

if tiene_ciclo(grafo_dict):
    print("Hay ciclo. No es conflictivamente serializable.")
else:
    print("No hay ciclos. Es serializable en cuanto a conflictos")
