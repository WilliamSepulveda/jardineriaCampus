from tabulate import tabulate
import modules.getClients as cliente

print(tabulate(cliente.getAllClientPaisRegionCiudad("Australia"),tablefmt= "grid"))

# print(tabulate(cliente.getAllClientPaisRegionCiudad("Australia")))


