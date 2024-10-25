from view.menu_basico_view import menu_basico_view
from view.inversor_registrar_view import registrar_inversor_view
from view.inversor_login_view import login_inversor_view
from view.inversor_cerrar_sesion_view import cerrar_sesion_view
from view.inversor_recuperar_contrasena_view import recuperar_contrasena_view

def mostrar_menu_principal_view(): 
    
    menu_principal_title = "Menú principal"
    menu_principal_opciones = {
        "1": ("Registrar inversor", registrar_inversor_view),
        "2": ("Login inversor", login_inversor_view),
        "3": ("Recuperar contraseña", recuperar_contrasena_view),
        "4": ("Cerrar programa", cerrar_sesion_view)
    }

    menu_basico_view(menu_principal_title, menu_principal_opciones)
