class MonticuloMinimo:
    def __init__(self):
        self.datos = []

    def _subir(self, indice):
        padre = (indice - 1) // 2
        if indice > 0 and self.datos[indice] < self.datos[padre]:
            self.datos[indice], self.datos[padre] = self.datos[padre], self.datos[indice]
            self._subir(padre)
    
    def _bajar(self, indice):
        menor = indice
        izquierda = indice * 2 + 1
        derecha = indice * 2 + 2

        if izquierda < len(self.datos) and self.datos[izquierda] < self.datos[menor]:
            pass
