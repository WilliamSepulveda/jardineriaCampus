from tabulate import tabulate
import modules.getClients as clientes
import modules.getOficina as Oficina 
import modules.getEmpleados as empleados
import modules.getpedido as pedido
print(tabulate(pedido.getAllPedidosEntregadosAtrasadosDeTiempo(), tablefmt='rounded_grid'))







