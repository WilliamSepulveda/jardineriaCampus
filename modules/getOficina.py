# Devuelve un listado con el código de oficina y la ciudad donde hay oficinas.
import storage.oficina as of 

def getAllCodigoCiudad():
    codigoCiudad = []
    for val in of.oficina:
        codigoCiudad.append({
            "codigo_oficina" :val.get("codigo_oficina"),
            "ciudad" :val.get("ciudad")
        })
    return codigoCiudad


#devuelve un listado con la ciudad y el telefono
#de las oficinas

def getAllCiudadTelefono(pais):
    ciudadTelefono = []
    for val in of.oficina:
        if(val.get("pais")==pais):

            ciudadTelefono.append({
                "ciudad" : val.get("ciudad"),
                "telefono" : val.get("telefono"),
                "oficina" : val.get("codigooficina"),
                "pais" : val.get("pais")
            })
    return ciudadTelefono

def menu():
    print(""" 

███╗   ███╗███████╗███╗   ██╗██╗   ██╗     ██████╗ ███████╗██╗ ██████╗██╗███╗   ██╗ █████╗     
████╗ ████║██╔════╝████╗  ██║██║   ██║    ██╔═══██╗██╔════╝██║██╔════╝██║████╗  ██║██╔══██╗    
██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║    ██║   ██║█████╗  ██║██║     ██║██╔██╗ ██║███████║    
██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║    ██║   ██║██╔══╝  ██║██║     ██║██║╚██╗██║██╔══██║    
██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝    ╚██████╔╝██║     ██║╚██████╗██║██║ ╚████║██║  ██║    
╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝      ╚═════╝ ╚═╝     ╚═╝ ╚═════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝    
                                                                                               

                                                                    
            1. La ciudad de una oficina (codifo, oficina, ciudad)
            2. la ciudad y el telefono de cada oficina segun el pais           

""")
   