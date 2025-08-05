# convertir decimal a binario

def dec_bin(n: int):
    if n == 0:
        return '0'

    div = n // 2
    resto = n % 2

    if div != 1:
        return dec_bin(div) + str(resto)
    if div == 1:
        return str(div) + str(resto)

for i in range(0,64):
    print(f"{i} -> {dec_bin(i)}")


# mejor forma
def dec_bin2(num: int):
    if num == 0 or num == 1:
        return str(num)

    return dec_bin2(num // 2) + str(num % 2)


    
