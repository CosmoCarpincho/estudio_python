def potencia_rec(base: int, exponente: int):
    if exponente < 0:
        return 1/(base * potencia_rec(base, (exponente*-1) -1))
    if exponente == 0:
        return 1
    if exponente == 1:
        return base
    return base * potencia_rec(base, exponente - 1)

# for i in range(10):
#     print(potencia_rec(2,i))

for i in range(-5,6):
    print(f"2^{i} -> {potencia_rec(2,i)}")
