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
            cursor = self.connection.cursor()
            query = f"INSERT INTO {self.db_conn.get_database_name()}.usuarios (nombre, apellido, cuil, correo, contrasena, pin, saldo) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            data = (inversor.nombre, inversor.apellido, inversor.cuil, inversor.correo, inversor.contrasena, inversor.pin, inversor.saldo)
            cursor.execute(query, data)
            self.connection.commit()
            
            # retorna el id asignado al usuario
            inversor.id = cursor.lastrowid
            logging.info(f"Hola {inversor.nombre} {inversor.apellido} fuiste registrado con éxito en ARGBroker")
            
            logging.info(f"Datos de control (borrar esta línea antes de la entrega) \nID: {inversor.id}, \n CUIL: {inversor.cuil}, \n Correo: {inversor.correo}, \n contrasena: {inversor.contrasena}, \n Saldo: {inversor.saldo}")
            
        except Exception as e:
            logging.error(f"No se pudo realizar el registro. Error de: {e}")
        finally:
            cursor.close()

    def get(self, id):
        # Implementación para obtener un inversor por ID
        pass

    def get_all(self):
        try:
            cursor = self.connection.cursor()
            query = f"SELECT * FROM {self.db_conn.get_database_name()}.usuarios"
            cursor.execute(query)
            results = cursor.fetchall()
            inversores = [Inversor(*result) for result in results]
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
     








# import logging
# from models.inversor import Inversor
# from config import get_db_connection

# def registrar_inversor(nombre, apellido, cuil, email, contrasena, pin):
#     inversor = Inversor(nombre, apellido, cuil, email, contrasena, pin)
#     connection = get_db_connection()
#     if connection:
#         try:
#             cursor = connection.cursor()
#             cursor.execute("""
#                 INSERT INTO usuarios (cuil, nombre, apellido, correo, contrasena, pin, saldo)
#                 VALUES (%s, %s, %s, %s, %s, %s, %s)
#             """, (inversor.cuil, inversor.nombre, inversor.apellido, inversor.email, inversor.contrasena, inversor.pin, inversor.saldo))
#             connection.commit()
#             logging.info("Inversor registrado exitosamente")
#             return True
#         except Exception as e:
#             logging.error(f"Error al registrar el inversor: {e}")
#             connection.rollback()
#             return False
#         finally:
#             cursor.close()
#             connection.close()
#     else:
#         logging.error("No se pudo conectar a la base de datos para registrar el inversor.")
#         return False

# def listar_inversores():
#     connection = get_db_connection()
#     inversores = []
#     if connection:
#         try:
#             cursor = connection.cursor(dictionary=True)
#             cursor.execute("SELECT cuil, nombre, apellido, correo, saldo FROM usuarios")
#             rows = cursor.fetchall()
#             for row in rows:
#                 inversor = Inversor(
#                     nombre=row['nombre'], 
#                     apellido=row['apellido'], 
#                     cuil=row['cuil'], 
#                     email=row['correo'], 
#                     contrasena='', 
#                     pin=0, 
#                     saldo=row['saldo']
#                 )
#                 inversores.append(inversor)
#         except Exception as e:
#             logging.error(f"Error al listar los inversores: {e}")
#         finally:
#             cursor.close()
#             connection.close()
#     else:
#         logging.error("No se pudo conectar a la base de datos para listar los inversores.")
#     return inversores

