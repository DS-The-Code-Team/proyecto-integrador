from dao.portafolio_dao import PortafolioDAO
from models.portafolio import Portafolio
import os

def portafolio_view():
   
   
    id_usuario = os.getenv("id_inversor")
    portafolio = Portafolio(id_usuario, None, None, 0, 0, 0)  
    dao = PortafolioDAO()
    dao.create(portafolio)