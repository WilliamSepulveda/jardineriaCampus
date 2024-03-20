import os
from tabulate import tabulate
import modules.Validaciones as vali
from modules.crudPagos import getAllDataPagos as getAllDataPagos
from modules.crudEmpleado import getAllDataEmpleado as em
from modules.crudClientes import getAllCliente as cli
import requests

def getAllDataOficina():
    #json-server storage/pago.json -p 5505
    peticion = requests.get("http://localhost:5505/pagos")
    data = peticion.json()
    return data 




def getAllCodigoClientePago():
    CodigoClientePago = list()
    for val in getAllDataPagos():
        if(val.get("fecha_pago")[0:4] == "2008"):
            CodigoClientePago.append(val.get("codigo_cliente"))
        converted = set(str(item) for item in CodigoClientePago)
    return converted

def getAllPagos2008getAllDataPagos():
    PagosgetAllDataPagos = list()
    for val in getAllDataPagos():
        if val.get("forma de pago") == "getAllDataPagosPal" and  " 2008" in val.get("fecha_Pago"):
            PagosgetAllDataPagos.append(val)
    PagosgetAllDataPagos.sort(key=lambda x: x.get("total"), reverse=True)
    return PagosgetAllDataPagos

def getAllFormasdePago():
    formasdepago = list()
    for val in getAllDataPagos():
        val.get("gorma de pago")
        formasdepago.append(val.get("forma_pago"))
        conjuntoFormaDePago = set(str(item) for item in formasdepago)
    return conjuntoFormaDePago

def getAllNombresClientesRealizaronPagos():
    nombresclientespagos = set()
    for val in cli():
        codigoCliente = val.get("codigo_cliente")
        nombreCliente = val.get("nombre_cliente")
        codigoEmpleado = val.get("codigo_empleado_rep_ventas")
        for val in em():
            nombreRepresentantesVentas =f'{val.get("nombre")} {val.get("apellido1")} {val.get("apellido2")}'
            if codigoEmpleado ==  val.get("codigo_empleado") and val.get("puesto") == "Representantes Ventas":
                for val in getAllDataPagos():
                    if codigoCliente == val.get("codigo_cliente"):
                        nombresclientespagos.add(( 
                            nombreCliente,
                            nombreRepresentantesVentas
                        )),
    return [{"nombre cliente": nombre, "nombre de representante de ventas": representante} for nombre, representante in nombresclientespagos]
def getAllNombreClientesNoRealizaronPagos():
    NombreClientesNoPagos = list()
    for val in cli():
        codigoCliente = val.get("codigo_cliente")
        nombreCliente = val.get("nombre_cliente")
        codigoEmpleado = val.get("codigo_empleado_rep_ventas")
        cliente_con_pago = False
        for val in em():
            nombreRepresentanteVentas = f'{val.get("nombre")} {val.get("apellido1")} {val.get("apellido2")}'
            if codigoEmpleado == val.get("codigo_empleado") and val.get("puesto") == "Representante Ventas":
                for val in getAllDataPagos():
                    if codigoCliente == val.get("codigo_cliente"):
                        cliente_con_pago = True
                        break
                if not cliente_con_pago:
                    NombreClientesNoPagos.append({
                        "nombre cliente": nombreCliente,
                        "nombre de representante de ventas": nombreRepresentanteVentas   
                    })
        return  NombreClientesNoPagos

def menu():        
    while True:
        os.system("clear")
        print("""

██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗███████╗    ██████╗ ███████╗    ██████╗  █████╗  ██████╗  ██████╗ 
██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝    ██╔══██╗██╔════╝    ██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗
██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   █████╗      ██║  ██║█████╗      ██████╔╝███████║██║  ███╗██║   ██║
██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   ██╔══╝      ██║  ██║██╔══╝      ██╔═══╝ ██╔══██║██║   ██║██║   ██║
██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   ███████╗    ██████╔╝███████╗    ██║     ██║  ██║╚██████╔╝╚██████╔╝
╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝    ╚═════╝ ╚══════╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ 
          0. Regresar al menu principal
          1. Obtener codigo cliente de los que realizaron pagos en el 2008.
          2. Obtener la infromacion de los clientes que pagaron con getAllDataPagospal y realizadas en el 2008.
          3. Obtener todas las formas de pago.
          4. Muestra el nombre de los clientes que hayan realizado pagos junto con el nombre de sus representantes de ventas.
          5. Obtener el nombre de los clientes que no hayan realizado pagos junto con el nombre de sus representantes de ventas.                                                                                                                       
        """)
        opcion = input("\nSeleccione una de las opciones: ")
        if vali.validacionOpciones(opcion) is not None:
            opcion = int(opcion)
            if (opcion >= 0 and opcion <= 5):
                if(opcion == 1):
                    print(tabulate(getAllCodigoClientePago()))
                    input("Precione una tecla para continuar.........")
                elif (opcion == 2):
                    print(tabulate(getAllPagos2008getAllDataPagos(), headers="keys", tablefmt="github"))
                    input("Precione una tecla para continuar.........")
                elif (opcion == 3):
                    print(tabulate(getAllFormasdePago()))
                    input("Precione una tecla para continuar.........")
                elif (opcion == 4):
                    print(tabulate(getAllNombreClientesNoRealizaronPagos(), headers="keys", tablefmt="github"))
                    input("Precione una tecla para continuar.........")
                elif (opcion == 5):
                    print(tabulate(getAllNombreClientesNoRealizaronPagos(), headers="keys", tablefmt="github"))
                    input("Precione una tecla para continuar.........")
                elif (opcion == 0):
                    break




