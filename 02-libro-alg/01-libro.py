#cuantos movimiento ajedrez caballo en teclado celular

# 1 2 3
# 4 5 6
# 7 8 9
#   0  

mapeo_movimientos =  {0:[6,4],
                1:[8,6],2:[7,9],3:[4,8],
                4:[3,9,0],5:[],6:[1,7,0],
                7:[6,2],8:[1,3],9:[4,2]}


def cantidad_movimientos(movimientos, mov_permitidos, mapeo_movimientos):
    if mov_permitidos == 0:
        return len(movimientos)

    cant_mov = 0
    for origen in movimientos:
        siguiente = mapeo_movimientos[origen]
        # print(f"aux: {siguiente}")
        cant_mov += cantidad_movimientos(siguiente, mov_permitidos -1 , mapeo_movimientos)
    return cant_mov


print(cantidad_movimientos(range(10), 1, mapeo_movimientos))
print(cantidad_movimientos(range(10), 2, mapeo_movimientos))
print(cantidad_movimientos(range(10), 3, mapeo_movimientos))
print(cantidad_movimientos(range(10), 4, mapeo_movimientos))


