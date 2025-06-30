class Esquema:
    def __init__(self, *atributos):
        self.esquema = set(atributos)

class Relacion:
    def __init__(self, nombre: str, esquema: Esquema, tuplas: list[tuple]):
        self.nombre = nombre
        self.esquema = esquema
        self.tuplas = set(tuplas)

class op:
    @staticmethod
    def seleccion(rel: Relacion, condicion_fn):
        nuevas_tuplas = {t for t in rel.tuplas if condicion_fn(t)}

    @staticmethod
    def proyeccion(rel):
        pass
    @staticmethod
    def producto_cartesiano(rel1, rel2):
        pass
    @staticmethod
    def union(rel1, rel2):
        pass
    @staticmethod
    def diferencia(rel1, rel2):
        pass


clientes = Esquema('Esquema-Cliente',('nroCliente', 'dni', 'apellido', 'nombre', 'direccion', 'localidad', 'telefono'))
r1 = Relacion('clientes', clientes, [
                ('1', '45433', 'carpincho', 'cosmo', 'siempre viva', 'ensenada', '241234'),
                ('2', '23341', 'argento', 'pepe', '1 y 60', 'quilmes', '134114'),
                ('3', '34123', 'gomez', 'german', '3 y 44', 'ensenada', '123434'),
                ('4', '21453', 'velazques', 'ana', '44 y 20', 'berisso', '24544'),
                ])

print(r1)

clientes = Esquema('Esquema-Cliente',('nroCliente', 'dni', 'apellido', 'nombre', 'direccion', 'localidad', 'telefono'))
r1 = Relacion(clientes.add(
                ('1', '45433', 'carpincho', 'cosmo', 'siempre viva', 'ensenada', '241234'),
                ('2', '23341', 'argento', 'pepe', '1 y 60', 'quilmes', '134114'),
                ('3', '34123', 'gomez', 'german', '3 y 44', 'ensenada', '123434'),
                ('4', '21453', 'velazques', 'ana', '44 y 20', 'berisso', '24544'),
))