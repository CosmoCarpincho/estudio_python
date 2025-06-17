def digital_root(n):
    digitos = []
    resultado = 0
    
    while n > 0:
        digitos.insert(0, n % 10)
        n //= 10
    
    for d in digitos:
        resultado += d
        if resultado > 9:
            resultado = digital_root(resultado)
        
    return resultado

numero = 942        

print(digital_root(numero))
