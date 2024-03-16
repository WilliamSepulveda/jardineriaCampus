import os
import json
import requests
from tabulate import tabulate
import modules.Validaciones as vali
import modules.getpedido as pe

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
                                                                                    
            ██████╗  █████╗ ████████╗ ██████╗ ███████╗    ██████╗ ███████╗          
            ██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝    ██╔══██╗██╔════╝          
            ██║  ██║███████║   ██║   ██║   ██║███████╗    ██║  ██║█████╗            
            ██║  ██║██╔══██║   ██║   ██║   ██║╚════██║    ██║  ██║██╔══╝            
            ██████╔╝██║  ██║   ██║   ╚██████╔╝███████║    ██████╔╝███████╗          
            ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝    ╚═════╝ ╚══════╝          
                                                                                    
                    ██████╗ ███████╗██████╗ ██╗██████╗  ██████╗ ███████╗            
                    ██╔══██╗██╔════╝██╔══██╗██║██╔══██╗██╔═══██╗██╔════╝            
                    ██████╔╝█████╗  ██║  ██║██║██║  ██║██║   ██║███████╗            
                    ██╔═══╝ ██╔══╝  ██║  ██║██║██║  ██║██║   ██║╚════██║            
                    ██║     ███████╗██████╔╝██║██████╔╝╚██████╔╝███████║            
                    ╚═╝     ╚══════╝╚═════╝ ╚═╝╚═════╝  ╚═════╝ ╚══════╝            
                1. agregar nuevo pedido 
                0. atras             
            """)
        opcion = input("\nSeleccione una de las opciones: ")
        if(vali.ValidacionesCodigo(opcion) is not None):
            opcion = int(opcion)
            if(opcion >= 0 and opcion <= 1):
                if (opcion == 1):
                    print(tabulate(postPedido(), headers="keys", tablefmt="rounded_grid"))
                    input("precione una tecla para continuar....")
                elif (opcion == 0):
                    break

def getAllDataPagos():
    #json-server storage/pago.json -b 5504
    peticion = requests.get("http://localhost:5504")
    data = peticion.json()
    return data 

def nuevoCodigoPedido():
    codigodelCliente = list()
    for val in pe():
        codigodelCliente.append(val.get("codigo_empleado"))
        if codigodelCliente:
            return max(codigodelCliente) +  1
        else:
            return 1

def postPedido():
    pedido = {
        "codigo_pedido": nuevoCodigoPedido(),
        "fecha_pedido": input("Ingrese la fecha del pedido: "),
        "fecha_esperada": input("Ingrese la fecha esperada: "),
        "fecha_entrega": input("Ingrese la fecha de entrega: "),
        "estado": input("Ingrese el estado del pedido: "),
        "comentario": input("Ingrese un comentario: "),
        "codigo_cliente": int(input("Ingrese el codigo del cliente: "))  
    }
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://localhost:5504", headers=headers, data=json.dumps(pedido))
    res = peticion.json()
    return [res]               
                                                              

