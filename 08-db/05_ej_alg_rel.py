EPersona = {'nombre': 'EPersona', 'atributos': ('dni', 'apellido', 'nombre', 'teléfono')}
EContratos = {'nombre': 'EContratos', 'atributos': ('NroContrato', 'dni', 'fechaInicioAlquiler', 'monto', 'fechaVtoContra', 'codInmueble')}
EInmuebles = {'nombre': 'EInmuebles', 'atributos': ('codInmueble', 'dirección', 'localidad', 'ambientes', 'expensas*')}
EPropInmueble = {'nombre': 'EPropInmueble', 'atributos': ('cuil', 'codigoInmueble')}
EPropietarios = {'nombre': 'EPropietarios', 'atributos': ('dni', 'fechaNac', 'cuil', 'dirección', 'localidad')}


Dom_dni = 'Conjunto de todos los DNI'
Dom_Contratos = 'Conjunto de todos los contratos'

def dom(atributo: str):
    if atributo == 'dni':
        return f'Conjunto de todos los DNI'

Dom_dni = dom('dni')

class Tupla:
    def __init__(self, esquema, argumentos):
        self.nombre_esquema = esquema['nombre']
        self.relacion = {}
        for i in range(len(esquema['atributos'])):
            self.relacion[esquema['atributos'][i]] = argumentos[i]
        
    def __getitem__(self, key):
        return self.relacion[key]
    
    def __eq__(self, other):
        return self.relacion == other.relacion
    
    def __hash__(self):
        return hash(tuple(sorted(self.relacion.items())))
    
    def __repr__(self):
        return f"Tupla({self.relacion})"

t = Tupla(EPropietarios, ['222222', '10/02/1980', '12222234', '1 y 60', 'Quilmes'])

class Relacion:
    def __init__(self, nombre, esquema):
        self.nombre = nombre
        self.esquema = esquema['nombre']
        self.relacion = set()
    
    def agregar_tupla(self, tupla):
        self.relacion.add(tupla)


rProp = Relacion('relPropietario', EPropietarios)
rProp.agregar_tupla(t)

print(rProp.relacion)

for tupla in rProp.relacion:
    print(tupla['dni'])

# esto es una selección
resultado = {t for t in rProp.relacion if t['dni'] == '222222'}
print(resultado)

print(type(resultado))

def seleccion(relacion: Relacion, predicado) -> set:
    return {t for t in relacion.relacion if predicado(t)}

res = seleccion(rProp, lambda t: t['dni'] == '222222')
print(res)