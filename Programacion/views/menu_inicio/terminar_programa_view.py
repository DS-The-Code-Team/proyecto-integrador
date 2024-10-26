import time
import logging
logging.basicConfig(level=logging.INFO)

def terminar_programa_view():
    logging.info("Saliendo...")
    time.sleep(1)
    quit()