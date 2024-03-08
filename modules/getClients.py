from tabulate import tabulate
import storage.cliente as cli

def getAllClientName():
    clienteName = list()
    for  val in cli.clientes:
        codigoName = dict({
        "codigo_cliente",val.get('codigo_cliente'),
        "nombre_cliente",val.append('nombre_cliente')
    })
    clienteName.append(codigoName)
    return clienteName

def getOneClientCodigo(codigo):
    for val in cli.clientes:
        if(val.get('codigo_cliente') == codigo):
            return[{
                "codigo_cliente": val.get('codigo_cliente'),
                "nombre_cliente":val.get('nombre_cliente')
            }]      

def getAllClientCreditCiudad(limiteCredit,ciudad):
    clienteCredit =list()
    for val in cli.clientes:
        if(val.get('limite_credito') >= limiteCredit and val.get('ciudad') == ciudad):
            clienteCredit.append({
                "codigo": val.get("codigo_cliente"),
                "responsable": val.get("nombre_cliente"),
                "director": {val.get("nombre_contacto")} {val.get("nombre_contacto")},
                "apellidos": val.get("apellido_contacto"),
                "telefono": val.get("telefono"),
                "fax": val.get("fax"),
                "direcciones": val.get("codigo_cliente"),
                "origen": f"{val.get("pais")} {val.get("region")} {val.get("ciudad")} {val.get("codigo_postal")}
                "codigo asesor": val.get("codigo_cliente"),
                "credito": val.get("limite_credito"),
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

def menu():
    print(f"""
          
                                                                                                                                              
                                                                     ,,                      ,,   ,,                                          
                                              mm                   `7MM                    `7MM   db                     mm                   
                                              MM                     MM                      MM                          MM                   
`7Mb,od8 .gP"Ya `7MMpdMAo.  ,pW"Wq.`7Mb,od8 mmMMmm .gP"Ya       ,M""bMM  .gP"Ya      ,p6"bo  MM `7MM  .gP"Ya `7MMpMMMb.mmMMmm .gP"Ya  ,pP"Ybd 
  MM' "',M'   Yb  MM   `Wb 6W'   `Wb MM' "'   MM  ,M'   Yb    ,AP    MM ,M'   Yb    6M'  OO  MM   MM ,M'   Yb  MM    MM  MM  ,M'   Yb 8I   `" 
  MM    8M""""""  MM    M8 8M     M8 MM       MM  8M""""""    8MI    MM 8M""""""    8M       MM   MM 8M""""""  MM    MM  MM  8M"""""" `YMMMa. 
  MM    YM.    ,  MM   ,AP YA.   ,A9 MM       MM  YM.    ,    `Mb    MM YM.    ,    YM.    , MM   MM YM.    ,  MM    MM  MM  YM.    , L.   I8 
.JMML.   `Mbmmd'  MMbmmd'   `Ybmd9'.JMML.     `Mbmo`Mbmmd'     `Wbmd"MML.`Mbmmd'     YMbmd'.JMML.JMML.`Mbmmd'.JMML  JMML.`Mbmo`Mbmmd' M9mmmP' 
                  MM                                                                                                                          
                .JMML.                                                                                                                        

                1. obtener todos los clientes (codigo y nombre)
                2. obtener un cliente por codigo (codigo y nombre)
                3. obtener la informacion de un cliente segun su limite de credito y ciudad que pertenece (ejem: 3000.0,  San Francisco)
          
        """)
    opcion = int(input("\nseleccione una de las opciones: "))
    if(opcion ==1):
         print(tabulate(getAllClientName(),headers="keys", tablefmt='rounded_grid'))
    elif(opcion ==2):
        codigoCliente = int(input("ingrese el codigo del cliente: "))

        print(tabulate(getOneClientCodigo(),headers="keys", tablefmt='rounded_grid'))
    elif(opcion == 3):