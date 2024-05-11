import json
from tabulate import tabulate
const = 'Objetos.json'
def Bienvenida():
    print("Bienvenido a tu inventario. ¿Qué deseas hacer?")
    print("I: Ver inventario")
    print("V: Vender un producto")
    print("S: Salir")
    print("E: Eliminar un producto")




def AbrirJson():
    with open(const, "r") as archivo:
        data = json.load(archivo)
        encabezado = ["Codigo", "Producto", "Stock", "Precio"]
        filas = [[producto["Codigo"], producto["Producto"], producto["Stock"], producto["Precio"]] for producto in data]
        tabla = tabulate(filas, headers=encabezado, tablefmt="grid")
        print(tabla)


def VenderProducto():
    print('hola')

def Quehacer():
    while True:
        Bienvenida()
        ins = input("¿Qué vas a hacer? ").upper()
        if ins == "I":
            AbrirJson()
        elif ins == "S":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

Quehacer()
