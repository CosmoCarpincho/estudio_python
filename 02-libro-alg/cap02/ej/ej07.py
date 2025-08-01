def serie(n: int) -> float:
    if n <= 0:
        print("Error: Tiene que ser mayor a cero")
        return 0
    if n == 1:
        return 1
    return 1/n + serie(n-1)

for i in range(1,20):
    print(f"f({i}) = {serie(i)}")