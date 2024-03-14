import os
from tabulate import tabulate
import json
import modules.getgamas as gG
import requests

def postproducto():
    # json-server storage/producto.json -b 5501
    producto = {
        "codigo_producto": input("Ingrese el codigo del producto: "),
        "nombre": input ("Ingrese el nombre del producto: "),
        "gama": input("Ingrse la gama del producto: "),
        "dimensiones": input("Ingrse la dimensiones del producto: "),
        "proveedor": input("Ingrse el proveedor del producto: "),
        "descripcion": input("Ingrse el descripcion del producto: "),
        "cant#idad_en_stock": float(input("Ingrse el cantidad en stock: ")),
        "precio_venta": float(input("Ingrse el precio de ventas: ")),
        "precio_proveedor": float(input("Ingrse el precio del proveedor: "))
        }    
    #json-server storage/producto.json -b 5501
    peticion = requests.post("http://172.16.102.108.5501")
    data = peticion.json()
    return json