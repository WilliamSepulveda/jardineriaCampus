import storage.producto as pro


# devuelve un listado con todos ls productos que pertenecen a la gama ornamentales 
# y que tienen mas de 180 unidades en stock, el listado debera esatr ordenasdo por su precio de ventas 
# mostrando en primer lugar los de mayor precio

def getAllStockPriceGama(gama, stock):
    condicciones =[]
    for val in pro.producto:
        if(val.get("gama") == gama and val.get("precio_venta") >= stock):
            condicciones.append(val)

    def precio(val):
        return val.get("precio_venta")
    condicciones.sort(key=precio)

    return condicciones