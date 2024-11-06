from dao.interface_dao import DataAccessDAO
from models.accion import Accion
from utils.db_conn import DBConn

from utils.loggin_colors import log_error, log_info, log_warning
from utils.sql_query import Sql_Query


class AccionDAO(DataAccessDAO):
    def __init__(self, db_conn=None, sql_query=None):
        self.db_conn = db_conn or DBConn()
        self.sql_query = sql_query or Sql_Query(self.db_conn)
    
    def get(self, id):
        query = "SELECT * FROM acciones WHERE id_accion = %s"
                
        try:
            result = self.sql_query.get(query, (id,))
        
            if result:
                accion = Accion(*result)
                return accion
            else:
                return None
        except Exception as e:
            log_error(f"Error al buscar la acción n° {id}: {e}")
            return None
        
    
    def get_all(self):
        query = "SELECT * FROM acciones"
        try:
            results = self.sql_query.get_all(query)
            acciones = [Accion(*result) for result in results] 
            return acciones
        except Exception as e:
            log_error(f"Error al buscar las acciones: {e}")
            return None

 
    def create(self, object):
        pass

   
    def update(self, object):
        pass

 
    def delete(self, object):
        pass
    

    def get_precios_de_acciones(self):
        query = """  SELECT a.id_accion, a.nombre_accion, c.precio_compra, a.cantidad_mercado
                    FROM acciones a
                    JOIN cotizacion c ON a.id_cotizacion = c.id_cotizacion """
        try:
            data_acciones = self.sql_query.get_all(query)
            return data_acciones  
        except Exception as e:
            log_error(f"Error al obtener precios de acciones: {e}")
            return []
        
    
    def get_acciones_portafolio(self, id_usuario):
        query = """
                    SELECT a.id_accion, a.nombre_accion, p.cantidad_acciones 
                    FROM portafolio p 
                    JOIN acciones a ON p.id_accion = a.id_accion 
                    WHERE p.id_usuario = %s
                """
        try:
            data_acciones = self.sql_query.get_all(query, (id_usuario,))
            return data_acciones  
        except Exception as e:
            log_error(f"Error al obtener acciones: {e}")
            return []

        
