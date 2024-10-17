#Este archivo gestiona la conexión a la base de datos utilizando mysql.connector y los datos de configuración almacenados en config.ini. Está diseñado para ser reutilizable, y es aquí donde se lee el archivo config.ini para obtener la información de conexión.

import mysql.connector
from mysql.connector import errorcode
import configparser
import pathlib

class DBConn:
    def __init__(self, config_file="config.ini"):
        self.config_file = config_file

        if self.config_file:
            config = configparser.ConfigParser()
            config_path = pathlib.Path(__file__).parent.parent / config_file
            config.read(config_path)
            self.db_config = config['database']
    
    def get_database_name(self):
        return self.db_config.get('database')

    def connect_to_mysql(self):
        try: 
            return mysql.connector.connect(
                user=self.db_config.get('user'),
                password=self.db_config.get('password'),
                host=self.db_config.get('host'),
            )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise ValueError("Usuario o Password no válido")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                raise ValueError("La base de datos no existe.")
            else:
                raise(err)
        return None
