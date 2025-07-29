
def factorial(n: int) -> int:
    if n == 2:
        return 2
    
    return n * factorial(n-1)


print(factorial(12))