def mult_recursiva(n1: int, n2: int) -> int:
    if n1 == 1:
        return n2
    return n2 + mult_recursiva(n1 - 1, n2)

for i in range(10):
    print(mult_recursiva(2,i))
    
for i in range(10):
    print(mult_recursiva(3,i))

for i in range(10):
    print(mult_recursiva(4,i))
