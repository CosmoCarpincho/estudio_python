# la idea es mapear cada letra con la opuesta en el abecedario. a -> z ..etc
# pero si se manda un segundo argumento "abcdefgh" el mapeo se hace a -> h ...etc y las que no estan se ignorano
# https://www.codewars.com/kata/571af500196bb01cc70014fa/

import string 
def mirror(code: str, codificacion: str=None):
    if codificacion == "":
        return code.lower()
    
    if codificacion:
        dic = str.maketrans(codificacion, codificacion[::-1])
        if not ' ' in codificacion:
            dic[ord(' ')] = ' '
        return code.lower().translate(dic)

    abecedario = string.ascii_lowercase
    mapeo = str.maketrans(abecedario, abecedario[::-1])
    mapeo[ord(' ')] = ' '
    return code.lower().translate(mapeo)


print(mirror("u9/Xze ruX*JeAfkTe7h", ''))
print("fin")