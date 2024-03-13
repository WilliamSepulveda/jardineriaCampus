from tabulate import tabulate
import modules.postProducto as psPro
import json
import requests

def getAllData():
    #json-server storage/producto.json -b 5501
    peticion = requests.get ("")
    data = peticion.json()
    return  data

def getAllStockPriceGama(gama, stock):
    condicciones =list()
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
            "proveedor": val.get("proveedor") 
        }

def menu():
    while True:
        print("""
          
                            _                                  _            _        
                           | |                                | |          | |       
  _ __ ___ _ __   ___  _ __| |_ ___  ___   _ __  _ __ ___   __| |_   _  ___| |_ ___  
 | '__/ _ \ '_ \ / _ \| '__| __/ _ \/ __| | '_ \| '__/ _ \ / _` | | | |/ __| __/ _ \ 
 | | |  __/ |_) | (_) | |  | ||  __/\__ \ | |_) | | | (_) | (_| | |_| | (__| || (_) |
 |_|  \___| .__/ \___/|_|   \__\___||___/ | .__/|_|  \___/ \__,_|\__,_|\___|\__\___/ 
          | |                             | |                                        
          |_|                             |_|                                        
                1. obtener todos los productos de una categoria ordenando sus precios de venta, tambien que su cantidad de inventario sea su
                2. guardar
                0. regresar al menu principal    
              
              
              
            """ )

        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1) :
            gama = input ("Ingrese la gama que deseas filtar: ")
            stock = int(input ("Ingrese las unidades que deseas mostrar: "))
            print(tabulate(getAllStockPriceGama(gama, stock), headers="keys", tablefmt="github"))

        elif(opcion == 2) :
            producto = {
            "codigo_producto": input("Ingrese el codigo del producto: "),
            "nombre": input ("Ingrese el nombre del producto: "),
            "gama": input("Ingrse la gama del producto: "),
            "dimensiones": input("Ingrse la dimensiones del producto: "),
            "proveedor": input("Ingrse el proveedor del producto: "),
            "descripcion": input("Ingrse el descripcion del producto: "),
            "cantidad_en_stock": float(input("Ingrse el cantidad en stock: ")),
            "precio_venta": float(input("Ingrse el precio de ventas: ")),
            "precio_proveedor": float(input("Ingrse el precio del proveedor: "))
        }    
        elif(opcion == 0):
            break 



        
