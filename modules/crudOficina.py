import os
import json
from urllib import request
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
                                                                                    
                     ██████╗ ███████╗██╗ ██████╗██╗███╗   ██╗ █████╗                
                    ██╔═══██╗██╔════╝██║██╔════╝██║████╗  ██║██╔══██╗               
                    ██║   ██║█████╗  ██║██║     ██║██╔██╗ ██║███████║               
                    ██║   ██║██╔══╝  ██║██║     ██║██║╚██╗██║██╔══██║               
                    ╚██████╔╝██║     ██║╚██████╗██║██║ ╚████║██║  ██║               
                     ╚═════╝ ╚═╝     ╚═╝ ╚═════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝                                     
                1. agregar un nuevo pago 
                0. atras                                                                     

            """)
        opcion = input("\nSeleccione una de las opciones:")
        if(vali.ValidacionesCodigo(opcion) is not None):
            opcion = int(opcion)
            if(opcion>= 0 and opcion<= 1):
                if (opcion == 1):
                    print(tabulate(postOficina(), headers="keys", tablefmt="github"))
                    input("Precione una tecla para continuar.........")
                elif (opcion == 0):
                    break

def getAllDataOficina():
    #json-server storage/oficina.json -b 5505
    peticion = request.get("http://localhost:5505/oficinas")
    data = peticion.json()
    return data 

def getAllCodigoOficina():
    oficinaNombre = list()
    for val in getAllDataOficina():
        oficinaNombre.append(val.get("codigo_oficina"))
        return oficinaNombre
    

def postOficina():
    oficina = {
       "codigo_oficina": input("Ingrese el codigo de la oficina: "),
        "ciudad": input("Ingrese la ciudad: "),
        "pais": input("Ingrese el pais: "),
        "region": input("Ingrese la region: "),
        "codigo_postal": input("Ingrese el codigo postal: "),
        "telefono": input("Ingrese el numero de telefono: "),
        "linea_direccion1": input("Ingrese una linea de direccion: "),
        "linea_direccion2": input("Ingrese otra linea de direccion(opcional): ")  
    }
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://localhost:5505", headers=headers, data=json.dumps(oficina))
    res = peticion.json()
    res["Mensaje"] = "Oficina Guardada"
    return [res]




