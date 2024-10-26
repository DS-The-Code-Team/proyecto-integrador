from dao.interface_dao import DataAccessDAO
from models.inversor import Inversor
from utils.db_conn import DBConn
import logging

class InversorDAO(DataAccessDAO):
    def __init__(self):
        self.db_conn = DBConn()
        self.connection = self.db_conn.connect_to_mysql()
    

    def _map_result_to_inversor(self, result):
        return Inversor(
                        id_usuario=result[0],
                        nombre=result[1],
                        apellido=result[2],
                        cuil=result[3],
                        correo=result[4],
                        contrasena=result[5],
                        pin=result[6],
                        saldo=result[7],
                        fecha_registro=result[8]
                   )


    def create(self, inversor):
        try:
            with DBConn() as connection:  
                cursor = connection.cursor()
                query = f"INSERT INTO {self.db_conn.get_database_name()}.usuarios (nombre, apellido, cuil, correo, contrasena, pin, saldo) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                data = (inversor.nombre, inversor.apellido, inversor.cuil, inversor.correo, inversor.contrasena, inversor.pin, inversor.saldo)
                cursor.execute(query, data)
                connection.commit()
                logging.info(f"Inversor {inversor.nombre} {inversor.apellido} registrado con éxito.")
        except Exception as e:
            logging.error(f"Error al registrar inversor: {e}")
        finally:
            cursor.close() 
           
            

    def get(self, id):
        pass


    def get_all(self):
        try:
            with DBConn() as connection:  
                cursor = connection.cursor()
                query = f"""
                    SELECT id_usuario, cuil, nombre, apellido, correo, contrasena, pin, saldo, fecha_registro 
                    FROM {self.db_conn.get_database_name()}.usuarios
                    """
                cursor.execute(query)
                results = cursor.fetchall()
                inversores = [
                    """ Inversor(
                        nombre=result[2], 
                        apellido=result[3], 
                        cuil=result[1], 
                        correo=result[4], 
                        contrasena=result[5], 
                        pin=result[6], 
                        saldo=result[7], 
                        id_usuario=result[0], 
                        fecha_registro=result[8]
                     )     """

                    self._map_result_to_inversor(result)
                    for result in results
                ]
                return inversores
        except Exception as e:
            logging.error(f"Error al listar inversores: {e}")
        finally:
            cursor.close()
            

    def update(self, inversor):
        try:
            with DBConn() as connection:  
                cursor = connection.cursor()
                data = (
                    inversor.nombre, inversor.apellido, inversor.cuil, inversor.correo,
                    inversor.contrasena, inversor.pin, inversor.saldo,
                    inversor.id_usuario
                )
                query = f"""
                    UPDATE {self.db_conn.get_database_name()}.usuarios 
                    SET nombre = %s, apellido = %s, cuil = %s, correo = %s, contrasena = %s, pin = %s
                    WHERE id_usuario = %s
                """
                cursor.execute(query, (data,))
                connection.commit()
                logging.info(f"Datos actualizados")
        except Exception as e:
            logging.error(f"Error al intentar actualizar los datos: {e}")
        finally:
            cursor.close() 


    def delete(self, inversor):
        try:
            with DBConn() as connection: 
                cursor = connection.cursor()
                query = f"DELETE FROM {self.db_conn.get_database_name()}.usuarios WHERE id_usuario = %s"
                cursor.execute(query, (inversor.id_usuario,))
                connection.commit()
                logging.info(f"Inversor {inversor.nombre} {inversor.apellido} eliminado con éxito.")
        except Exception as e:
            logging.error(f"Error al intentar iniciar sesión: {e}")
            return None
        finally:
            cursor.close() 


    """  Métodos exclusivos de clase InversorDAO """
    
    def get_login(self, correo, contrasena):
        try:
            with DBConn() as connection: 
                cursor = connection.cursor()
                query = f"SELECT id_usuario, nombre, apellido, cuil, correo, contrasena, pin, saldo, fecha_registro FROM {self.db_conn.get_database_name()}.usuarios WHERE correo = %s AND contrasena = %s"
                cursor.execute(query, (correo, contrasena))
                result = cursor.fetchone()
                print(result)
                if result:
                    inversor = self._map_result_to_inversor(result)
                    logging.info(f"Inversor {inversor.nombre} {inversor.apellido} ha iniciado sesión con éxito.")
                    return inversor
                else:
                    logging.warning(f"Intento de inicio de sesión fallido para el correo: {correo}")
                    return None
        except Exception as e:
            logging.error(f"Error al intentar iniciar sesión: {e}")
            return None
        finally:
            cursor.close() 


    def get_verificar_usuario(self, correo, pin):
        try:
            with DBConn() as connection:  
                cursor = connection.cursor()
                select_query = f"SELECT correo FROM {self.db_conn.get_database_name()}.usuarios WHERE correo = %s AND pin = %s"
                cursor.execute(select_query, (correo, pin))
                usuario_existe = cursor.fetchone()

                if not usuario_existe:
                    return False
                return True
        except Exception as e:
            logging.error(f"Error al verificar el usuario: {e}")
        finally:
            cursor.close() 


    def set_contrasena_nueva(self, correo, contrasena_nueva):
        try:
            with DBConn() as connection:  
                cursor = connection.cursor()
                query = f"UPDATE {self.db_conn.get_database_name()}.usuarios SET contrasena = %s WHERE correo = %s"
                cursor.execute(query, (contrasena_nueva, correo))
                connection.commit()
                logging.info(f"Contraseña de {correo} actualizada con éxito.")
        except Exception as e:
            logging.error(f"Error al intentar actualizar la contraseña: {e}")
        finally:
            cursor.close() 