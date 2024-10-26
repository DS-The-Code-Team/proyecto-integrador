from views.menu_basico_view import menu_basico_view

def transacciones_historial():
    print("Historial de transacciones")


def transacciones_view():
    submenu_title = "Menú Transacciones"
    submenu_opciones = {
        "1": ("Compra", None),
        "2": ("Venta", None),
        "3": ("Historial", transacciones_historial),
        "4": ("Volver al menú anterior", None),
    }

    menu_basico_view(submenu_title, submenu_opciones)