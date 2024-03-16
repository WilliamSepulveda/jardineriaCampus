import os
from tabulate import tabulate
import json
import requests
import re 
import modules.getproducto as gP

    #json-server storage/producto.json -b 5501
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

def getAllDataPagos():
    #json-server storage/pago.json -b 5504
    peticion = requests.get("http://localhost:5504")
    data = peticion.json()
    return data 

def postproducto():
    # json-server storage/producto.json -b 5501
    producto = dict()
    while True:
        try:
            #expresion regular que valide de una cadena numeros y letras en mayusculas
            if(not producto.get("codigo_producto ")):
                codigo = input("ingresa el codigo del producto: ")
                if(re.match(r'^[A-Z]{2}-[0-9]{3}$', codigo) is not None):
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
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://localhost:5501", headers=headers, data=json.dumps(producto))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]
