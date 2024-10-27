from dao.portafolio_dao import PortafolioDAO
from models.portafolio import Portafolio
from views.menu_basico_view import menu_basico_view
import os

def crear_portafolio():
    id_usuario = int(os.getenv("id_inversor"))
    print(f"Creando portafolio para el usuario con id: {id_usuario}")
    
    portafolio = Portafolio(id_usuario, None, 0, 0, 0)
    dao = PortafolioDAO()
    dao.create(portafolio)

def get_portafolio(id_usuario):
    dao = PortafolioDAO()
    portafolio = dao.get(id_usuario)
    return portafolio


def portafolio_view():
    id_usuario = int(os.getenv("id_inversor"))

    portafolio = get_portafolio(id_usuario)
    if portafolio:
        print(f"""
        Portafolio:{portafolio}
        """)
    else:
        portafolio = crear_portafolio()
        print("Portafolio creado con éxito.")
        portafolio = get_portafolio(id_usuario)
        print(f"""
        Portafolio:{portafolio}
        """)
    