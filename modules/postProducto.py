import json
import requests

def postproducto(json):
    #json-server storage/producto.json -b 5501
    peticion = requests.post("http://172.16.102.108.5501")
    data = peticion.json()
    return json