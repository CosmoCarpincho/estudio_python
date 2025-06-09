def numeros_pares_impares(numero):
    """Muestra los numeros pares e impares"""
    cont_imp = 0
    for i in range(1, numero+1):
        if(i % 2 == 0):
            print(i, 'Es Par')
        else:
            print(i, 'Es Impar')
            cont_imp += 1
    print('Cantidad de Números Impares:', cont_imp)

# análisis
# if(i% 2 == 0) -> O(1)
# True -> O(1)
# False -> O(3)
# -> max(O(1)+O(3)) = O(3)

numeros_pares_impares(30)
