p1 = 'r2a,w2b,r4b,w4b,r3c,w3b,r1a,r1b,r1d,w1a,w1d'

valores_iniciales = {
    'A': 100,
    'B': 50,
    'C': 225,
    'D': 30
}

def crear_bitacora_inmediata(planificacion: str, valores_iniciales: dict) -> list:

    valores = valores_iniciales.copy() # copia superficial
    
    plan = str.split(planificacion, ',')
    bitacora = []
    # ("T1", "Comienza")
    # ("T1", A, valor_viejo, valor_nuevo)
    # ("T1", Finaliza)
    # ("Falla del sistema")
    # ("Checkpoint")
    tupla = ('T1','W',)
    estados = {
        'Comienza': 'Comienza',
        'Finaliza': 'Finaliza',
        'Checkpoint': 'Checkpoint',
        'Fallo': 'Fallo del sistema'
    }

    nodos = set()
    for i in range(len(plan)):
        # cuando comienza
        if not plan[i][1] in nodos:
            nodos.add(plan[i][1])
            bitacora.append((f"T{plan[i][1]}", estados['Comienza']))
        # los writes

            bitacora.append((f"T{plan[i][1]}", f"{plan[i][2].upper()}", valores[], valores.A))
        #finaliza
    print("HOla")

    
crear_bitacora_inmediata(p1, valores_iniciales)

