import storage.pedido as pe
from datetime import datetime
import os
import requests
from tabulate import tabulate

def getAllDataPedido():
    #json-server storage/pedido.json -b 5503
    peticion = requests.get("http://localhost:5503")
    data = peticion.json()
    return data 



def getAllEstadoPedido():
    estadoPedido = list()
    for val in getAllDataPedido():
        estadoPedido.append(
            {
               
                "codigo": val.get("codigo_pedido"),
                "estado": val.get("estado") 
            }
        )

def getAllPedidosEntregadosAtrasadosDeTiempo():
    pedidosEntregado = []
    for val in pe.pedido:
        if val.get("estado") == "Entregado" and val.get("fecha_entrega") is None:
            val["fecha_entrega"] = val.get("fecha_esperada")
        if val.get("estado") == "Entregado":
            date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])

        start = datetime.strptime(date_1, "%d/%m/%Y")
        end = datetime.strptime(date_2, "%d/%m/%Y")
        diff = end.date() - start.date()
        if diff.days < 0:
                pedidosEntregado.append({
                    "código_de_pedido": val.get("codigo_pedido"),
                    "código_de_cliente": val.get("codigo_cliente"),
                    "fecha_esperada": val.get("fecha_esperada"),
                    "fecha_de_entrega": val.get("fecha_entrega"),
                })
    return pedidosEntregado
# solucion punto numero 10
# devuelve un listado con el codigo del pedido, codigo cliente, fecha esperada y fecha de entrega de los pedidios cuya 
#fecha de entrega ha sido al menos dos dias antes de la fecha esperada 

def getAllPedidosEntregadosDosDiasAntes():
    pedidosEntregado = []
    for pedido in pe.pedido:
        if pedido.get("estado") == "Entregado" and pedido.get("fecha_entrega") is None:
            pedido["fecha_entrega"] = pedido.get("fecha_esperada")
        if pedido.get("estado") == "Entregado":
            date_1 = "/".join(pedido.get("fecha_entrega").split("-")[::-1])
            date_2 = "/".join(pedido.get("fecha_esperada").split("-")[::-1])

        start = datetime.strptime(date_1, "%d/%m/%Y")
        end = datetime.strptime(date_2, "%d/%m/%Y")
        diff = end.date() - start.date()
        if diff.days >= 2:
                pedidosEntregado.append({
                    "código_de_pedido": pedido.get("codigo_pedido"),
                    "código_de_cliente": pedido.get("codigo_cliente"),
                    "fecha_esperada": pedido.get("fecha_esperada"),
                    "fecha_de_entrega": pedido.get("fecha_entrega"),
                })
    return pedidosEntregado



# devuelve un listado de todos los pedidos que fueron rechazados en 2009

def getAllListadoDePedidosRechazados2009():
    pedidosrechazados = []
    for pedido in pe.pedido:                 
       if pedido.get("estado") == "Rechazado":
        date_1 = "/".join(pedido.get("fecha_esperada").split("-")[::-1])
        start = datetime.strptime(date_1, "%d/%m/%Y")
        if start.year == 2009:

            pedidosrechazados.append({
                "estado": pedido.get("estado del pedido"),
                "código_de_pedido": pedido.get("codigo_pedido"),
                "código_de_cliente": pedido.get("codigo_cliente"),
                "fecha_esperada": pedido.get("fecha_esperada")
            }) 
    return pedidosrechazados
            
# devuelve un listado de todos los pedidos que han sido entregados en le mes de enero de cualquier año         

def getAllListadoPedidosEntregadosMesEnero():
    pedidosentregados = []
    for pedido in pe.pedido:
        if pedido.get("estado") == "Entregado":
            date_1 = "/".join(pedido.get("fecha_entrega").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            if start.month == "january":

                pedidosentregados.append(
                    {
                    "estado": pedido.get("estado del pedido"),
                    "fecha_de_entrega": pedido.get("fecha_entrega")
                    }
                )
    return pedidosentregados

def menu():
    while True:
        os.system("clear")
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
        opcion = int(input("\nSeleccione una de las opciones: "))
        if (opcion == 1):
            print(tabulate(getAllEstadoPedido(), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.........")
        elif (opcion == 2):
            print(tabulate(getAllPedidosEntregadosAtrasadosDeTiempo(), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.........")
        elif (opcion == 3):
            print(tabulate(getAllPedidosEntregadosDosDiasAntes(), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.........")
        elif (opcion == 4):
            print(tabulate(getAllListadoDePedidosRechazados2009(), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.........")
        elif (opcion == 5):
            print(tabulate(getAllListadoPedidosEntregadosMesEnero(), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.........")
        elif (opcion == 0):
            break
        else:
            print("Opcion no valida")