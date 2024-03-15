import os
from tabulate import tabulate
import json
import requests
import modules.getgamas as gG

def postproducto():
    # json-server storage/producto.json -b 5501
    producto = {
        "codigo_producto": input("Ingrese el codigo del producto: "),
        "nombre": input ("Ingrese el nombre del producto: "),
        "gama": gG.getAllNombre()[int(input("Selecione la gama:\n"+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())])))],
        "dimensiones": input("Ingrse la dimensiones del producto: "),
        "proveedor": input("Ingrse el proveedor del producto: "),
        "descripcion": input("Ingrse el descripcion del producto: "),
        "cant#idad_en_stock": float(input("Ingrse el cantidad en stock: ")),
        "precio_venta": float(input("Ingrse el precio de ventas: ")),
        "precio_proveedor": float(input("Ingrse el precio del proveedor: "))
    }    
    #json-server storage/producto.json -b 5501
    peticion = requests.post("http://172.16.102.108.5501", data=json.dumps(producto))
    res = peticion.json()
    res["mensaje"] = "producto guardado"
    return [res]

def menu():
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