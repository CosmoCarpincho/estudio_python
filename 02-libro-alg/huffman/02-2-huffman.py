from collections import Counter

class Nodo:
    def __init__(self, caracter=None, frecuencia=0):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

class MonticuloMinimo:
    def __init__(self):
        self.datos = []

    def insertar(self, elemento):
        self.datos.append(elemento)
        self._subir(len(self.datos) - 1)

    def extraer_minimo(self):
        if len(self.datos) == 1:
            return self.datos.pop()
        raiz = self.datos[0]
        self.datos[0] = self.datos.pop()
        self._bajar(0)
        return raiz

    def __len__(self):
        return len(self.datos)

    def _subir(self, indice):
        padre = (indice - 1) // 2
        if indice > 0 and self.datos[indice] < self.datos[padre]:
            self.datos[indice], self.datos[padre] = self.datos[padre], self.datos[indice]
            self._subir(padre)

    def _bajar(self, indice):
        menor = indice
        izquierda = 2 * indice + 1
        derecha = 2 * indice + 2
        if izquierda < len(self.datos) and self.datos[izquierda] < self.datos[menor]:
            menor = izquierda
        if derecha < len(self.datos) and self.datos[derecha] < self.datos[menor]:
            menor = derecha
        if menor != indice:
            self.datos[indice], self.datos[menor] = self.datos[menor], self.datos[indice]
            self._bajar(menor)

def construir_arbol_huffman(texto):
    # Cuenta la frecuencia de cada caracter en el texto
    frecuencias = Counter(texto)
    monticulo = MonticuloMinimo()

    # Crea un nodo por caracter y lo inserta en el montículo
    for caracter, frecuencia in frecuencias.items():
        monticulo.insertar(Nodo(caracter, frecuencia))

    # Combina los nodos de menor frecuencia hasta construir el árbol completo
    while len(monticulo) > 1:
        nodo1 = monticulo.extraer_minimo()
        nodo2 = monticulo.extraer_minimo()
        nodo_combinado = Nodo(frecuencia=nodo1.frecuencia + nodo2.frecuencia)
        nodo_combinado.izquierda = nodo1
        nodo_combinado.derecha = nodo2
        monticulo.insertar(nodo_combinado)

    return monticulo.extraer_minimo() if len(monticulo) == 1 else None

def construir_codigos(raiz):
    # Recorre el árbol en profundidad para asignar códigos binarios a cada caracter
    codigos = {}
    def _construir_codigos(nodo, codigo_actual):
        if nodo is None:
            return
        if nodo.caracter is not None:
            codigos[nodo.caracter] = codigo_actual
        _construir_codigos(nodo.izquierda, codigo_actual + "0")
        _construir_codigos(nodo.derecha, codigo_actual + "1")

    _construir_codigos(raiz, "")
    return codigos

def codificar_huffman(texto):
    # Construye el árbol de Huffman y genera el texto codificado
    raiz = construir_arbol_huffman(texto)
    codigos = construir_codigos(raiz)
    texto_codificado = ''.join(codigos[caracter] for caracter in texto)
    return texto_codificado, codigos

def decodificar_huffman(texto_codificado, codigos):
    # Decodifica el texto binario usando los códigos generados
    codigos_invertidos = {v: k for k, v in codigos.items()}
    codigo_actual = ""
    texto_decodificado = ""
    for bit in texto_codificado:
        codigo_actual += bit
        if codigo_actual in codigos_invertidos:
            texto_decodificado += codigos_invertidos[codigo_actual]
            codigo_actual = ""
    return texto_decodificado

# Ejemplo de uso
if __name__ == "__main__":
    texto = "huffman encoding algorithm"
    texto_codificado, codigos = codificar_huffman(texto)
    texto_decodificado = decodificar_huffman(texto_codificado, codigos)

    print("Texto original:", texto)
    print("Codificado:", texto_codificado)
    print("Decodificado:", texto_decodificado)
    print("Códigos:", codigos)
