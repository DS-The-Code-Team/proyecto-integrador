import logging

""" 
    
    INSTRUCCIONES DE USO

    titulo = ""
    opciones = {
        n : ("descripcion", funcion),
        ...
    }

    menu_basico(titulo, opciones)

"""

def menu_basico_view(menu_titulo, menu_options):
    msg_error = f"Opción no válida\nPor favor intente de nuevo\n"

    print(menu_titulo)
    for key, value in menu_options.items():
        print(f"{key}: {value[0]}")
    print("")

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


        