from tabulate import tabulate
import os
import re
import json
import requests


import modules.getClients as cliente
import modules.getOficina as oficina
import modules.getEmpleados as empleado
import modules.getpedido as pedidos
import modules.getproducto as Repproducto
import modules.crudProductos as CRUDproducto
import modules.getPagos as pago
import modules.menu as men

# ACTIVADORES DE JSON SERVER PARA 1 SOLO:
#  json-server ./storage/producto.json -p 5504 



# ACTIVADORES DE JSON SERVER PARA 2 O MAS(RECOMENDABLE HACER TODOS DE UNA VEZ):
# json-server ./storage/oficina.json -p 5504 & json-server ./storage/producto.json -p 5505 



def menuProducto():
    while True:
        os.system("clear")
        print("""
    ____  _                            _     __               __                                 
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /  ____ ___  ___  ____  __  __    
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /  / __ `__ \/ _ \/ __ \/ / / /    
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /  / / / / / /  __/ / / / /_/ /     
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/ __\__,_/_/  /_/ /_/ /_/\___/_/ /_/\__,_/      
  ____/ /__     ____  _________  ____/ /_  _______/ /_____  _____                                
 / __  / _ \   / __ \/ ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/                                
/ /_/ /  __/  / /_/ / /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  )                                 
\__,_/\___/  / .___/_/   \____/\__,_/\__,_/\___/\__/\____/____/                                  
            /_/                                                                                  
        
            1. Reportes de los productos
            2. Guardar, Actualizar y Eliminar productos
            0. Regresar al menu principal
          
            """)
        opcion = input("\nSelecione una de las opciones: ")
        if(re.match(r'[0-9]+$', opcion) is not None):
            opcion = int(opcion)
            if(opcion>=0 and opcion<=2):
                if(opcion == 1):
                    Repproducto.menu()
                if(opcion == 2):
                    CRUDproducto.menu()
                elif(opcion == 0):
                    break




if(__name__ == "__main__"):


# devuelve un listado con el codigo de pedido codigo cl, 
# fecha esperada y fecha de entrega de los pedidos que no 
# han sido entrregados a tiempo
    
    # peticion = requests.get("http://154.38.171.54:5007/pedidos?estado=Entregado")
    # data = json.dumps(peticion.json(), indent=4)
    # print(data)




    # print(tabulate(pedidos.getAllPedidosEntregadosAtrasadosDeTiempo(), headers="keys", tablefmt="github"))




#     # https://patorjk.com/software/taag/#p=display&h=2&v=2&f=Slant&t=Menu%20Principal
    while True:
        os.system("cls")
        print(""" 
    __  ___                    ____       _            _             __
   /  |/  /__  ____  __  __   / __ \_____(_)___  _____(_)___  ____ _/ /
  / /|_/ / _ \/ __ \/ / / /  / /_/ / ___/ / __ \/ ___/ / __ \/ __ `/ / 
 / /  / /  __/ / / / /_/ /  / ____/ /  / / / / / /__/ / /_/ / /_/ / /  
/_/  /_/\___/_/ /_/\__,_/  /_/   /_/  /_/_/ /_/\___/_/ .___/\__,_/_/   
                                                    /_/                
                        1. Cliente
                        2. Oficina
                        3. Empleado
                        4. Pedidos
                        5. Productos
                        6. pago
                        0. Salir
""") 
        opcion = input("\nSelecione una de las opciones: ")
        if(re.match(r'[0-9]+$', opcion) is not None):
            opcion = int(opcion)
            if(opcion>=0 and opcion<=6):
                if(opcion == 1):
                    cliente.menu()
                elif(opcion == 2):
                    oficina.menu()
                elif(opcion == 3):
                    empleado.menu()
                elif(opcion == 4):
                    pedidos.menu()
                elif(opcion == 5):
                   men.menuProducto()
                elif(opcion == 6):
                    pago.menu()
                elif(opcion == 0):
                    break
        input("seleccione una tecla para continuar.....")
    

        












       






        # data = input("Datos")
        # if(re.match(r'[a-z A-Z]+$', data) is not None):
        #     print("Letras")
        # elif(re.match(r'[0-9.]+$', data) is not None):
        #     print("Numeros")










# import sys
# def menu():
#     contador = 1
#     print("Menu Principal")
#     for nombre, objeto in sys.modules.items():
#         if nombre.startswith("modules"):
#             modulo = getattr(objeto, "__name__", None)
#             if(modulo != "modules"):
#                 print(f"""{contador}. {modulo.split("get")[-1]} """)
#                 contador += 1
# menu()




# import sys
# def menu():
#     contador = 1
#     print("Menu Principal")
#     for nombre, objeto in sys.modules.items():
#         if nombre.startswith("modules"):
#             modulo = getattr(objeto, "__name__", None)
#             if(modulo != "modules"):
#                 print(f"""{contador}. {modulo.split("get")[-1]} """)
#                 contador += 1
# menu()