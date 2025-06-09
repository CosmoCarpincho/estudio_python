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


"""
Algoritmo de Huffman:

1. Contar la frecuencia de aparición de cada carácter en el texto.
2. Crear un nodo hoja para cada carácter con su frecuencia.
3. Insertar todos los nodos en un montículo mínimo (min-heap).
4. Mientras haya más de un nodo en el montículo:
    a. Extraer los dos nodos con menor frecuencia.
    b. Crear un nuevo nodo padre con la suma de las frecuencias de estos nodos.
    c. Asignar los nodos extraídos como hijos izquierdo y derecho del nodo padre.
    d. Insertar el nodo padre de nuevo en el montículo.
5. El nodo restante en el montículo es la raíz del árbol de Huffman.
6. Recorrer el árbol para asignar códigos binarios a cada carácter:
    - Asignar '0' al recorrer hacia la izquierda.
    - Asignar '1' al recorrer hacia la derecha.
7. Codificar el texto reemplazando cada carácter por su código binario asignado.
8. Decodificar el texto reconstruyendo los caracteres a partir de los códigos binarios y el árbol.
"""
def construir_arbol_huffman(texto):
    # Cuenta la frecuencia de cada caracter en el texto y devuelve un dic ej: {'a':5, 'b': 10}
    frecuencias = Counter(texto)
    monticulo = MonticuloMinimo() # es un arbol binario con dos restricciones
    # estructura: todos los niveles del árbol deben estar completos, a excepción del último que se completa desde izq
    # orden: el arbol debe estar ordenado por niveles asc o desc. En este caso es de orden mínimo. Padre menor que sus hijos.
    # Pagina del libro 187. LEER!!!

    # Crea un nodo por caracter y lo inserta en el montículo
    for caracter, frecuencia in frecuencias.items():
        monticulo.insertar(Nodo(caracter, frecuencia))

    # Combina los nodos de menor frecuencia hasta construir el árbol completo
    # ESTE ES LA PARTE IMPORTANTE DEL ALGORITMO HUFFMAN
    
    while len(monticulo) > 1:
        nodo1 = monticulo.extraer_minimo()
        nodo2 = monticulo.extraer_minimo()
        nodo_combinado = Nodo(frecuencia=nodo1.frecuencia + nodo2.frecuencia)
        nodo_combinado.izquierda = nodo1
        nodo_combinado.derecha = nodo2
        monticulo.insertar(nodo_combinado)

    return monticulo.extraer_minimo() if len(monticulo) == 1 else None

# Parte 6 del algoritmo de huffman ->
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

def menu():
    while True:
        print("\n--- Menú Huffman ---")
        print("1. Ingresar texto para codificar")
        print("2. Comprimir archivo de texto")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            texto = input("Ingrese el texto a codificar: ")
            codificado, codigos = codificar_huffman(texto)
            decodificado = decodificar_huffman(codificado, codigos)
            print(f"\nTexto codificado:\n{codificado}")
            print(f"\nTexto decodificado:\n{decodificado}")
            print(f"\nCódigos asignados:\n{codigos}")

        elif opcion == "2":
            ruta = input("Ingrese la ruta del archivo de texto: ")
            try:
                with open(ruta, "r", encoding="utf-8") as archivo:
                    texto = archivo.read()
                codificado, codigos = codificar_huffman(texto)
                decodificado = decodificar_huffman(codificado, codigos)
                print(f"\nArchivo codificado (primeros 500 bits):\n{codificado[:500]}")
                print(f"\nTexto decodificado:\n{decodificado[:500]}")
                print(f"\nCódigos asignados:\n{codigos}")
            except FileNotFoundError:
                print("Archivo no encontrado. Intente nuevamente.")
            except Exception as e:
                print(f"Error al leer el archivo: {e}")

        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
