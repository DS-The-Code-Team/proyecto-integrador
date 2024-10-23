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

def menu_basico(menu_titulo, menu_options):
    msg_error = f"Opción no válida seleccionada\nPor favor intente de nuevo\n"

    print(menu_titulo)
    for key, value in menu_options.items():
        print(f"{key}: {value[0]}")

    while True:
        opcion = input("Ingrese una opción: ").strip()
        if opcion.isdigit():
            break
        else:
            logging.warning(msg_error)

    if opcion in menu_options:
        descripcion, funcion = menu_options[opcion]
        logging.info(f"Opción {opcion} seleccionada: {descripcion}")
        if funcion:
            funcion()
    else:
        logging.warning(msg_error)

def mostrar_menu():

    """ 
    
    INSTRUCCIONES DE USO

    titulo = "algo"
    opciones = {
        1 : ("descripcion", funcion),
        ...
    }

    menu_basico(titulo, opciones)

    """
    
    menu_principal_title = "Menú principal"
    menu_principal_opciones = {
        "1": ("Registrar inversor", registrar_inversor_view),
        "2": ("Listar inversores", listar_inversores_view),
        "3": ("Login inversor", login_inversor_view),
        "4": ("Salir", exit_view)
    }

    menu_basico(menu_principal_title, menu_principal_opciones)
    


# Ejecución del menú o las vistas 
while True:
    mostrar_menu()


       

     