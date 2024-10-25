from dao.inversor_dao import InversorDAO
from models.inversor import Inversor
import logging

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

def login_inversor_view():
    dao = InversorDAO()
    correo = input("Ingrese su correo: ")
    contrasena = input("Ingrese su contraseña: ")
    dao.login(correo, contrasena)
