import os
import time

def inversor_cerrar_sesion_view():
    os.environ["id_inversor"] = ""
    os.environ["nombre_inversor"] = ""
    os.environ["apellido_inversor"] = ""
    os.environ["saldo_inversor"] = ""
    os.environ["contrasena_inversor"] = ""
    print("Sesión cerrada con éxito, volviendo al menú de inicio...")
    time.sleep(1) 
    return None