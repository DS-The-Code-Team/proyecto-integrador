from dao.portafolio_dao import PortafolioDAO
from models.portafolio import Portafolio
from views.menu_basico_view import menu_basico_view
import os

def crear_portafolio():
    id_usuario = int(os.getenv("id_inversor"))
    print(f"Creando portafolio para el usuario con id: {id_usuario}")
    
    portafolio = Portafolio(id_usuario, 0, 0, 0, 0)
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
              Portafolio: {portafolio.id_portafolio}
              Usuario: {portafolio.id_usuario}
              Acciones: {portafolio.id_accion}
              Cantidad total: {portafolio.cantidad_acciones}
              Valor comprometido: {portafolio.valor_comprometido}
              Rendimiento de las operaciones: {portafolio.rendimiento_operacion}
        """)
    else:
        portafolio = crear_portafolio()       
        portafolio = get_portafolio(id_usuario)
        print(f"""
        Portafolio:{portafolio}
        """)
    