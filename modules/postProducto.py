import os
from tabulate import tabulate
import json
import requests
import modules.getgamas as gG
import re 
import modules.getproducto as gP
def postProducto():


def postproducto():
    # json-server storage/producto.json -b 5501
    producto = dict()
    while True:
        try:
            #expresion regular que valide de una cadena numeros y letras en mayusculas
            if(not producto.get("codigo_producto ")):
                codigo = input("ingresa el codigo del producto: ")
                if(re.match(r'^[A-Z]{2}-[0-9]{3}$', codigo) iss not None):
                    data = gP.getproductCodigo(codigo)
                    if(data):
                        print(tabulate(data, headers="keys", tablefmt="rounded_grid"))
                        raise Exception("el codigo del producto ya existe")
                    else:
                        producto["codigo_producto"] = codigo
                else:
                    raise Exception("el codigo del producto NO cumple con el estandar establecido")
                    
                #expresion regular que valida de una cadena solo letras para que las primeras 
                if(not producto.get("nombre")):
                    nombre = input("ingresa el nimbre del producto: ")
                    if(re.match(r'^([A-Z][a-z]\s)+$', nombre) is not None):
                        producto["nombre"] = nombre
                        break
                else:
                    raise Exception("el codigo del producto NO cumple con el estandar establecido")
                            
        except Exception as error:
            print(error)
    print(producto)
def menu():
        # # json-server storage/producto.json -b 5501
    # producto = {
    #     "codigo_producto": input("Ingrese el codigo del producto: "),
    #     "nombre": input ("Ingrese el nombre del producto: "),
    #     "gama": gG.getAllNombre()[int(input("Selecione la gama:\n"+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())])))],
    #     "dimensiones": input("Ingrse la dimensiones del producto: "),
    #     "proveedor": input("Ingrse el proveedor del producto: "),
    #     "descripcion": input("Ingrse el descripcion del producto: "),
    #     "cant#idad_en_stock": float(input("Ingrse el cantidad en stock: ")),
    #     "precio_venta": float(input("Ingrse el precio de ventas: ")),
    #     "precio_proveedor": float(input("Ingrse el precio del proveedor: "))
    # }    
    #json-server storage/producto.json -b 5501
    while True:
        os.system("clear")
        print("""              

 █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗██╗███████╗████████╗██████╗  █████╗ ██████╗     
██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗    
███████║██║  ██║██╔████╔██║██║██╔██╗ ██║██║███████╗   ██║   ██████╔╝███████║██████╔╝    
██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║██║╚════██║   ██║   ██╔══██╗██╔══██║██╔══██╗    
██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║██║███████║   ██║   ██║  ██║██║  ██║██║  ██║    
╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    
                                                                                        
                        ██████╗  █████╗ ████████╗ ██████╗ ███████╗                      
                        ██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝                      
                        ██║  ██║███████║   ██║   ██║   ██║███████╗                      
                        ██║  ██║██╔══██║   ██║   ██║   ██║╚════██║                      
                        ██████╔╝██║  ██║   ██║   ╚██████╔╝███████║                      
                        ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝                      
                                                                                        
██████╗ ███████╗    ██████╗ ██████╗  ██████╗ ██████╗ ██╗   ██╗ ██████╗████████╗ ██████╗ 
██╔══██╗██╔════╝    ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██║   ██║██╔════╝╚══██╔══╝██╔═══██╗
██║  ██║█████╗      ██████╔╝██████╔╝██║   ██║██║  ██║██║   ██║██║        ██║   ██║   ██║
██║  ██║██╔══╝      ██╔═══╝ ██╔══██╗██║   ██║██║  ██║██║   ██║██║        ██║   ██║   ██║
██████╔╝███████╗    ██║     ██║  ██║╚██████╔╝██████╔╝╚██████╔╝╚██████╗   ██║   ╚██████╔╝
╚═════╝ ╚══════╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝  ╚═════╝   ╚═╝    ╚═════╝ 
         1. guardar producto nuevo 
         0. atras                                                                               
        """)
        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            print(tabulate(postproducto(), headers="keys", tablefmt="rounded_grid"))
            input("seleccione una tecla para continuar...")
        elif(opcion == 0):
            break

         # # json-server storage/producto.json -b 5501
    # producto = {
    #     "codigo_producto": input("Ingrese el codigo del producto: "),
    #     "nombre": input ("Ingrese el nombre del producto: "),
    #     "gama": gG.getAllNombre()[int(input("Selecione la gama:\n"+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())])))],
    #     "dimensiones": input("Ingrse la dimensiones del producto: "),
    #     "proveedor": input("Ingrse el proveedor del producto: "),
    #     "descripcion": input("Ingrse el descripcion del producto: "),
    #     "cant#idad_en_stock": float(input("Ingrse el cantidad en stock: ")),
    #     "precio_venta": float(input("Ingrse el precio de ventas: ")),
    #     "precio_proveedor": float(input("Ingrse el precio del proveedor: "))
    # }    
    #json-server storage/producto.json -b 5501