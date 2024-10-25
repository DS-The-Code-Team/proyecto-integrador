import time
import logging
logging.basicConfig(level=logging.INFO)

def cerrar_sesion_view():
    logging.info("Saliendo...")
    time.sleep(1)
    quit()