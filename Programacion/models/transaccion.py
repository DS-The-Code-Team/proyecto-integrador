class Transaccion:
    def __init__(self, id_transaccion, id_usuario, id_accion, id_cotizacion, tipo_operacion, cantidad, precio_unitario, total_operacion, fecha_transaccion):
        self.id_transaccion = id_transaccion
        self.id_usuario = id_usuario
        self.id_accion = id_accion
        self.id_cotizacion = id_cotizacion
        self.tipo_operacion = tipo_operacion
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.total_operacion = total_operacion
        self.fecha_transaccion = fecha_transaccion
