import storage.oficina as of

def getAllCodigoCiudad():
    codigoCiudad = []
    for val in of.oficina:
        codigoCiudad.append({
            "codigo:oficina": val.get("ciudad")
        })
        return codigoCiudad