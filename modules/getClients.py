from tabulate import tabulate
import storage.cliente as cli

def getAllClientName():
    clienteName = list()
    for val in cli.clientes:       
        codigoName = dict({            
        "codigo": val.get('codigo_cliente'),
        "nombre": val.get('nombre_cliente')
    })
        clienteName.append(codigoName)
    return clienteName

def getOneClientCodigo(codigo):
    for val in cli.clientes:
        if(val.get('codigo_cliente') == codigo):
            return[{
                "codigo": val.get('codigo_cliente'),
                "nombre" :val.get('nombre_cliente'),
            }]      

def getAllClientCreditCiudad(limiteCredit,ciudad):
    clienteCredit =list()
    for val in cli.clientes:
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
        

def getAllClientPaisRegionCiudad(pais,region=None,ciudad=None):
    clientZone = list()
    for val in cli.clientes:
        if(val.get('pais') == pais):

            if(pais != None or val.get('region' == pais)):
                clientZone.append(val)
            elif(val.get('pais' == None)):

              clientZone.append(val)
    return clientZone 

def getAllClientcodigo_empleado_rep_ventas(codigo_empleado):
        
        clientCodigo = list()
        for val in cli.clientes:
            if(val.get('codigo_empleado' == codigo_empleado)):
                return{
                    "codigo_empleado_rep_ventas":val.get('codigo_empleado'),
                    "nombre_empleado":val.get('nombre_empleao')                   
                }
            clientCodigo.append(val)
        return clientCodigo 

def getNombreContacto(codigo):

    contacClient=[]
    for val in cli.clientes:
        if(val.get('codigo_cliente') == codigo):

           contacClient.append({
            "codigo_cliente":{val.get('codigo_cliente')},
            "nombre_contacto":{val.get('nombre_contacto')},
            "apellido_contacto":{val.get('apellido_contacto')}
           })

    return contacClient


def getClientesPais(pais):
    ClientesPais=[]
    for val in cli.clientes:
       if(val.get("pais") == pais):
           ClientesPais.append(
               {
                   "codigo_cliente":{val.get("codigo_cliente")},
                   "nombre_cliente":{val.get("nombre_cliente")},
                   "pais": {val.get("pais")}
               }
           )
    return ClientesPais

def menu():
    print(f"""

d8888b. d88888b d8888b.  .d88b.  d8888b. d888888b d88888b      d8888b. d88888b       .o88b. db      d888888b d88888b d8b   db d888888b d88888b .d8888. 
88  `8D 88'     88  `8D .8P  Y8. 88  `8D `~~88~~' 88'          88  `8D 88'          d8P  Y8 88        `88'   88'     888o  88 `~~88~~' 88'     88'  YP 
88oobY' 88ooooo 88oodD' 88    88 88oobY'    88    88ooooo      88   88 88ooooo      8P      88         88    88ooooo 88V8o 88    88    88ooooo `8bo.   
88`8b   88~~~~~ 88~~~   88    88 88`8b      88    88~~~~~      88   88 88~~~~~      8b      88         88    88~~~~~ 88 V8o88    88    88~~~~~   `Y8b. 
88 `88. 88.     88      `8b  d8' 88 `88.    88    88.          88  .8D 88.          Y8b  d8 88booo.   .88.   88.     88  V888    88    88.     db   8D 
88   YD Y88888P 88       `Y88P'  88   YD    YP    Y88888P      Y8888D' Y88888P       `Y88P' Y88888P Y888888P Y88888P VP   V8P    YP    Y88888P `8888Y' 
                                                                                                                                                       
                                                                                                                                                       
                                                                     
                1. obtener todos los clientes (codigo y nombre)
                2. obtener un cliente por codigo (codigo y nombre)
                3. obtener la informacion de un cliente segun su limite de credito y ciudad que pertenece (ejem: 3000.0,  San Francisco)
                4. obtener todos los clientes de un pais, una region y una ciudad(pais, region, ciudad)
                5. obtener el nombre de contacto de un cliente (codigo del cliente)
                6. obtener segun el pais        
        """)
    opcion = int(input("\nseleccione una de las opciones: "))
    if(opcion ==1):
        print(tabulate(getAllClientName(),headers="keys", tablefmt='rounded_grid'))

    elif(opcion ==2):
        codigo = int(input("ingrese el codigo del cliente: "))
        print(tabulate(getOneClientCodigo(codigo),headers="keys", tablefmt='rounded_grid'))

        
    elif(opcion == 3):
        limite = float(input("ingrese el limite de credito de los clientes que deseas verfificar: "))
        ciudad = input("ingrese enl nombre de la ciudad que desea filtrar los clientes: ")

        print(tabulate(getAllClientCreditCiudad(limite,ciudad), headers="keys",tablefmt="rounded_grid"))
    elif(opcion == 4):
        pais = input('Ingresa el pais: ') 
        region = input('Ingresa la region: ') or None
        ciudad = input('Ingresa la ciudad: ') or None
        print(tabulate(getAllClientPaisRegionCiudad(pais, region, ciudad), headers="keys", tablefmt="github"))
    elif(opcion == 5):
        codigo = int(input('Ingrese el codigo del cliente: '))
        print(tabulate(getNombreContacto(codigo), headers="keys", tablefmt="rounded_grid"))
    elif(opcion == 6):
        pais = input('ingrese el pais: ')
        print(tabulate(getClientesPais(pais), headers="keys", tablefmt="rounded_grid"))