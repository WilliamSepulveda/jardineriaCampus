from tabulate import tabulate

import modules.getClients as clientes
import modules.getOficina as Oficina 
import modules.getEmpleados as empleados

# print(cliente.getAllClientcodigo_empleado_rep_ventas("codigo_empleado_rep_ventas"))

# print(tabulate(empleados.getAllNombreApellidoemail(7), tablefmt= 'gird'))

print(tabulate(Oficina.getAllCodigoCiudad(), tablefmt= 'gird'))







