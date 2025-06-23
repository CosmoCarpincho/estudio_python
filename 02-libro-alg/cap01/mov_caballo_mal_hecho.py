# movimiento de un caballo en teclado de telefono (pág 14)
# ERROR: Me confundi aca conte la cantidad total de pasos no de movimientos finales. OJOOOO!!
# ej si tengo 2 movimientos mertidos y arranco en "1" tendria que dar 5, pero en este algoritmo da 8 porque cuenta 
# todos los pasos. OJO esta mal!!
def mov_caballo(cant_mov_permitidos, ubicacion):
    mapeo = {
        "0": ("4","6"),
        "1": ("6","8"),
        "2": ("7","9"),
        "3": ("4","8"),
        "4": ("3","9","0"),
        "6": ("1","7","0"),
        "7": ("2","6"),
        "8": ("1","3"),
        "9": ("2","4"),
    }
    cant_movimientos_total = 0
    if ubicacion in ["1", "2", "3", "7", "8", "9", "0"]:
        cant_movimientos_total += 2
        if cant_mov_permitidos > 1:
            cant_movimientos_total += mov_caballo(cant_mov_permitidos-1,mapeo[ubicacion][0])
            cant_movimientos_total += mov_caballo(cant_mov_permitidos-1,mapeo[ubicacion][1])
    elif ubicacion in ["4", "6"]:
        cant_movimientos_total += 3
        if cant_mov_permitidos > 1:
            cant_movimientos_total += mov_caballo(cant_mov_permitidos-1,mapeo[ubicacion][0])
            cant_movimientos_total += mov_caballo(cant_mov_permitidos-1,mapeo[ubicacion][1])
            cant_movimientos_total += mov_caballo(cant_mov_permitidos-1,mapeo[ubicacion][2])
    elif ubicacion == "5":
        pass
    else:
        print("No existe esa posición en un teclado de teléfono")
    
    return cant_movimientos_total
        

def mov_caballo_todas_casillas(cant_mov_permitidos):
    cant = 0
    for i in range(10):
        cant += mov_caballo(cant_mov_permitidos,str(i))
    return cant

# print(f"1 {mov_caballo_todas_casillas(1)}")
print(f"2 {mov_caballo_todas_casillas(2)}")
print(f"3 {mov_caballo_todas_casillas(3)}")
print(f"4 {mov_caballo_todas_casillas(4)}")
print(f"5 {mov_caballo_todas_casillas(5)}")
print(f"6 {mov_caballo_todas_casillas(6)}")
print(f"7 {mov_caballo_todas_casillas(7)}")