from tabulate import tabulate
import os 
import requests

def getAllData():
    #json-server storage/producto.json -b 5501
    peticion = requests.get ("http://172.16.102.108:5501")
    data = peticion.json()
    return  data

def getproductCodigo(codigo):
    for val in getAllData():
        if(val.get('codigo_producto')== codigo):
            return[val]
# Devuelve un listado con todos los productos que pertenecen a la gama Ornamentales 
# y que tienen más de 100 unidades en stock. El listado deberá estar ordenado por su precio de venta, 
# mostrando en primer lugar los de mayor precio.
def getAllStockPriceGama(gama, stock):
    condicciones =[]
    for val in getAllData():
        if(val.get("gama") == gama and val.get("cantidad_en_stock") >= stock):
            condicciones.append(val)
    def price(val):
        return val.get("precio_venta" )
    condicciones. sort(key=price, reverse=True)
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
        os.system("clear")
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

        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1) :
            gama = input ("Ingrese la gama que deseas filtar: ")
            stock = int(input ("Ingrese las unidades que deseas mostrar: "))
            print(tabulate(getAllStockPriceGama(gama, stock), headers="keys", tablefmt="github"))
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



        
