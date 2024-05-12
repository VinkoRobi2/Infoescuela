import json
import time 
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

def Eliminar():
    with open (const,'r+') as archivo:
     data = json.load(archivo)
     codigo = int(input("Ingresa el código del producto a eliminar: "))
     for producto in data:
         if producto['Codigo'] == codigo:
             data.remove(producto)
             print("El producto fue elimnado exitosamente")
    with open(const, "w") as archivo:
        json.dump(data, archivo, indent=4)



def VenderProducto():
    with open(const, "r") as archivo:
        data = json.load(archivo)
    codigo = int(input("Ingresa el código del producto a vender: "))
    for producto in data:
        if producto['Codigo'] == codigo:
            if producto['Stock'] > 0:
                producto['Stock'] -= 1
                Stock = producto["Stock"]
                print("El precio del producto es:", producto['Precio'])
                print("El Stock es: ", Stock)
                print("Item vendido")
            else:
                print("No hay stock disponible para este producto.")
            break 
    else:
        print("Codigo de producto no válido")
    with open(const, "w") as archivo:
        json.dump(data, archivo, indent=4)


def Quehacer():
    while True:
        time.sleep(3)
        Bienvenida()
        ins = input("¿Qué vas a hacer? ").upper()
        if ins == "I":
            AbrirJson()
        elif ins == "S":
            print("¡Hasta luego!")
            break
        elif ins == "V":
            VenderProducto()
        elif ins == "E":
            Eliminar()
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

Quehacer()
