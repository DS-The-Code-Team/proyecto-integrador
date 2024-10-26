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
            cursor.close()

    
    def get_all(self):
        try:
            with DBConn() as connection:  
                cursor = connection.cursor()
                query = "SELECT * FROM acciones"
                cursor.execute(query)
                results = cursor.fetchall()
                acciones = Accion(*results)
                return acciones
        except Exception as e:
            logging.error(f"Error al buscar las acciones: {e}")
            return None
        finally:
            cursor.close()


 
    def create(self, object):
        pass

   
    def update(self, object):
        pass

 
    def delete(self, object):
        pass