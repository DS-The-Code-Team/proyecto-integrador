from views.menu_basico_view import menu_basico_view
from views.sesion.resumen_cuenta_view import resumen_cuenta_view
from views.sesion.panel_control_view import session_panel_control_view

# resumen
# panel de control
""" 
def sesion_pantalla_principal_view():
    menu_principal_title = "Menú principal"
    menu_principal_opciones = {
        "1": ("Inversor", None),
        "2": ("Proyecto", None),
        "3": ("Cerrar sesión", None),
    }

    menu_basico_view(menu_principal_title, menu_principal_opciones) """

def sesion_pantalla_principal_view():
    resumen_cuenta_view()
    session_panel_control_view()