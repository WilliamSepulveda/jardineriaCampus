
from tabulate import tabulate
import modules.getClients as clientes
import modules.getOficina as Oficina
import modules.getEmpleados as empleados
import modules.getpedido as pedido

# print(tabulate(pedido.getAllListadoPedidosEntregadosMesEnero(), tablefmt='rounded_grid'))

if(__name__ =="__main__"):

    print("""
    __  ___                    ____       _            _             __
   /  |/  /__  ____  __  __   / __ \_____(_)___  _____(_)___  ____ _/ /
  / /|_/ / _ \/ __ \/ / / /  / /_/ / ___/ / __ \/ ___/ / __ \/ __ `/ / 
 / /  / /  __/ / / / /_/ /  / ____/ /  / / / / / /__/ / /_/ / /_/ / /  
/_/  /_/\___/_/ /_/\__,_/  /_/   /_/  /_/_/ /_/\___/_/ .___/\__,_/_/   
                                                    /_/                
                        1.cliente
                        2.oficina 
                        3.empleados
                        4.pedidos
    
""")

opcion = int(input("\nseleccione una de las opciones: "))
if(opcion == 1):
    clientes.menu()
    if(opcion == 2):
        Oficina.menu()
    if(opcion == 3):
        empleados.menu()
    if(opcion == 4):
        pedido.menu()






