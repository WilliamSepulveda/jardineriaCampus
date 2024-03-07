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




# def getAllPedidosEntregadosAtrasadosDeTiempo():
#     pedidosEntregado = []
#     for pedidos in pe.pedido:
#         if (pedidos.get("estado") == "Entregado" and pedidos.get("fecha_entrega") is None):
#             pedidos["fecha_entrega"]= pedidos.get("fecha_esperada")
#         if pedidos.get("estado") == "Entregado":

#             date_1 = "/".join(pedidos.get("fecha_entrega").split("-")[::-1])
#             date_2 = "/".join(pedidos.get("fecha_esperada").split("-")[::-1])
#             start = datetime.strptime(date_1, "%d/%m/%Y")
#             end = datetime.strptime(date_2, "%d/%m/%Y")
#             diff = end.date() - start.date()
#             if diff.days < 0 :
#                 pedidosEntregado.append({
#                     "codigo_pedido": pedidos.get("codigo_pedido"),
#                     "codigo_cliente": pedidos.get("codigo_cliente"),
#                     "fecha_esperada": pedidos.get("fecha_esperada"),
#                     "fecha_de_entrega": pedidos.get("fecha_entrega")
#                 })
#     return pedidosEntregado