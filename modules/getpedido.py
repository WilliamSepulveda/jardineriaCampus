# devuelve un listado con el codigo del pedido
# codigo de cliente fecha esperada y fecha de entrega
# de los pedidos que no han sido entregados a tiempo
import storage.pedido as pe
from datetime import datetime

import storage.pedido as pe
from datetime import datetime

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

import storage.pedido as pe
from datetime import datetime

import storage.pedido as pe
from datetime import datetime

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
