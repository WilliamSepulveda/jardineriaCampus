from tabulate import tabulate

import modules.getClients as clientes
import modules.getOficina as Oficina 
import modules.getEmpleados as empleados
# se imprime los valores
print(tabulate(empleados.getAllNombreApellidoPuestos(), tablefmt= 'gird'))







