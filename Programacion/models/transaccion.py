class Transaccion:
    def __init__(self,
                id_transaccion:str,
                tipo:str,
                cantidad:float,
                precio_unit: float, 
                precio_total:float, 
                fecha:str,
                descripcion: str):
        self.id_transaccion = id_transaccion
        self.tipo = tipo
        self.cantidad = cantidad
        self.precio_unit = precio_unit
        self.fecha = fecha
        self.precio_total = precio_total
        self.descripcion = descripcion

    