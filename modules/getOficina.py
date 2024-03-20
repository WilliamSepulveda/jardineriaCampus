# Devuelve un listado con el código de oficina y la ciudad donde hay oficinas.
from modules.crudOficina import getAllDataOficina
import modules.Validaciones as val 
import os 
from  tabulate import tabulate 
import requests


def getAllDataOficina():
    #json-server storage/oficina.json -b 5505
    peticion = requests.get("http://localhost:5504/oficinas")
    data = peticion.json()
    return data 


def getAllCodigoCiudad():
    codigoCiudad = list()
    for val in getAllDataOficina():
        codigoCiudad.append({
            "codigo_oficina": val.get("codigo_oficina"),
            "ciudad": val.get("ciudad")
        })
    return codigoCiudad


#devuelve un listado con la ciudad y el telefono
#de las oficinas

def getAllCiudadTelefono(pais):
    ciudadTelefono = list()
    for val in getAllDataOficina():
        if(val.get("pais") == pais):
            ciudadTelefono.append({
                "ciudad": val.get("ciudad"),
                "telefono": val.get("telefono"),
                "oficina": val.get("codigooficina"),
                "pais": val.get("pais")
            })
    return ciudadTelefono

def menu():
    while True:
        os.system("clear")
        print(""" 


██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗███████╗    ██████╗ ███████╗     ██████╗ ███████╗██╗ ██████╗██╗███╗   ██╗ █████╗ 
██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝    ██╔══██╗██╔════╝    ██╔═══██╗██╔════╝██║██╔════╝██║████╗  ██║██╔══██╗
██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   █████╗      ██║  ██║█████╗      ██║   ██║█████╗  ██║██║     ██║██╔██╗ ██║███████║
██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   ██╔══╝      ██║  ██║██╔══╝      ██║   ██║██╔══╝  ██║██║     ██║██║╚██╗██║██╔══██║
██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   ███████╗    ██████╔╝███████╗    ╚██████╔╝██║     ██║╚██████╗██║██║ ╚████║██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝    ╚═════╝ ╚══════╝     ╚═════╝ ╚═╝     ╚═╝ ╚═════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
                                                                                                                                                                                               
        0. regresar al menu anterior   
        1. obtener una lista de las oficinas que hay en una ciudad  (codigo, oficina, ciudad)
        2. obtener los contactos de todas las oficinas del pais especifico.         

""")
        opcion = input("\n seleccione una de las opciones: ")
        if(val.validacionesOpciones(opcion) is not None):
            opcion = int(opcion)
            if(opcion >= 0 and opcion <= 2):
                if (opcion == 1):
                    print(tabulate(getAllCodigoCiudad(), headers="keys", tablefmt="founded_grid"))
                elif (opcion == 2):
                    pais = input("ingrese el pais que desea que filtremos: ")
                    input(tabulate(getAllCiudadTelefono(pais), headers="keys", tablefmt="rounded_grid")) 
                    
                elif ( opcion == 0):
                    break
                

