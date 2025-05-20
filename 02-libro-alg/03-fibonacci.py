import time

def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_iterativo(n):
    n0 = 0
    n1 = 1
    fib = 0
    if n == 0 or n == 1:
        fib = n
    else:
        i = 2
        while i <= n:
            fib = n0 + n1
            n0 = n1
            n1 = fib
            i += 1
    return fib

for i in range(40):
    inicio1 = time.perf_counter()
    print(f"posición: {i} -> fibonacci recursivo = {fibonacci(i)}", end=" -> ")
    fin1 = time.perf_counter()
    print(f"tardo {fin1 - inicio1:.6f} segundos")

    inicio2 = time.perf_counter()
    print(f"posición: {i} -> fibonacci iterativo = {fibonacci(i)}", end=" -> ")
    fin2 = time.perf_counter()
    print(f"tardo {fin2 - inicio2:.6f} segundos")