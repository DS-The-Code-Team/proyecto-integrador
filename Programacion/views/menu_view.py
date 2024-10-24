import logging
import time
from views.inversor_view import registrar_inversor_view, listar_inversores_view, login_inversor_view

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
    menu_principal_title = "Menú principal"
    menu_principal_opciones = {
        "1": ("Registrar inversor", registrar_inversor_view),
        "2": ("Listar inversores", listar_inversores_view),
        "3": ("Login inversor", login_inversor_view),
        "4": ("Salir", exit_view)
    }

    menu_basico(menu_principal_title, menu_principal_opciones)