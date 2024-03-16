import os
import json 
import requests
from tabulate import tabulate
import modules.Validaciones as vali

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
                                                                                    
                    ██████╗  █████╗  ██████╗  ██████╗ ███████╗                      
                    ██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗██╔════╝                      
                    ██████╔╝███████║██║  ███╗██║   ██║███████╗                      
                    ██╔═══╝ ██╔══██║██║   ██║██║   ██║╚════██║                      
                    ██║     ██║  ██║╚██████╔╝╚██████╔╝███████║                      
                    ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝                      
                1. agregar nuevo pago
                0. atras                                                                    
            """)       
        opcion = input("\nSeleccione una de las opciones: ")
        if(vali.ValidacionesCodigo(opcion) is not None):
            opcion = int(opcion)
            if(opcion >= 0 and opcion <= 1):
                if (opcion == 1):
                    print(tabulate(postPagos(), headers="keys", tablefmt="rounded_grid"))
                    input("precione una tecla para continuar....")
                elif (opcion == 0):
                    break


def getAllDataPagos():
    #json-server storage/pago.json -b 5504
    peticion = requests.get("http://localhost:5504")
    data = peticion.json()
    return data 


def postPagos():
    pago = {
      "codigo_cliente": int(input("Ingrese el codigo del cliente: ")),
        "forma_pago": input("Ingrese la forma de pago: "),
        "id_transaccion": input("Ingrese la id de la transaccion: "),
        "fecha_pago": input("Ingrese la fecha de pago: "),
        "total": int(input("Ingrese el total pagado: "))  
    }
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://localhost:5504", headers=headers, data=json.dumps(pago))
    res = peticion.json()
    return [res]

                          
        

        