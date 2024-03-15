# devuelve un listado con el nombre, apellidos, y email 
# de los empleados cuyo  jefe tiene un codigo de jefe igual  a 7 

from jardineriaCampus.modules.getClients import getAllDataEmpleado
import storage.empleado as em
from tabulate import tabulate
import os

def getAllNombreApellidoemail(codigo):
    NombreApellidoemail = []
    for val in em.empleados:
        if(val.get("codigo_jefe") == codigo):
            NombreApellidoemail.append(
                {
                    "nombre": val.get("nombre"),
                    "Apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                    "email": val.get("email"),
                    "jefe": val.get("codigo_jefe")
                }
            )
    return NombreApellidoemail

# devuelve el nombre, puesto, apellido y email del jefe de la empresa 

def getAllNombrePuestoApellidoEmailJefe(codigo):
    NombrePuestoApellidoEmailJefe = []
    for val in em.empleados:
        if(val.get("codigo_jefe")) == codigo:
            NombrePuestoApellidoEmailJefe.append(
                {                  
                "puesto": val.get("puesto"),
                "nombre": val.get("nombre"),
                "apellidos": f'{val.get("apellido1")} {val.get("apellido2")})',
                "email": val.get("email"),
                "jefe": val.get("jefe") 
                }
            )          
    return NombrePuestoApellidoEmailJefe
    
#Devuelve un listado con el nombre, apellidos y puesto de aquellos empleados que no sean representantes de ventas
def getAllNombreApellidoPuestos():
    NombreApellidoPuestos = []
    for val in em.empleados:
        if (val.get("puesto") != 'Representante Ventas'):
            NombreApellidoPuestos.append({
            "nombre": val.get("nombre"),
            "Apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
            "puesto": val.get("puesto")
        })
    return NombreApellidoPuestos 

def getAllNombresApellidosPuestosRepresentantesDeVentas():
    nombreApellidosPuestos = list()
    for val in getAllDataEmpleado():
        if(val.get("puesto") != 'representante de ventas: '):
            {
                "nombre": val.get("nombre"),
                "apellidos": f'{val.get("apellido_1"),{val.get("apellido_2")}}',
                "puesto": val.get("puesto")
            }
    return nombreApellidosPuestos


def menu():
    while True:
        os.system("clear")
        print(""" 


███╗   ███╗███████╗███╗   ██╗██╗   ██╗    ███████╗███╗   ███╗██████╗ ██╗     ███████╗ █████╗ ██████╗  ██████╗ ███████╗
████╗ ████║██╔════╝████╗  ██║██║   ██║    ██╔════╝████╗ ████║██╔══██╗██║     ██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║    █████╗  ██╔████╔██║██████╔╝██║     █████╗  ███████║██║  ██║██║   ██║███████╗
██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║    ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝  ██╔══██║██║  ██║██║   ██║╚════██║
██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝    ███████╗██║ ╚═╝ ██║██║     ███████╗███████╗██║  ██║██████╔╝╚██████╔╝███████║
╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝     ╚══════╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝
                                                                                                                      
 
                                                                                                                                                                       
        1. Obtener el nombre, apellidos y email de los empleados con el mismo codigo del jefe.
        2. Obtener la informacion de su jefe.
        3. Obtener el listado con el nombre, apellidos y puesto de aquellos empleados que no sean representantes de ventas.
        0. devolver 
    """)
        opcion = int(input("\nseleccione una de las opciones: "))

        if(opcion ==1):
                    codigo = int(input("ingrese el codigo del jefe: "))
                    print(tabulate(getAllNombreApellidoemail(codigo), headers="keys", tablefmt='rounded_grid'))
                    input("Precione una tecla para continuar.........")
        elif(opcion ==2):
                    codigo = int(input("ingrese el codigo del jefe para obtener la informacion: "))
                    print(tabulate(getAllNombrePuestoApellidoEmailJefe(codigo), headers="keys", tablefmt='rounded_grid'))    
                    input("Precione una tecla para continuar.........")
        elif (opcion == 3):
                    print(tabulate(getAllNombresApellidosPuestosRepresentantesDeVentas(), headers="keys", tablefmt="github"))
                    input("Precione una tecla para continuar.........")
        elif (opcion == 0):
            break
        else:   
            print("opcion no valida")