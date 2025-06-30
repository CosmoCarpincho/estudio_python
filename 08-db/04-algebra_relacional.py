from collections import namedtuple

class Esquema:
    def __init__(self, nombre: str, atributos: tuple[str, ...]):
        self.nombre = nombre
        self.atributos = list(atributos)
        self.atributo_cantidad = len(atributos)
        nombre_clase = nombre.replace('-', '_') + "Fila"
        self.Fila = namedtuple(nombre_clase, atributos)

    def add(self, *tuplas: tuple) -> tuple['Esquema', set]:
        filas = set()
        for i, t in enumerate(tuplas):
            if len(t) != self.atributo_cantidad:
                raise ValueError(f"Tupla #{i+1} tiene {len(t)} elementos, pero el esquema '{self.nombre}' espera {self.atributo_cantidad}")
            filas.add(self.Fila(*t))
        return (self, filas)

    def __repr__(self):
        return f"Esquema('{self.nombre}', atributos={self.atributos})"


class Relacion:
    def __init__(self, nombre: str, datos: tuple[Esquema, set]):
        self.nombre = nombre
        self.esquema = datos[0]
        self.tuplas = datos[1]

    def __repr__(self):
        encabezado = f"{self.esquema.nombre}({', '.join(self.esquema.atributos)})"
        cabecera = f"{self.nombre}({self.esquema.nombre}) ="
        filas = "\n".join(str(tuple(t)) for t in sorted(self.tuplas, key=lambda x: x[0]))
        return f"{encabezado}\n{cabecera}\n{filas if filas else '(vacía)'}"


class op:
    @staticmethod
    def seleccion(rel: Relacion, condicion_fn, nombre: str = None):
        nuevas_tuplas = {t for t in rel.tuplas if condicion_fn(t)}
        if nombre is None:
            nombre = f"σ({rel.nombre})"
        return Relacion(nombre, (rel.esquema, nuevas_tuplas))

    @staticmethod
    def proyeccion(rel: Relacion, *atributos, nombre: str = None):
        nuevo_esquema = Esquema(f"Proyeccion_{rel.esquema.nombre}", atributos)
        nuevas_tuplas = {tuple(getattr(t, attr) for attr in atributos) for t in rel.tuplas}
        filas = {nuevo_esquema.Fila(*t) for t in nuevas_tuplas}
        if nombre is None:
            lista_atributos = ",".join(atributos)
            nombre = f"π_{{{lista_atributos}}}({rel.nombre})"
        return Relacion(nombre, (nuevo_esquema, filas))

    @staticmethod
    def union(rel1: Relacion, rel2: Relacion):
        if rel1.esquema.atributos != rel2.esquema.atributos:
            raise ValueError("Esquemas incompatibles para la unión")
        nuevas_tuplas = rel1.tuplas | rel2.tuplas
        return Relacion(f"∪({rel1.nombre},{rel2.nombre})", (rel1.esquema, nuevas_tuplas))

    @staticmethod
    def diferencia(rel1: Relacion, rel2: Relacion):
        if rel1.esquema.atributos != rel2.esquema.atributos:
            raise ValueError("Esquemas incompatibles para la diferencia")
        nuevas_tuplas = rel1.tuplas - rel2.tuplas
        return Relacion(f"−({rel1.nombre},{rel2.nombre})", (rel1.esquema, nuevas_tuplas))

    @staticmethod
    def producto_cartesiano(rel1: Relacion, rel2: Relacion):
        nuevos_atributos = tuple(rel1.esquema.atributos + rel2.esquema.atributos)
        nuevo_esquema = Esquema(f"{rel1.esquema.nombre}_x_{rel2.esquema.nombre}", nuevos_atributos)
        nuevas_tuplas = set()
        for t1 in rel1.tuplas:
            for t2 in rel2.tuplas:
                nueva_tupla = t1 + t2
                nuevas_tuplas.add(nuevo_esquema.Fila(*nueva_tupla))
        return Relacion(f"×({rel1.nombre},{rel2.nombre})", (nuevo_esquema, nuevas_tuplas))


# Ejemplo de uso
clientes = Esquema('Esquema-Cliente', (
    'nroCliente', 'dni', 'apellido', 'nombre', 'direccion', 'localidad', 'telefono'))

r1 = Relacion("r1", clientes.add(
    ('1', '45433', 'carpincho', 'cosmo', 'siempre viva', 'ensenada', '241234'),
    ('2', '23341', 'argento', 'pepe', '1 y 60', 'quilmes', '134114'),
    ('3', '34123', 'gomez', 'german', '3 y 44', 'ensenada', '123434'),
    ('4', '21453', 'velazques', 'ana', '44 y 20', 'berisso', '24544'),
))

print(r1)

r2 = op.seleccion(r1, lambda f: f.localidad == 'ensenada')
print("\nClientes de Ensenada:")
print(r2)

r3 = op.proyeccion(r2, 'apellido', 'nombre')
print("\nProyección apellido y nombre de clientes de Ensenada:")
print(r3)
