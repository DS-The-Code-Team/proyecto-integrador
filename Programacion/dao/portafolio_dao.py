from dao.interface_dao import DataAccessDAO
from models.portafolio import Portafolio
from utils.db_conn import DBConn
import logging

class PortafolioDAO(DataAccessDAO):
    def __init__(self):
        self.db_conn = DBConn()
        self.connection = self.db_conn.connect_to_mysql()
    
    def get(self, id):
        try:
            with DBConn() as connection:
                cursor = connection.cursor()
                query = "SELECT * FROM portafolio WHERE id_usuario = %s"
                cursor.execute(query, (id,))
                result = cursor.fetchone()
                if result:
                    portafolio = Portafolio(*result)
                    return portafolio
                else:
                    return None
        except Exception as e:
            logging.error(f"Error: {e}")
            return None
        finally:
            cursor.close()

    
    def get_all(self):
        pass

 
    def create(self, portafolio):
        try:
            with DBConn() as connection:  
                cursor = connection.cursor()
                query = f"INSERT INTO {self.db_conn.get_database_name()}.portafolio (id_usuario, id_accion, cantidad_acciones, valor_comprometido, rendimiento_operacion) VALUES (%s, %s, %s, %s, %s)"
                data = (portafolio.id_usuario, portafolio.id_accion, portafolio.cantidad_acciones, portafolio.valor_comprometido, portafolio.rendimiento_operacion)
                cursor.execute(query, data)
                connection.commit()
                logging.info(f"Potafolio creado con éxito.")
        except Exception as e:
            logging.error(f"Error al crear portafolio: {e}")
        finally:
            cursor.close()


   
    def update(self, portafolio):
        try:
            with DBConn() as connection:  
                cursor = connection.cursor()
                data = (
                        portafolio.id_portafolio,
                        portafolio.id_usuario,
                        portafolio.id_accion,
                        portafolio.cantidad_acciones,
                        portafolio.valor_comprometido,
                        portafolio.rendimiento_operacion
                    )
                query = f"""
                    UPDATE {self.db_conn.get_database_name()}.portafolio 
                    SET id_accion = %s, cantidad_acciones = %s, valor_comprometido = %s, rendimiento_operacion = %s
                    WHERE id_usuario = %s AND id_portafolio = %s
                """
                cursor.execute(query, (data,))
                connection.commit()
                logging.info(f"Datos actualizados")
        except Exception as e:
            logging.error(f"Error al intentar actualizar los datos: {e}")
        finally:
            cursor.close() 


    def delete(self, object):
        pass