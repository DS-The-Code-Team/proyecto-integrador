from dao.interface_dao import DataAccessDAO
from utils.db_conn import DBConn
from models.transaccion import Transaccion
import logging  

class TransaccionDAO(DataAccessDAO):
    def __init__(self):
        self.db_conn = DBConn() 

    
    def get(self, id: int):
        pass

 
    def get_all(self):
        pass


    def create(self, object):
        pass


    def update(self, object):
        pass

    def delete(self, object):
        pass
    
 
    def comprar_accion(self, id_usuario, id_accion, cantidad):
        try:
            with DBConn() as connection:
                with connection.cursor() as cursor:
                    # Obtener saldo del usuario
                    cursor.execute("SELECT saldo FROM usuarios WHERE id_usuario = %s", (id_usuario,))
                    saldo_actual = cursor.fetchone()
                    if saldo_actual is None:
                        raise ValueError("El usuario no tiene un saldo disponible.")
                    saldo_actual = saldo_actual[0]

                    # Obtener comision del broker
                    cursor.execute("SELECT broker_comision FROM transacciones")
                    result = cursor.fetchall()  # Asegúrate de consumir todos los resultados
                    comision_broker = result[0][0] if result else 0.015  # Comision 1.5%

                    # Obtener el precio de compra de la acción
                    cursor.execute("""
                        SELECT c.precio_compra, a.id_cotizacion 
                        FROM acciones a 
                        JOIN cotizacion c ON a.id_cotizacion = c.id_cotizacion 
                        WHERE a.id_accion = %s
                    """, (id_accion,))
                    precio_result = cursor.fetchone()
                    if precio_result is None:
                        raise ValueError("No se encontró la cotización para la acción solicitada.")
                    precio_compra, id_cotizacion = precio_result

                    # Calcular el total de la operación y verificar el saldo
                    total_operacion = precio_compra * cantidad
                    comision = total_operacion * comision_broker  # 1.5%
                    costo_total = total_operacion + comision

                    if saldo_actual < costo_total:
                        logging.warning("Saldo insuficiente para hacer la compra.")
                        return False  # Saldo insuficiente

                    # Registrar la transacción en la tabla transacciones
                    query_transaccion = """
                        INSERT INTO transacciones 
                        (id_usuario, id_accion, id_cotizacion, tipo_operacion, cantidad, precio_unitario, total_operacion, broker_comision) 
                        VALUES (%s, %s, %s, 'compra', %s, %s, %s, %s)
                    """
                    cursor.execute(query_transaccion, (id_usuario, id_accion, id_cotizacion, cantidad, precio_compra, costo_total, comision))

                    # Actualizar saldo del usuario
                    nuevo_saldo = saldo_actual - costo_total
                    cursor.execute("UPDATE usuarios SET saldo = %s WHERE id_usuario = %s", (nuevo_saldo, id_usuario))

                    # Actualizar o agregar la acción al portafolio del usuario
                    cursor.execute("SELECT cantidad_acciones FROM portafolio WHERE id_usuario = %s AND id_accion = %s", (id_usuario, id_accion))
                    portafolio_result = cursor.fetchone()

                    if portafolio_result:
                        cantidad_actual = portafolio_result[0]
                        nueva_cantidad = cantidad_actual + cantidad
                        cursor.execute("UPDATE portafolio SET cantidad_acciones = %s WHERE id_usuario = %s AND id_accion = %s", (nueva_cantidad, id_usuario, id_accion))
                    else:
                        cursor.execute("""
                            INSERT INTO portafolio (id_usuario, id_accion, cantidad_acciones, valor_comprometido, rendimiento_operacion) 
                            VALUES (%s, %s, %s, %s, %s)
                        """, (id_usuario, id_accion, cantidad, costo_total, 0.0))

                    # Confirmar transacción
                    connection.commit()
                    logging.info("Compra de acción realizada con éxito.")
                    return True

        except Exception as e:
            logging.error(f"Error al realizar la compra de acción: {e}")
            return False





    
    def vender_accion(self, id_usuario, id_accion, cantidad):
        try:
            with DBConn() as connection:
                with connection.cursor() as cursor:
                    # Obtener la cantidad de acciones en el portafolio del usuario
                    cursor.execute("SELECT cantidad_acciones FROM portafolio WHERE id_usuario = %s AND id_accion = %s", (id_usuario, id_accion))
                    portafolio_result = cursor.fetchone()

                    if portafolio_result is None:
                        logging.warning("No se encontraron acciones en el portafolio para vender.")
                        return False  # No hay acciones para vender
                    
                    cantidad_actual = portafolio_result[0]
                    if cantidad > cantidad_actual:
                        logging.warning("No se puede vender más acciones de las que posee.")
                        return False  # No tiene suficientes acciones

                   # Obtener el precio de venta de la acción
                    cursor.execute(""" 
                        SELECT c.precio_venta, a.id_cotizacion 
                        FROM acciones a 
                        JOIN cotizacion c ON a.id_cotizacion = c.id_cotizacion 
                        WHERE a.id_accion = %s
                    """, (id_accion,))
                    precio_result = cursor.fetchone()
                    if precio_result is None:
                        raise ValueError("No se encontró la cotización para la acción solicitada")
                    precio_venta, id_cotizacion = precio_result

                    # Convertir precio_venta a float
                    precio_venta_float = float(precio_venta)  # Convertimos a float

                    # Calcular el total de la operación
                    total_operacion = precio_venta_float * cantidad  # Ahora ambos son float
                    comision_broker = 0.015  # Suponiendo una comisión fija del 1.5%
                    comision = total_operacion * comision_broker
                    ingreso_total = total_operacion - comision

                    # Registrar la transacción en la tabla transacciones
                    query_transaccion = """
                        INSERT INTO transacciones 
                        (id_usuario, id_accion, id_cotizacion, tipo_operacion, cantidad, precio_unitario, total_operacion, broker_comision) 
                        VALUES (%s, %s, %s, 'venta', %s, %s, %s, %s)
                    """
                    cursor.execute(query_transaccion, (id_usuario, id_accion, id_cotizacion, cantidad, precio_venta, ingreso_total, comision))

                    # Actualizar o disminuir la cantidad de acciones en el portafolio del usuario
                    nueva_cantidad = cantidad_actual - cantidad
                    if nueva_cantidad > 0:
                        cursor.execute("UPDATE portafolio SET cantidad_acciones = %s WHERE id_usuario = %s AND id_accion = %s", (nueva_cantidad, id_usuario, id_accion))
                    else:
                        # Si se venden todas las acciones, eliminar de la tabla portafolio
                        cursor.execute("DELETE FROM portafolio WHERE id_usuario = %s AND id_accion = %s", (id_usuario, id_accion))

                    # Actualizar el saldo del usuario con el ingreso total
                    cursor.execute("UPDATE usuarios SET saldo = saldo + %s WHERE id_usuario = %s", (ingreso_total, id_usuario))

                    # Confirmar transacción
                    connection.commit()
                    logging.info("Venta de acción realizada con éxito.")
                    return True

        except Exception as e:
            logging.error(f"Error al realizar la venta de acción: {e}")
            return False




