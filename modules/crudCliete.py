import os
import json 
import requests
from tabulate import tabulate

def menu():
    while True:
        os.system("clear")
        print("""

 █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗██╗███████╗████████╗██████╗  █████╗ ██████╗     ██████╗  █████╗ ████████╗ ██████╗ ███████╗    ██████╗ ███████╗     ██████╗██╗     ██╗███████╗███╗   ██╗████████╗███████╗███████╗    
██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗    ██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝    ██╔══██╗██╔════╝    ██╔════╝██║     ██║██╔════╝████╗  ██║╚══██╔══╝██╔════╝██╔════╝    
███████║██║  ██║██╔████╔██║██║██╔██╗ ██║██║███████╗   ██║   ██████╔╝███████║██████╔╝    ██║  ██║███████║   ██║   ██║   ██║███████╗    ██║  ██║█████╗      ██║     ██║     ██║█████╗  ██╔██╗ ██║   ██║   █████╗  ███████╗    
██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║██║╚════██║   ██║   ██╔══██╗██╔══██║██╔══██╗    ██║  ██║██╔══██║   ██║   ██║   ██║╚════██║    ██║  ██║██╔══╝      ██║     ██║     ██║██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  ╚════██║    
██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║██║███████║   ██║   ██║  ██║██║  ██║██║  ██║    ██████╔╝██║  ██║   ██║   ╚██████╔╝███████║    ██████╔╝███████╗    ╚██████╗███████╗██║███████╗██║ ╚████║   ██║   ███████╗███████║    
╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝    ╚═════╝ ╚══════╝     ╚═════╝╚══════╝╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚══════╝    
                                                                                                                                                                                                                            
              1. agrgar nuevo cliente
              0. atras              
              
            """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if (opcion == 1):
            print(tabulate(postEmpleados(), headers="keys", tablefmt="rounded_grid"))
            input("precione una tecla para comtinuar....")
        elif(opcion == 0):
            break
        else:
            print("opcion no valida")

def getAllCliente():
 #json-server storage/cliente.json -b 5507
    peticion = requests.get("http://localhost:5507")
    data = peticion.json()
    return data

def nuevoCodigoCliente():
    codigodelCliente = list()
    for val in getAllCliente():
        codigodelCliente.append(val.get("codigo_cliente"))
    if codigodelCliente:
        return max(codigodelCliente) + 1
    else:
        return 1
    

def postEmpleados():
    cliente = {
        "codigo_cliente": nuevoCodigoCliente(),
        "nombre_cliente": input("Ingrese el nombre del cliente: "),
        "nombre_contacto": input("Ingrese el nombre del contacto: "),
        "apellido_contacto": input("Ingrese el apellido de contacto: "),
        "telefono": input("Ingrese el numero de telefono: "),
        "fax": input("Ingrese el fax: "),
        "linea_direccion1": input("Ingrese una linea de direccion: "),
        "linea_direccion2": input("Ingrese otra linea de direccion(opcional): "),
        "ciudad": input("Ingrese la ciudad: "),
        "region": input("Ingrese la region(opcional): "),
        "pais": input("Ingrese el pais: "),
        "codigo_postal": input("Ingrese el codigo postal: "),
        "codigo_empleado_rep_ventas": int(input("Ingrese el codigo de empelado: ")),
        "limite_credito": float(input("Ingrese el limite de credito: "))
    }
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://localhost:5507", headers=headers, data=json.dumps(cliente))
    res = peticion.json()
    res["Mensaje"] = "Cliente Agregado"
    return [res]
