# tipos de datos
# string (cadenas de texto, texto)
nombre = "luis"  # se puede usar "" o ''

edad = 25  # entero int

estatura = 1.75  # flotante float

# booleanos (booleanos)
mayor_de_edad = True
tiene_licencia = False

# listas (listas)
lista_comida = ["pizza", "hamburguesa", "pasta"]
print(lista_comida[0])

# tupla
tupla_numeros = (1, 2, 3, 4, 5)
print(tupla_numeros[0])

# set
set_variados = {"luis", 25, True, 1.75}
print(set_variados)

# diccionarios (diccionarios)
diccionario_persona = {
    "nombre": "luis",
    "edad": 25,
    "estatura": 1.75,
    "mayor_de_edad": True,
    "tiene_licencia": False,
}
print(diccionario_persona["nombre"])

name = 'luis'
last_name = 'nunez'


full_name = f'{name} {last_name} {edad}'
print(full_name)
