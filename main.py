import os
import modules.getClients as cliente
import modules.getOficina as oficina
import modules.getEmpleados as empleado
import modules.getpedido as pedidos
import modules.getproducto as Repproducto
import modules.postProducto as CRUDproducto
import re   



# import os
# #from tabulate import tabulate
# import modules.menu as men
# import modules.Validaciones as val


# if(__name__ == "__main__"):
def menuProducto():
    while True:
        os.system("clear")
        print(""" 

██████╗ ██╗███████╗███╗   ██╗██╗   ██╗███████╗███╗   ██╗██╗██████╗  ██████╗      █████╗ ██╗             
██╔══██╗██║██╔════╝████╗  ██║██║   ██║██╔════╝████╗  ██║██║██╔══██╗██╔═══██╗    ██╔══██╗██║             
██████╔╝██║█████╗  ██╔██╗ ██║██║   ██║█████╗  ██╔██╗ ██║██║██║  ██║██║   ██║    ███████║██║             
██╔══██╗██║██╔══╝  ██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║██║  ██║██║   ██║    ██╔══██║██║             
██████╔╝██║███████╗██║ ╚████║ ╚████╔╝ ███████╗██║ ╚████║██║██████╔╝╚██████╔╝    ██║  ██║███████╗        
╚═════╝ ╚═╝╚══════╝╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═╝╚═════╝  ╚═════╝     ╚═╝  ╚═╝╚══════╝        
                                                                                                        
                                ███╗   ███╗███████╗███╗   ██╗██╗   ██╗                                  
                                ████╗ ████║██╔════╝████╗  ██║██║   ██║                                  
                                ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║                                  
                                ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║                                  
                                ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝                                  
                                ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝                                   
                                                                                                        
    ██████╗ ███████╗    ██████╗ ██████╗  ██████╗ ██████╗ ██╗   ██╗ ██████╗████████╗ ██████╗ ███████╗    
    ██╔══██╗██╔════╝    ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██║   ██║██╔════╝╚══██╔══╝██╔═══██╗██╔════╝    
    ██║  ██║█████╗      ██████╔╝██████╔╝██║   ██║██║  ██║██║   ██║██║        ██║   ██║   ██║███████╗    
    ██║  ██║██╔══╝      ██╔═══╝ ██╔══██╗██║   ██║██║  ██║██║   ██║██║        ██║   ██║   ██║╚════██║    
    ██████╔╝███████╗    ██║     ██║  ██║╚██████╔╝██████╔╝╚██████╔╝╚██████╗   ██║   ╚██████╔╝███████║    
    ╚═════╝ ╚══════╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝  ╚═════╝   ╚═╝    ╚═════╝ ╚══════╝                                    
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
# https://patorjk.com/software/taag/#p=display&h=2&v=2&f=Slant&t=Menu%20Principal    
    while True:
        os.system("clear")
        print("""

███╗   ███╗███████╗███╗   ██╗██╗   ██╗    ██████╗ ██████╗ ██╗███╗   ██╗ ██████╗██╗██████╗  █████╗ ██╗     
████╗ ████║██╔════╝████╗  ██║██║   ██║    ██╔══██╗██╔══██╗██║████╗  ██║██╔════╝██║██╔══██╗██╔══██╗██║     
██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║    ██████╔╝██████╔╝██║██╔██╗ ██║██║     ██║██████╔╝███████║██║     
██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║    ██╔═══╝ ██╔══██╗██║██║╚██╗██║██║     ██║██╔═══╝ ██╔══██║██║     
██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝    ██║     ██║  ██║██║██║ ╚████║╚██████╗██║██║     ██║  ██║███████╗
╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝ 
                        1. Cliente
                        2. Oficina
                        3. Empleado
                        4. Pedidos
                        5. Productos
                        0. Salir
""")

        opcion = input("\nSeleccione una de las opciones: ")
        if re.match(r'^[0-5]$', opcion):
                opcion = int(opcion)
                if 0 < opcion < 6:
                    if opcion == 1:
                        cliente.menu()
                    elif opcion == 2:
                        oficina.menu()
                    elif opcion == 3:
                        empleado.menu()
                    elif opcion == 4:
                        pedidos.menu()
                    elif opcion == 5:
                        menuProducto()
                    elif opcion == 0:
                        break
                else:
                    print("Opción inválida. Por favor, seleccione un número entre 0 y 5.")





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