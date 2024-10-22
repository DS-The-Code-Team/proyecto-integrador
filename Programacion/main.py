from dao.inversor_dao import InversorDAO
from models.inversor import Inversor
import time
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


def login_inversor_view():
    dao = InversorDAO()
    correo = input("Ingrese su correo: ")
    contrasena = input("Ingrese su contraseña: ")
    dao.login(correo, contrasena)


def exit_view():
    logging.info("Saliendo...")
    time.sleep(1)
    quit()


def mostrar_menu():

    menu_options = {
        "1": ("Registrar inversor", registrar_inversor_view),
        "2": ("Listar inversores", listar_inversores_view),
        "3": ("Login inversor", login_inversor_view),
        "4": ("Salir", exit_view)
    }
    opcion = input("Ingrese una opción: ").strip('.-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')   
    logging.info(f"Opción ingresada: {opcion}")

    if opcion in menu_options:
        descripcion, funcion = menu_options[opcion]
        logging.info(f"Opción {opcion} seleccionada: {descripcion}")
        if funcion:
            funcion()
    else:
        logging.warning("Opción no válida seleccionada")
        print("Opción no válida, por favor intente de nuevo.")


# Ejecución del menú o las vistas 
while True:
    mostrar_menu()


       

     