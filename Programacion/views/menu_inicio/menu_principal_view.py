from views.menu_basico_view import menu_basico_view
from views.inversor.inversor_registrar_view import inversor_registrar_view
from views.inversor.inversor_login_view import inversor_login_view
from views.inversor.inversor_recuperar_contrasena_view import inversor_recuperar_contrasena_view
from views.menu_inicio.terminar_programa_view import terminar_programa_view

def mostrar_menu_principal_view(): 
    
    usuario_logueado = False
    menu_principal_title = "Menú principal"
    menu_principal_opciones = {
        "1": ("Registrar inversor", inversor_registrar_view),
        "2": ("Login inversor", inversor_login_view, usuario_logueado),
        "3": ("Recuperar contraseña", inversor_recuperar_contrasena_view),
        "4": ("Cerrar programa", terminar_programa_view),
    }

    menu_basico_view(menu_principal_title, menu_principal_opciones)

    if usuario_logueado:
        return True
