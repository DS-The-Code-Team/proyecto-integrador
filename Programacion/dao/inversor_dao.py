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
        # Implementación para obtener un inversor por ID
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


    """  Métodos exclusivos de clase InversorDAO """
    
    def get_login(self, correo, contrasena):
        try:
            with DBConn() as connection: 
                cursor = connection.cursor()
                query = f"SELECT id_usuario, nombre, apellido, cuil, correo, contrasena, pin, saldo FROM {self.db_conn.get_database_name()}.usuarios WHERE correo = %s AND contrasena = %s"
                cursor.execute(query, (correo, contrasena))
                result = cursor.fetchone()
                logging.info(f"Resultado de la consulta de inicio de sesión: {result}")
                if result:
                    inversor = Inversor(*result)
                    logging.info(f"Inversor {inversor.nombre} ha iniciado sesión con éxito.")
                    return inversor
                else:
                    logging.warning(f"Intento de inicio de sesión fallido para el correo: {correo}")
                    return None
        except Exception as e:
            logging.error(f"Error al intentar iniciar sesión: {e}")
            return None


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

    
    #Metodo para mostrar resumen del inversor que inicio sesión
    def obtener_datos_cuenta(self, inversor):
        try:
            with DBConn() as connection:  
                cursor = connection.cursor()
                # Consulta para obtener el saldo del usuario y otros datos del portafolio
                query = """
                SELECT u.saldo, p.valor_comprometido, p.rendimiento_operacion
                FROM usuarios u
                LEFT JOIN portafolio p ON u.id_usuario = p.id_usuario
                WHERE u.id_usuario = %s
                """
                cursor.execute(query, (inversor,))
                result = cursor.fetchone()
                if result:
                    # Procesa y devuelve los datos necesarios
                    saldo, valor_comprometido, rendimiento_operacion = result
                    return saldo, valor_comprometido, rendimiento_operacion
                else:
                    logging.warning(f"No se encontraron datos para el inversor {inversor}.")
                    return None, None, None
        except Exception as e:
            logging.error(f"Error al obtener datos de la cuenta del inversor {inversor}: {e}")
            return None, None, None
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
            






