from tabulate import tabulate

import modules.getClients as clientes
import modules.getOficina as Oficina
import modules.getEmpleados as empleados
import modules.getproducto as producto
import modules.getpago as pago
import modules.getpedido as pedido


# print(tabulate(producto.getAllStockPriceGama("ornamentales",100), headers="keys", tablefmt="found_grid"))



# if(__name__ =="__main__"):
#     print(f"""
#             __  ___                    ____       _            _             __
#            /  |/  /__  ____  __  __   / __ \_____(_)___  _____(_)___  ____ _/ /
#           / /|_/ / _ \/ __ \/ / / /  / /_/ / ___/ / __ \/ ___/ / __ \/ __ `/ / 
#          / /  / /  __/ / / / /_/ /  / ____/ /  / / / / / /__/ / /_/ / /_/ / /  
#         /_/  /_/\___/_/ /_/\__,_/  /_/   /_/  /_/_/ /_/\___/_/ .___/\__,_/_/   
#                                                         /_/                
#                 1.cliente
#                 2.oficina 
#                 3.empleados
#                 4.pedidos
#     """)
    
# opcion = int(input("\nseleccione una de las opciones: "))

# if(opcion == 1):
#     clientes.menu()
# elif(opcion == 2):
#     Oficina.menu()
# elif(opcion == 3):
#     empleados.menu()
# elif(opcion == 4):
#     pedido.menu()
# elif(opcion == 5):
#     producto.menu()
# elif(opcion == 6):
#     pago.menu()
# else: 
#     print("opcion no valida... ") 




# import json
        
# plantilla = '[{"nombre":"miguel"}, {"nombre": "jhon"},["hola mundo"]]'
# plantilla = json. loads(plantilla)

# example = list([
#    dict({"nombre":"miguel"}), 
#    dict({"nombre":"jhon"}),
#    list(["hola mundo"])
# ])
# example = json.dumps


# print(json[1].get("nombre"))

import json
import requests

empleadoNuevo = {
        "codigo": 999,
        "nombre": "Andres",
        "apellido": "Lizaraso"
}
obtener = requests. post ("[http://172.16.102.108:5007](http://172.16.102.108:5007/)", data=json.dumps (empleadoNuevo))

# eliminar = requests. delete ("http://172.16.102.108:5007/3")

# print(eliminar)




