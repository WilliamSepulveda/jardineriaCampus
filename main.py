import os 
import modules.getClients as cliente
import modules.getOficina as oficina
import modules.getEmpleados as empleado
import modules.getPedido as pedidos
import modules.getproducto as Repproducto
import modules.postproducto as CRUDproducto


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
        opcion = int(input("\nseleccione una de las opciones: "))
        if(opcion == 1):
            Repproducto.menu()
        if(opcion == 2):
                CRUDproducto.menu()
        elif(opcion == 0):
             break
if(__name__ =="__main__"):
     
     while True:
          os.system("clear")
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
                        0. Salir
""")
          
          opcion = int(input("\nSelecione una de las opciones: "))
          if(opcion == 1):
                cliente.menu()
          elif(opcion == 2):
            oficina.menu()
          elif(opcion == 3):
            empleado.menu()
          elif(opcion == 4):
            pedidos.menu()
          elif(opcion == 5):
            menuProducto()
          elif(opcion == 0):
            break


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