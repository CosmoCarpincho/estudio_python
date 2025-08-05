# calcular logaritmo entero de número n en base b.
# log_b(n/b) = log_b n + lob_b b

# es el el exponente max c <= n.  log_b n = c

def log_entero(num, base):
    if num < base:
        return 0
    return 1 + log_entero(num // base, base)
    

    
