import requests

def getAllGama():
    # json-server storage/gama_producto.json -b 5502
    peticion = requests.get("http://localhost:5503/gama")
    data = peticion.json()
    return data

def getAllNombre():
    gamaNombre = list()
    for val in getAllGama():
        gamaNombre.append(val.get("gama"))
    return gamaNombre 