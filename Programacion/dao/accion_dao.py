from dao.interface_dao import DataAccessDAO
from models.accion import Accion
from utils.db_conn import DBConn
import logging

class AccionDAO(DataAccessDAO):
    def __init__(self):
        self.db_conn = DBConn()
        self.connection = self.db_conn.connect_to_mysql()
    
    def get(self, id):
        try:
            with DBConn() as connection:
                cursor = connection.cursor()
                query = "SELECT * FROM acciones WHERE id_accion = %s"
                cursor.execute(query, (id,))
                result = cursor.fetchone()
                if result:
                    accion = Accion(*result)
                    return accion
                else:
                    return None
        except Exception as e:
            logging.error(f"Error al buscar la acción n° {id}: {e}")
            return None
        finally:
            if cursor:
                cursor.close()

    
    def get_all(self):
        try:
            with DBConn() as connection:  
                cursor = connection.cursor()
                query = "SELECT * FROM acciones"
                cursor.execute(query)
                results = cursor.fetchall()
                acciones = [Accion(*result) for result in results] 
                return acciones
        except Exception as e:
            logging.error(f"Error al buscar las acciones: {e}")
            return None
        finally:
            if cursor:
                cursor.close()



 
    def create(self, object):
        pass

   
    def update(self, object):
        pass

 
    def delete(self, object):
        pass
    

    def get_precios_de_acciones(self):
        cursor = None  
        try:
            with DBConn() as connection:
                cursor = connection.cursor()  
                cursor.execute(""" 
                    SELECT a.id_accion, a.nombre_accion, c.precio_compra
                    FROM acciones a
                    JOIN cotizacion c ON a.id_cotizacion = c.id_cotizacion
                """)
                return cursor.fetchall()  
        except Exception as e:
            logging.error(f"Error al obtener precios de acciones: {e}")
            return []
        finally:
            if cursor: 
                cursor.close()

    
    def get_acciones_portafolio(self, id_usuario):
        with DBConn() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT a.id_accion, a.nombre_accion, p.cantidad_acciones 
                    FROM portafolio p 
                    JOIN acciones a ON p.id_accion = a.id_accion 
                    WHERE p.id_usuario = %s
                """, (id_usuario,))
                return cursor.fetchall()  

        
