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
            return{
                "codigo_cliente": val.get('codigo_cliente'),
                "nombre_cliente":val.get('nombre_cliente')
            }
        

        
def getAllClientCreditCiudad(limiteCredit,ciudad):
    clienteCredit =list()
    for val in cli.clientes:
        if(val.get('limite_credito') >= limiteCredit and val.get('ciudad') == ciudad):
            clienteCredit.append(val)
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
        clientZone = list()
        for val in cli.clientes:
            if(val.get('codigo_empleado' == codigo_empleado)):
                return{
                    "codigo_empleado_rep_ventas":val.get('codigo_empleado'),
                    "nombre_empleado":val.get('nombre_empleao')                   
                }
            





        clientZone.append(val)
        return clientZone 


     # val.get('pais') == pais and
        # (val.get('region') == region or val.get('region') ==None) or
        # (val.get('ciudad') == ciudad or val.get('ciudad') ==None) 
              