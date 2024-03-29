
from modules.crudEmpleado import getAllEmpleado 
from tabulate import tabulate
import os
import modules.Validaciones as vali 
import requests
# devuelve un listado con el nombre, apellidos, y email 
# de los empleados cuyo  jefe tiene un codigo de jefe igual  a 7

def getAllEmpleado():
    peticion = requests.get("http://154.38.171.54:5003/empleados")
    data = peticion.json()
    return data

def getAllNombreApellidoemail(codigo):
    NombreApellidoemail = []
    for val in getAllEmpleado():
        if(val.get("codigo_jefe") == codigo) and  val.get("codigoJefe") == None:
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
    NombrePuestoApellidoEmailJefe = list()
    for val in getAllEmpleado():
        if((val.get("codigo_empleado") == codigo)):
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
def getAllJefeNombreApellidoEmailJefe(codigo):
    JefeNombreApellidoEmailJefe = list()
    for val in getAllEmpleado():
         if((val.get("codigo_empleado") == codigo)):
              JefeNombreApellidoEmailJefe.append(
                   {
                    "nombre": val.get("nombre"),
                    "apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                    "email": val.get("email"),
                    "puesto": val.get("puesto")    
                   }
              )
               
    return JefeNombreApellidoEmailJefe 

def getAllNombreApellidosPuestoNoRepresentantesDeVentas():
    nombreApellidosPuetos = list()
    for val in getAllEmpleado():
        if(val.get("puesto") != 'Representante Ventas'):
            nombreApellidosPuetos.append(
                {
                    "nombre": val.get("nombre"),
                    "apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                    "puesto": val.get("puesto")
                }
            )
    return nombreApellidosPuetos


def menu():
    while True:
        os.system("cls")
        print(""" 

██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗███████╗    ███████╗███╗   ███╗██████╗ ██╗     ███████╗ █████╗ ██████╗  ██████╗ ███████╗
██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝    ██╔════╝████╗ ████║██╔══██╗██║     ██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   █████╗      █████╗  ██╔████╔██║██████╔╝██║     █████╗  ███████║██║  ██║██║   ██║███████╗
██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   ██╔══╝      ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝  ██╔══██║██║  ██║██║   ██║╚════██║
██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   ███████╗    ███████╗██║ ╚═╝ ██║██║     ███████╗███████╗██║  ██║██████╔╝╚██████╔╝███████║
╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝    ╚══════╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝
                                                                                                                                          
                                                                                                                                                           
        1. Obtener el nombre, apellidos y email de los empleados con el mismo codigo del jefe.
        2. Obtener la informacion de su jefe.
        3. Obtener el listado con el nombre, apellidos y puesto de aquellos empleados que no sean representantes de ventas.
        0. devolver 
    """)

        opcion = input("\nseleccione una de las opciones: ")
        if(vali.validacionOpciones(opcion) is not None):
            opcion = int(opcion)
            if(opcion >= 0 and opcion <= 3):

                if(opcion ==1):
                            codigo = int(input("ingrese el codigo del jefe: "))
                            print(tabulate(getAllNombreApellidoemail(codigo), headers="keys", tablefmt='rounded_grid'))
                            input("Precione una tecla para continuar.........")
                elif(opcion ==2):
                            codigo = int(input("ingrese el codigo del jefe para obtener la informacion: "))
                            print(tabulate(getAllNombrePuestoApellidoEmailJefe(codigo), headers="keys", tablefmt='rounded_grid'))    
                            input("Precione una tecla para continuar.........")
                elif (opcion == 3):
                            print(tabulate(getAllNombreApellidosPuestoNoRepresentantesDeVentas(), headers="keys", tablefmt="github"))
                            input("Precione una tecla para continuar.........")
                elif (opcion == 0):
                    break
                else:   
                    print("opcion no valida")
 