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
            query = f"INSERT INTO {self.db_conn.get_database_name()}.usuarios (nombre, apellido, cuil, correo, contraseña, pin, saldo) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            data = (inversor.nombre, inversor.apellido, inversor.cuil, inversor.correo, inversor.contraseña, inversor.pin, inversor.saldo)
            cursor.execute(query, data)
            self.connection.commit()
            logging.info(f"Inversor {inversor.nombre} {inversor.apellido} registrado con exito. Bienvenido a ARGBroker")
        except Exception as e:
            logging.error(f"Error al registrar inversor: {e}")
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
     








# import logging
# from models.inversor import Inversor
# from config import get_db_connection

# def registrar_inversor(nombre, apellido, cuil, email, contraseña, pin):
#     inversor = Inversor(nombre, apellido, cuil, email, contraseña, pin)
#     connection = get_db_connection()
#     if connection:
#         try:
#             cursor = connection.cursor()
#             cursor.execute("""
#                 INSERT INTO usuarios (cuil, nombre, apellido, correo, contraseña, pin, saldo)
#                 VALUES (%s, %s, %s, %s, %s, %s, %s)
#             """, (inversor.cuil, inversor.nombre, inversor.apellido, inversor.email, inversor.contraseña, inversor.pin, inversor.saldo))
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
#                     contraseña='', 
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

