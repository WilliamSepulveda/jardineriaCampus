from tabulate import tabulate
import os 
import requests
import re


def getAllData():
    #json-server ./storage/producto.json -p 5507
    peticion = requests.get ("http://154.38.171.54:5008/productos")
    data = peticion.json()
    return  data

def getproductCodigo(codigo):
    peticion = requests.get(f"http://154.38.171.54:5008/productos{codigo}")
    return [peticion.json()] if peticion.ok else []
# Devuelve un listado con todos los productos que pertenecen a la gama Ornamentales 
# y que tienen más de 100 unidades en stock. El listado deberá estar ordenado por su precio de venta, 
# mostrando en primer lugar los de mayor precio.
def getAllStockPriceGama(gama, stock):
    peticion = requests.get(f"http://154.38.171.54:5008/productos?gama={gama}&cantidadEnStock_gte={stock}&_sort=-precio_venta")
    condicciones = peticion.json()
    for i, val in enumerate (condicciones):
        condicciones [i] = {
            "codigo": val.get ("codigo_producto"),
            "venta": val.get ("precio_venta"),
            "nombre": val.get ("nombre"),
            "gama": val.get ("gama"),
            "dimensiones": val.get("dimensiones"),
            "proveedor": val.get("proveedor"),
            "descripcion": f'{val.get("descripcion")[:5]}...' if condicciones[i].get("descripcion") else None,
            "stock": val.get("cantidad_en_stock"),
            "base": val.get("precio_proveedor")
        }
    return condicciones

def menu():
    while True:
        os.system("cls")
        print("""

██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗███████╗███████╗    ██████╗ ██████╗  ██████╗ ██████╗ ██╗   ██╗ ██████╗████████╗ ██████╗ 
██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔════╝    ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██║   ██║██╔════╝╚══██╔══╝██╔═══██╗
██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   █████╗  ███████╗    ██████╔╝██████╔╝██║   ██║██║  ██║██║   ██║██║        ██║   ██║   ██║
██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   ██╔══╝  ╚════██║    ██╔═══╝ ██╔══██╗██║   ██║██║  ██║██║   ██║██║        ██║   ██║   ██║
██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   ███████╗███████║    ██║     ██║  ██║╚██████╔╝██████╔╝╚██████╔╝╚██████╗   ██║   ╚██████╔╝
╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚══════╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝  ╚═════╝   ╚═╝    ╚═════╝ 
                                                                                                                                          

                1. obtener todos los productos de una categoria ordenando sus precios de venta, tambien que su cantidad de inventario sea su
                0. regresar al menu principal    
  
                      
""" )

        opcion = input("\nSelecione una de las opciones: ")
        if(re.match(r'[0-9]+$', opcion) is not None):
            opcion = int(opcion)
            if(opcion>=0 and opcion<=1):            
                if(opcion == 1) :                   
                    gama = input ("Ingrese la gama que deseas filtar: ")
                    stock = int(input ("Ingrese las unidades que deseas mostrar: "))
                    print(tabulate(getAllStockPriceGama(gama, stock), headers="keys", tablefmt="github"))

                    input("seleccione una tecla para continuar.....")
                elif(opcion == 0):
                    break
       # elif(opcion == 2) :
        # #   producto = {
           # "codigo_producto": input("Ingrese el codigo del producto: "),
            #"nombre": input ("Ingrese el nombre del producto: "),
           # "3gama": input("Ingrse la gama del producto: "),
            #"d#imensiones": input("Ingrse la dimensiones del producto: "),
            #"pr#oveedor": input("Ingrse el proveedor del producto: "),
            #"des#cripcion": input("Ingrse el descripcion del producto: "),
            #"cant#idad_en_stock": float(input("Ingrse el cantidad en stock: ")),
            #"precio_venta": float(input("Ingrse el precio de ventas: ")),
            #"precio_proveedor": float(input("Ingrse el precio del proveedor: "))
        #}    



        
