# Diseñar menú de panel control: usuario, saldo actual o inicial, transacciones, historial de transacciones, Inversiones, Portafolio, Ayuda
from views.menu_basico_view import menu_basico_view
from views.sesion.submenues.informacion_usuario_view import informacion_usuario_view
from views.sesion.submenues.transacciones_view import transacciones_view
from views.sesion.submenues.inversiones_view import inversiones_view
from views.sesion.submenues.portafolio_view import portafolio_view
from views.sesion.submenues.ayuda_view import ayuda_view

def session_panel_control_view():
    menu_panel_control_title = "Menú principal"
    menu_panel_control_opciones = {
        "1": ("Información del usuario", informacion_usuario_view),
        "2": ("Transacciones", transacciones_view),
        "3": ("Inversiones", inversiones_view),
        "4": ("Portafolio", portafolio_view),
        "5": ("Ayuda", ayuda_view),
        "6": ("Cerrar sesión", None),
    }

    menu_basico_view(menu_panel_control_title, menu_panel_control_opciones)