from collections import defaultdict

p1 = 'r2a,w2b,r4b,w4b,r3c,w3b,r1a,r1b,r1d,w1a,w1d'

def crear_grafo_precendencia(text):
    plan = str.split(text, ',')

    grafo = defaultdict(set)
    for op in plan:
        grafo[op[1]]

    for i in range(len(plan)):
        if plan[i][0] == 'w':
            variable = plan[i][2]
            for j in range(len(plan)):
                if ((plan[j][0] == 'w' or plan[j][0] == 'r') and plan[j][2] == variable and plan[j][1] != plan[i][1]):
                    if i < j:
                        grafo[plan[i][1]].add(plan[j][1])
                    elif i > j:
                        grafo[plan[j][1]].add(plan[i][1])
                    else:
                        pass
    return grafo
        

a = crear_grafo_precendencia(p1)
print(a)