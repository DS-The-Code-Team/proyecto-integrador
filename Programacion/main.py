from dao.inversor_dao import InversorDAO
from models.inversor import Inversor
import logging

logging.basicConfig(level=logging.INFO)

#Consola, vistas:   

def registrar_inversor_view():
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    cuil = input("Ingrese CUIL: ")
    correo = input("Ingrese email: ")
    contrasena = input("Ingrese contraseña: ")
    pin = input("Ingrese pin: ")
    saldo = 1000000.00

    inversor = Inversor(nombre, apellido, cuil, correo, contrasena, pin, saldo)
    dao = InversorDAO()
    dao.create(inversor)
  

def listar_inversores_view():
    dao = InversorDAO()
    inversores = dao.get_all()
    for inversor in inversores:
        print(inversor)

# Ejecución del menú o las vistas

registrar_inversor_view()
