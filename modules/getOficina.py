# Devuelve un listado con el código de oficina y la ciudad donde hay oficinas.

import storage.oficina as of

def getAllCodigoCiudad():
    codigoCiudad = []
    for val in of.oficina:
        codigoCiudad.append({
            "codigo_oficina": val.get("codigo_oficina"),
            "codigo_ciudad": val.get("ciudad")
        })
    return codigoCiudad