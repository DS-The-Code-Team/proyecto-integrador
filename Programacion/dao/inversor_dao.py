from dao.interface_dao import DataAccessDAO
from models.inversor import Inversor
from utils.db_conn import DBConn
import logging

class InversorDAO(DataAccessDAO):
    def __init__(self):
        self.db_conn = DBConn()
        self.connection = self.db_conn.connect_to_mysql()

    def create(self, inversor):
        try:
            with DBConn() as connection:  # Aquí se usa `with` para abrir y cerrar la conexión automáticamente
                cursor = connection.cursor()
                query = f"INSERT INTO {self.db_conn.get_database_name()}.usuarios (nombre, apellido, cuil, correo, contrasena, pin, saldo) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                data = (inversor.nombre, inversor.apellido, inversor.cuil, inversor.correo, inversor.contrasena, inversor.pin, inversor.saldo)
                cursor.execute(query, data)
                connection.commit()
                logging.info(f"Inversor {inversor.nombre} {inversor.apellido} registrado con éxito.")
        except Exception as e:
            logging.error(f"Error al registrar inversor: {e}")
        finally:
            cursor.close()  # Aunque la conexión se cierra automáticamente, cerramos el cursor manualmente
           
            

    def get(self, id):
        # Implementación para obtener un inversor por ID
        pass

    def get_all(self):
        try:
            with DBConn() as connection:  # Con `with` para manejar la conexión
                cursor = connection.cursor()
                query = f"""
                    SELECT id_usuario, cuil, nombre, apellido, correo, contrasena, pin, saldo, fecha_registro 
                    FROM {self.db_conn.get_database_name()}.usuarios
                    """
                cursor.execute(query)
                results = cursor.fetchall()
                inversores = [
                    Inversor(
                        nombre=result[2], 
                        apellido=result[3], 
                        cuil=result[1], 
                        correo=result[4], 
                        contrasena=result[5], 
                        pin=result[6], 
                        saldo=result[7], 
                        id_usuario=result[0], 
                        fecha_registro=result[8]
                     )    
                    for result in results
                ]
                return inversores
        except Exception as e:
            logging.error(f"Error al listar inversores: {e}")
        finally:
            cursor.close()



              

    def update(self, inversor):
        # Implementación para actualizar un inversor
        pass

    def delete(self, inversor):
        # Implementación para eliminar un inversor
        pass


    """  Método login exclusivo de clase InversorDAO """
    def login(self, correo, contrasena):
        try:
            cursor = self.connection.cursor()
            query = f"SELECT nombre, apellido, cuil, correo, contrasena, pin, saldo FROM {self.db_conn.get_database_name()}.usuarios WHERE correo = %s AND contrasena = %s"

            cursor.execute(query, (correo, contrasena))
            result = cursor.fetchone()
            if result:
                inversor = Inversor(*result)
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
               
     














# Metodos sin with:

#  def create(self, inversor):
#         try:
#             cursor = self.connection.cursor()
#             query = f"INSERT INTO {self.db_conn.get_database_name()}.usuarios (nombre, apellido, cuil, correo, contrasena, pin, saldo) VALUES (%s, %s, %s, %s, %s, %s, %s)"
#             data = (inversor.nombre, inversor.apellido, inversor.cuil, inversor.correo, inversor.contrasena, inversor.pin, inversor.saldo)
#             cursor.execute(query, data)
#             self.connection.commit()
            
#             # retorna el id asignado al usuario
#             inversor.id = cursor.lastrowid
#             logging.info(f"Hola {inversor.nombre} {inversor.apellido} fuiste registrado con éxito en ARGBroker")
            
#             logging.info(f"Datos de control (borrar esta línea antes de la entrega) \nID: {inversor.id}, \n CUIL: {inversor.cuil}, \n Correo: {inversor.correo}, \n contrasena: {inversor.contrasena}, \n Saldo: {inversor.saldo}")
            
#         except Exception as e:
#             logging.error(f"No se pudo realizar el registro. Error de: {e}")
#         finally:
#             cursor.close()

#   def create(self, inversor):
#         try:
#             cursor = self.connection.cursor()
#             query = f"INSERT INTO {self.db_conn.get_database_name()}.usuarios (nombre, apellido, cuil, correo, contrasena, pin, saldo) VALUES (%s, %s, %s, %s, %s, %s, %s)"
#             data = (inversor.nombre, inversor.apellido, inversor.cuil, inversor.correo, inversor.contrasena, inversor.pin, inversor.saldo)
#             cursor.execute(query, data)
#             self.connection.commit()
            
#             # retorna el id asignado al usuario
#             inversor.id = cursor.lastrowid
#             logging.info(f"Hola {inversor.nombre} {inversor.apellido} fuiste registrado con éxito en ARGBroker")
            
#             logging.info(f"Datos de control (borrar esta línea antes de la entrega) \nID: {inversor.id}, \n CUIL: {inversor.cuil}, \n Correo: {inversor.correo}, \n contrasena: {inversor.contrasena}, \n Saldo: {inversor.saldo}")
            
#         except Exception as e:
#             logging.error(f"No se pudo realizar el registro. Error de: {e}")
#         finally:
#             cursor.close()           
            






