import modules.crudPedidos as pe
from datetime import datetime
import os
import requests
from tabulate import tabulate
import modules.Validaciones as vali
import re


def getAllDataPedido():
    #json-server ./storage/pedido.json -p 5506
    peticion = requests.get("http://154.38.171.54:5007/pedidos")
    data = peticion.json()
    return data 



def getAllEstadoPedido():
    pedidosEntregado = list()
    peticion = requests.get("http://154.38.171.54:5007/pedidos?estado=")
    data = peticion.json()
    for val in data:
    
        pedidosEntregado.append(
            {              
            "codigo": val.get("codigoPedido"),
            "estado": val.get("estado") 
            }
        )
    return pedidosEntregado

def getAllPedidosEntregadosAtrasadosDeTiempo():
    pedidosEntregados = list()
    peticion = requests.get("http://154.38.171.54:5007/pedidos?estado=Entregado")
    data = peticion.json()
    
    for val in data:
        if val.get("fechaEntrega") is None:
            val["fechaEntrega"] = val.get("fecha_esperada")
        if val.get("fechaEntrega") is None:
            continue
        
        date_1 = "/".join(val.get("fechaEntrega").split("-")[::-1])
        date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
        start = datetime.strptime(date_1, "%d/%m/%Y")
        end = datetime.strptime(date_2, "%d/%m/%Y")
        diff = end.date() - start.date()
        if (diff.days < 0):
            pedidosEntregados.append({
                    "Codigo de pedido": val.get("codigo_pedido"),
                    "Codigo de cliente": val.get("codigo_cliente"),
                    "Fecha esperada": val.get("fecha_esperada"),
                    "Fecha de entrega": val.get("fechaEntrega"),
                    "Dias de retraso": -(diff.days)
                })
    return pedidosEntregados


# devuelve un listado con el codigo del pedido, codigo cliente, fecha esperada y fecha de entrega de los pedidios cuya 
#fecha de entrega ha sido al menos dos dias antes de la fecha esperada 
def getAllPedidosEntregadosAlMenosDosDiasAnteDeEspera():
    pedidosEntregados = list()
    peticion = requests.get("http://154.38.171.54:5007/pedidos?estado=Entregado")
    data = peticion.json()
    
    for val in data:
        if val.get("fechaEntrega") is None:
            val["fechaEntrega"] = val.get("fecha_esperada")
        if val.get("fechaEntrega") is None:
            continue
        
        date_1 = "/".join(val.get("fechaEntrega").split("-")[::-1])
        date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
        start = datetime.strptime(date_1, "%d/%m/%Y")
        end = datetime.strptime(date_2, "%d/%m/%Y")
        diff = end.date() - start.date()
        if (diff.days >= 2):
            pedidosEntregados.append({
                    "Codigo de pedido": val.get("codigo_pedido"),
                    "Codigo de cliente": val.get("codigo_cliente"),
                    "Fecha esperada": val.get("fecha_esperada"),
                    "Fecha de entrega": val.get("fechaEntrega"),
                    "Dias Anticipados": (diff.days)
                })
    return pedidosEntregados



def getAllListadoDePedidosRechazados2009():
    pedidos_rechazados = []
    peticion = requests.get("http://154.38.171.54:5007/pedidos?estado=Rechazado")
    data = peticion.json()
    for pedido in data:                   
        if "2009"   in pedido.get("fecha_pedido"):       
            pedidos_rechazados.append({
                "estado": pedido.get("estado"),
                "código Pedido": pedido.get("codigo_pedido"),
                "codigo Cliente": pedido.get("codigo_cliente"),
                "Fecha pedido": pedido.get("fecha_pedido")

            }) 
    return pedidos_rechazados
            
# devuelve un listado de todos los pedidos que han sido entregados en le mes de enero de cualquier año         


def getAllListadoPedidosEntregadosMesEnero():
    pedidos_entregados_enero = []
    peticion = requests.get("http://154.38.171.54:5007/pedidos?estado=Entregado")
    data = peticion.json()
    for pedido in data:                   
        fecha_entrega = pedido.get("fechaEntrega")
        if fecha_entrega is not None:
            date_1 = "/".join(fecha_entrega.split("-")[::-1])
            if date_1.startswith("01"):
                pedidos_entregados_enero.append({
                    "Código del pedido": pedido.get("codigo_pedido"),
                    "Código del cliente": pedido.get("codigo_cliente"),
                    "Fecha de entrega": date_1
                }) 
    return pedidos_entregados_enero

def menu():
    while True:
        os.system("cls")
        print("""
              
              
██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗███████╗    ██████╗ ███████╗    ██████╗ ███████╗██████╗ ██╗██████╗  ██████╗ ███████╗
██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝    ██╔══██╗██╔════╝    ██╔══██╗██╔════╝██╔══██╗██║██╔══██╗██╔═══██╗██╔════╝
██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   █████╗      ██║  ██║█████╗      ██████╔╝█████╗  ██║  ██║██║██║  ██║██║   ██║███████╗
██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   ██╔══╝      ██║  ██║██╔══╝      ██╔═══╝ ██╔══╝  ██║  ██║██║██║  ██║██║   ██║╚════██║
██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   ███████╗    ██████╔╝███████╗    ██║     ███████╗██████╔╝██║██████╔╝╚██████╔╝███████║
╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝    ╚═════╝ ╚══════╝    ╚═╝     ╚══════╝╚═════╝ ╚═╝╚═════╝  ╚═════╝ ╚══════╝
                                                                                                                                      
          0. Regresar al menu principal
          1. Obtener todos los estados de los pedidos.
          2. Obtener la lista de los pedidos atrasados.
          3. Obtener todos los pedidos que fueron entregados al menos 2 dias antes de lo esperado.
          4. Mostrar todos los pedidos rechazados en el 2009.
          5. Mostrar los pedidos entregados en el mes de enero sin importar el año.

    """)
        opcion = input("\nSeleccione una de las opciones: ")
        if(re.match(r'[0-9]+$', opcion) is not None):
            opcion = int(opcion)
            if(opcion >= 0 and opcion <= 5):           
                if (opcion == 1):
                    print(tabulate(getAllEstadoPedido(), headers="keys", tablefmt="github"))
                    input("Preccione una tecla para continuar.........")
                elif (opcion == 2):
                    print(tabulate(getAllPedidosEntregadosAtrasadosDeTiempo(), headers="keys", tablefmt="github"))
                    input("Precione una tecla para continuar.........")
                elif (opcion == 3):
                    print(tabulate(getAllPedidosEntregadosAlMenosDosDiasAnteDeEspera(), headers="keys", tablefmt="github"))
                    input("Preccione una tecla para continuar.........")
                elif (opcion == 4):
                
                    print(tabulate(getAllListadoDePedidosRechazados2009(), headers="keys", tablefmt="github"))
                    input("Preccione una tecla para continuar.........")
                elif (opcion == 5):
                    print(tabulate(getAllListadoPedidosEntregadosMesEnero(), headers="keys", tablefmt="github"))
                    input("Preccione una tecla para continuar.........")
                elif (opcion == 0):
                    break
                else:
                    print("Opcion no valida.")