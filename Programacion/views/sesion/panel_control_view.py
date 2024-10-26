
# Diseñar menú de panel control: usuario, saldo actual o inicial, transacciones, historial de transacciones, Inversiones, Portafolio, Ayuda
from views.menu_basico_view import menu_basico_view

def session_panel_control_view():
    menu_principal_title = "Menú principal"
    menu_principal_opciones = {
        "1": ("Inversor", None),
        "2": ("Proyecto", None),
        "3": ("Cerrar sesión", None),
    }

    menu_basico_view(menu_principal_title, menu_principal_opciones)