def fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci2(n: int) -> int:
    return n if n == 0 or n == 1 else fibonacci2(n -1) + fibonacci(n -2)


for i in range(12):
    print(fibonacci(i))


for i in range(15):
    print(fibonacci2(i))