from tabulate import tabulate
from modules.getproducto import getAllData
from modules.crudClientes import getAllCliente
from modules.crudEmpleado import getAllEmpleado
import requests
import os
import modules.Validaciones as val 

def getAllCliente():
    peticion = requests.get("http://154.38.171.54:5001/cliente")
    data = peticion.json()
    return data

def getAllClientName():
    clienteName = list()
    for val in   getAllCliente():       
        codigoName = dict({            
        "codigo": val.get('codigo_cliente'),
        "nombre": val.get('nombre_cliente')
    })
        clienteName.append(codigoName)
    return clienteName

def getOneClientCodigo(codigo):
    for val in  getAllCliente():
        if(val.get('codigo_cliente') == codigo):
            return[{
                "codigo": val.get('codigo_cliente'),
                "nombre" :val.get('nombre_cliente'),
            }]      

def getAllClientCreditCiudad(limiteCredit,ciudad):
    clienteCredit =list()
    for val in   getAllCliente():
        if(val.get('limite_credito') >= limiteCredit and val.get('ciudad') == ciudad):
            clienteCredit.append({
                "codigo": val.get("codigo_cliente"),
                "responsable": val.get("nombre_cliente"),
                "director": f'{val.get("nombre_contacto")} {val.get("nombre_contacto")}',
                "apellidos": val.get("apellido_contacto"),
                "telefono": val.get("telefono"),
                "fax": val.get("fax"),
                "direcciones": val.get("codigo_cliente"),
                "origen": f'{val.get("pais")} {val.get("region")} {val.get("ciudad")} {val.get("codigo_postal")}',
                "codigo asesor": val.get("codigo_cliente"),
                "credito": val.get("limite_credito")
            })
    return clienteCredit
        
# obtener todos los clientes de un pais, una region y una ciudad(pais, region, ciudad)
def getAllClientPaisRegionCiudad(pais,region= None,ciudad= None):
    clientZone = list()
    for val in   getAllCliente():
        if(val.get('pais') == pais):
            if((region is None or val.get('region') == region)):
                if((ciudad is None or val.get('ciudad') == ciudad)):
                    clientZone.append({
                "codigo": val.get('codigo_cliente'),
                "Responsable": val.get('nombre_cliente'),
                "Director": f"{val.get('nombre_contacto')} {val.get('apellido_contacto')}",
                "Telefono": val.get('telefono'),
                "Fax": val.get('fax'),
                "Direcciones": f"{val.get('linea_direccion1')} {val.get('linea_direccion2')}",
                "Origen": f"{val.get('pais')} {val.get('region')} {val.get('ciudad')} {val.get('codigo_postal')}",
                "Codigo del asesor": val.get('codigo_empleado_rep_ventas'),
                "Credito": val.get('limite_credito')    
                })
    return clientZone 

def getClientCodePostal(postal):
    clientpostal = list()
    for val in   getAllCliente():
        if (val.get('codigo_postal') == postal):
            clientpostal.append(
                        {
                        "codigo": val.get('codigo_cliente'),
                        "Responsable": val.get('nombre_cliente'),
                        "Director": f"{val.get('nombre_contacto')} {val.get('apellido_contacto')}",
                        "Telefono": val.get('telefono'),
                        "Fax": val.get('fax'),
                        "Direcciones": f"{val.get('linea_direccion1')} {val.get('linea_direccion2')}",
                        "Origen": f"{val.get('pais')} {val.get('region')} {val.get('ciudad')} {val.get('codigo_postal')}",
                        "Codigo del asesor": val.get('codigo_empleado_rep_ventas'),
                        "Credito": val.get('limite_credito')

                    })
    return clientpostal
    
                    
def getAllNombreApellidosDeClientesRepresentanteVentas():
    nombreClienteRepresentanteVentas = list()
    for val in getAllCliente():
        codigoEmpleado = val.get("codigo_empleado_rep_ventas")
        nombreCliente = val.get("nombre_cliente")
        for val in getAllEmpleado():
            if codigoEmpleado == val.get("codigo_empleado") and val.get("puesto") == "Representante Ventas":
                nombreClienteRepresentanteVentas.append({
                    "nombre cliente": nombreCliente,
                    "nombre del representante de ventas": f'{val.get("nombre")} {val.get("apellido1")} {val.get("apellido2")}'
                })
    return nombreClienteRepresentanteVentas

def getNombreContacto(codigo):

    contacClient=[]
    for val in   getAllCliente():
        if(val.get('codigo_cliente') == codigo):

            contacClient.append({
            "codigo_cliente":{val.get('codigo_cliente')},
            "nombre_contacto":{val.get('nombre_contacto')},
            "apellido_contacto":{val.get('apellido_contacto')}
            })

    return contacClient


def getClientesPais(pais):
    ClientesPais=[]
    for val in   getAllCliente():
        if(val.get("pais") == pais):
            ClientesPais.append(
                {
                "codigo_cliente":{val.get("codigo_cliente")},
                "nombre_cliente":{val.get("nombre_cliente")},
                "pais": {val.get("pais")}
                }
        )
    return ClientesPais

def getCityEmploy0(ciudad):
    clientecity = []
    for val in getAllData():
        if(val.get("ciudad")) ==  ciudad and (val.get("codigo_empleado_rep_ventas") ==11) or (val.get("codigo_empleado_rep_ventas") == 30):
            clientecity.append(
                {   
                "codigoCliente": val.get("codigo_cliente"),
                "nombreCliente": val.get("nombre_cliente"),
                "ciudad": val.get("ciudad"),
                "representante_de_ventas": val.get("codigo_empleado_rep_ventas")
                }
            )
            return clientecity
def  getAllClienteRep():
    allclientRep = []
    for val in getAllData():
            for val2 in  getAllCliente():
                if val.get("codigo_empleado_rep_ventas") == val2.get("codigo_empleado") and val2.get("puesto") == "representante de venta":
                    allclientRep.append(
                    {
                        "nombre": val.get("nombre_cliente"),
                        "nombre_rep": val2.get("nombre"),
                        "apellido_rep": f"{val2.get('apellido1')}  {val2.get('apellido2')}"
                    }
                )
    return allclientRep                       



def menu():
    while True:
        os.system("cls")
        print("""


██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗███████╗     ██████╗██╗     ██╗███████╗███╗   ██╗████████╗███████╗███████╗
██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝    ██╔════╝██║     ██║██╔════╝████╗  ██║╚══██╔══╝██╔════╝██╔════╝
██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   █████╗      ██║     ██║     ██║█████╗  ██╔██╗ ██║   ██║   █████╗  ███████╗
██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   ██╔══╝      ██║     ██║     ██║██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  ╚════██║
██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   ███████╗    ╚██████╗███████╗██║███████╗██║ ╚████║   ██║   ███████╗███████║
╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝     ╚═════╝╚══════╝╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚══════╝
                                                                                                                            
                                                                                                                                                
                0. menu anterior                                                    
                1. obtener todos los clientes (codigo y nombre)
                2. obtener un cliente por codigo (codigo y nombre)
                3. obtener la informacion de un cliente segun su limite de credito y ciudad que pertenece (ejem: 3000.0,  San Francisco)
                4. obtener todos los clientes de un pais, una region y una ciudad(pais, region, ciudad)
                5. obtener el nombre de contacto de un cliente (codigo del cliente)
                6. obtener segun el pais 
                7. obtener nombre de los clientes segun codigo postal
                8. listado con combre del cliente  y su representante de venta 
        """)
        opcion = input("\nSelecione una de las opciones: ")
        if(val.validacionOpciones(opcion) is not None):
            opcion = int(opcion)
            if(opcion >= 0 and opcion <= 9):

                if(opcion == 1):
                        print(tabulate(getAllClientName(), headers="keys", tablefmt="rounded_grid"))
                elif(opcion == 2):
                        codigoCliente = int(input("Ingrese el codigo del cliente: "))
                        print(tabulate(getOneClientCodigo(codigoCliente), headers="keys", tablefmt="rounded_grid"))
                elif(opcion == 3):
                        limite = float(input("Ingrese el limite de credito de los clientes que deseas vizualizar: "))
                        ciudad = input("Ingrese el nombre de la ciudad que deseas filtrar los clientes: ")
                        print(tabulate(getAllClientCreditCiudad(limite, ciudad), headers="keys", tablefmt="rounded_grid"))
                elif(opcion == 4):
                        pais = input('Ingresa el pais: ') 
                        region = input('Ingresa la region: ') or None
                        ciudad = input('Ingresa la ciudad: ') or None
                        print(tabulate(getAllClientPaisRegionCiudad(pais = pais, region = None, ciudad = None ), headers="keys", tablefmt="rounded_grid"))
                elif(opcion == 5):
                        codigo = int(input('Ingrese el codigo del cliente: '))
                        print(tabulate(getNombreContacto(codigo), headers="keys", tablefmt="rounded_grid"))
                elif(opcion == 6):
                        pais = input('ingrese el pais: ')
                        print(tabulate(getClientesPais(pais), headers="keys", tablefmt="rounded_grid"))
                elif (opcion == 7):
                        codigo_postal = input("Ingrese el codigo postal del cliente que deseas filtrar: ")
                        print(tabulate(getClientCodePostal(codigo_postal), headers="keys", tablefmt="github"))
                elif (opcion == 8):
                        print(tabulate(getAllNombreApellidosDeClientesRepresentanteVentas(), headers="keys", tablefmt="github"))    
                elif(opcion == 0):
                    break
            input("presione una tecla para continuar....") 